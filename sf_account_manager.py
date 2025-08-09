#!/usr/bin/env python3
"""
=================================================================================
SALESFORCE ACCOUNT MANAGER - COMMAND LINE TOOL
=================================================================================

SCRIPT DESCRIPTION:
------------------
A Python command-line tool for managing Salesforce Account objects via the 
Salesforce REST API. Provides functionality to create new accounts and update 
existing accounts with comprehensive error handling and logging capabilities.

SCRIPT SETUP REQUIREMENTS:
--------------------------
1. Python 3.7+ installed
2. Required Python packages (install via: pip install -r requirements.txt):
   - simple-salesforce>=1.12.0
   - python-dotenv>=0.19.0
   - argparse (built-in)
   - json (built-in)
   - logging (built-in)
   - configparser (built-in)

3. Salesforce Connected App with API access:
   - Consumer Key
   - Consumer Secret
   - Username with API permissions
   - Password + Security Token

4. Configuration file (config.ini) or environment variables:
   - SF_USERNAME: Salesforce username
   - SF_PASSWORD: Salesforce password
   - SF_SECURITY_TOKEN: Salesforce security token
   - SF_DOMAIN: Salesforce domain (default: login)
   - SF_CONSUMER_KEY: Connected App Consumer Key
   - SF_CONSUMER_SECRET: Connected App Consumer Secret

SCRIPT USAGE INSTRUCTIONS:
--------------------------
Basic Usage:
  python sf_account_manager.py --help

Create Account:
  python sf_account_manager.py create --name "Acme Corp" --type "Customer"
  python sf_account_manager.py create --name "Test Company" --type "Prospect" --industry "Technology"

Update Account:
  python sf_account_manager.py update --id "001XX000003DHP0" --name "Updated Name"
  python sf_account_manager.py update --account-number "ACC-001" --phone "555-1234"

List Accounts:
  python sf_account_manager.py list --limit 10
  python sf_account_manager.py list --filter "Type='Customer'"

Options:
  --config: Specify custom configuration file path
  --verbose: Enable verbose logging
  --dry-run: Preview operations without making changes

RUNNING CHANGE LOG:
-------------------
Version 1.0.0 (Initial Release):
- Created initial command-line interface structure
- Implemented Salesforce authentication using simple-salesforce
- Added account creation functionality with required fields validation
- Added account update functionality with flexible field updates
- Implemented comprehensive error handling and logging
- Added support for configuration files and environment variables
- Created list functionality for viewing existing accounts
- Added dry-run mode for testing operations
- Included detailed help documentation and usage examples
- Reason: Initial implementation to provide basic CRUD operations for Salesforce accounts

=================================================================================
"""

import argparse
import json
import logging
import os
import sys
from configparser import ConfigParser
from typing import Dict, List, Optional, Any

try:
    from simple_salesforce import Salesforce, SalesforceLogin, SFType
    from simple_salesforce.exceptions import SalesforceAuthenticationFailed, SalesforceMoreThanOneRecord, SalesforceResourceNotFound
except ImportError:
    print("Error: simple-salesforce package not installed. Run: pip install simple-salesforce")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    print("Warning: python-dotenv not installed. Environment variables from .env file won't be loaded.")
    load_dotenv = None

__version__ = "1.0.0"

class SalesforceAccountManager:
    def __init__(self, config_path: Optional[str] = None, verbose: bool = False):
        self.sf = None
        self.verbose = verbose
        self.setup_logging()
        self.load_configuration(config_path)
        
    def setup_logging(self):
        log_level = logging.DEBUG if self.verbose else logging.INFO
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('sf_account_manager.log')
            ]
        )
        self.logger = logging.getLogger(__name__)

    def load_configuration(self, config_path: Optional[str] = None):
        if load_dotenv:
            load_dotenv()
        
        self.config = {}
        
        if config_path and os.path.exists(config_path):
            parser = ConfigParser()
            parser.read(config_path)
            if 'salesforce' in parser.sections():
                self.config.update(dict(parser['salesforce']))
                self.logger.info(f"Loaded configuration from {config_path}")
        
        required_keys = ['username', 'password', 'security_token']
        env_mapping = {
            'username': 'SF_USERNAME',
            'password': 'SF_PASSWORD', 
            'security_token': 'SF_SECURITY_TOKEN',
            'domain': 'SF_DOMAIN',
            'consumer_key': 'SF_CONSUMER_KEY',
            'consumer_secret': 'SF_CONSUMER_SECRET'
        }
        
        for key, env_var in env_mapping.items():
            if key not in self.config:
                env_value = os.getenv(env_var)
                if env_value:
                    self.config[key] = env_value
        
        self.config.setdefault('domain', 'login')
        
        missing_keys = [key for key in required_keys if key not in self.config or not self.config[key]]
        if missing_keys:
            self.logger.error(f"Missing required configuration: {', '.join(missing_keys)}")
            raise ValueError(f"Missing required configuration keys: {missing_keys}")

    def authenticate(self):
        try:
            self.logger.info("Authenticating with Salesforce...")
            
            auth_params = {
                'username': self.config['username'],
                'password': self.config['password'],
                'security_token': self.config['security_token'],
                'domain': self.config['domain']
            }
            
            if self.config.get('consumer_key') and self.config.get('consumer_secret'):
                auth_params.update({
                    'consumer_key': self.config['consumer_key'],
                    'consumer_secret': self.config['consumer_secret']
                })
            
            self.sf = Salesforce(**auth_params)
            self.logger.info("Successfully authenticated with Salesforce")
            return True
            
        except SalesforceAuthenticationFailed as e:
            self.logger.error(f"Salesforce authentication failed: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error during authentication: {e}")
            return False

    def create_account(self, account_data: Dict[str, Any], dry_run: bool = False) -> Optional[str]:
        if not self.sf:
            if not self.authenticate():
                return None
        
        required_fields = ['Name']
        missing_fields = [field for field in required_fields if field not in account_data or not account_data[field]]
        
        if missing_fields:
            self.logger.error(f"Missing required fields for account creation: {missing_fields}")
            return None
        
        try:
            self.logger.info(f"Creating account: {account_data['Name']}")
            
            if dry_run:
                self.logger.info(f"DRY RUN: Would create account with data: {json.dumps(account_data, indent=2)}")
                return "dry_run_id"
            
            result = self.sf.Account.create(account_data)
            account_id = result['id']
            
            self.logger.info(f"Successfully created account with ID: {account_id}")
            return account_id
            
        except Exception as e:
            self.logger.error(f"Error creating account: {e}")
            return None

    def update_account(self, identifier: str, account_data: Dict[str, Any], 
                      identifier_type: str = 'id', dry_run: bool = False) -> bool:
        if not self.sf:
            if not self.authenticate():
                return False
        
        try:
            if identifier_type == 'id':
                account_id = identifier
            else:
                accounts = self._find_accounts_by_field(identifier_type, identifier)
                if not accounts:
                    self.logger.error(f"No account found with {identifier_type}: {identifier}")
                    return False
                if len(accounts) > 1:
                    self.logger.error(f"Multiple accounts found with {identifier_type}: {identifier}")
                    return False
                account_id = accounts[0]['Id']
            
            self.logger.info(f"Updating account ID: {account_id}")
            
            if dry_run:
                self.logger.info(f"DRY RUN: Would update account {account_id} with data: {json.dumps(account_data, indent=2)}")
                return True
            
            result = self.sf.Account.update(account_id, account_data)
            
            if result == 204:
                self.logger.info(f"Successfully updated account: {account_id}")
                return True
            else:
                self.logger.warning(f"Unexpected response code: {result}")
                return False
                
        except SalesforceResourceNotFound:
            self.logger.error(f"Account not found with ID: {account_id}")
            return False
        except Exception as e:
            self.logger.error(f"Error updating account: {e}")
            return False

    def list_accounts(self, limit: int = 10, filter_clause: str = None, output_file: str = None) -> Optional[List[Dict]]:
        if not self.sf:
            if not self.authenticate():
                return None
        
        try:
            base_query = "SELECT Id, Name, Type, Industry, Phone, Website, Domain__c, BillingCity, BillingState, CreatedDate FROM Account"
            
            if filter_clause:
                query = f"{base_query} WHERE {filter_clause}"
            else:
                query = base_query
            
            query += " ORDER BY CreatedDate DESC"
            
            # Handle pagination automatically
            all_accounts = []
            
            # If limit is 0 (get all) or > 2000, use query_all for automatic pagination
            if limit == 0:
                self.logger.info(f"Executing query (fetching ALL records): {query}")
                # Use query_all which handles pagination automatically
                result = self.sf.query_all(query)
                all_accounts = result['records']
                self.logger.info(f"Total accounts retrieved: {len(all_accounts)}")
            elif limit > 2000:
                # For limits > 2000, we need to handle pagination manually
                self.logger.info(f"Executing query (fetching up to {limit} records): {query}")
                result = self.sf.query(query)
                all_accounts.extend(result['records'])
                total_retrieved = len(result['records'])
                
                # Continue fetching if more records exist and we haven't reached our limit
                while 'nextRecordsUrl' in result and total_retrieved < limit:
                    self.logger.info(f"Fetching more records... (retrieved {total_retrieved} so far)")
                    result = self.sf.query_more(result['nextRecordsUrl'], identifier_is_url=True)
                    
                    # Add records up to our limit
                    if total_retrieved + len(result['records']) > limit:
                        records_to_add = limit - total_retrieved
                        all_accounts.extend(result['records'][:records_to_add])
                        total_retrieved = limit
                        break
                    else:
                        all_accounts.extend(result['records'])
                        total_retrieved += len(result['records'])
                
                self.logger.info(f"Total accounts retrieved: {len(all_accounts)}")
            else:
                # For small limits, use simple query with LIMIT clause
                query_with_limit = f"{query} LIMIT {limit}"
                self.logger.info(f"Executing query: {query_with_limit}")
                result = self.sf.query(query_with_limit)
                all_accounts = result['records']
                self.logger.info(f"Total accounts retrieved: {len(all_accounts)}")
            
            if output_file:
                self._write_accounts_to_file(all_accounts, output_file)
            
            return all_accounts
            
        except Exception as e:
            self.logger.error(f"Error listing accounts: {e}")
            return None

    def _write_accounts_to_file(self, accounts: List[Dict], output_file: str):
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                for account in accounts:
                    line_parts = []
                    
                    # Format: ID|Name|Type|Industry|Phone|Website|Domain|BillingCity|BillingState|CreatedDate
                    fields = ['Id', 'Name', 'Type', 'Industry', 'Phone', 'Website', 'Domain__c', 'BillingCity', 'BillingState', 'CreatedDate']
                    
                    for field in fields:
                        value = account.get(field, '') or ''
                        # Clean the value and escape any pipe characters
                        clean_value = str(value).replace('|', '\\|').replace('\n', ' ').replace('\r', ' ').strip()
                        line_parts.append(clean_value)
                    
                    f.write('|'.join(line_parts) + '\n')
                    
            self.logger.info(f"Successfully wrote {len(accounts)} accounts to {output_file}")
            
        except Exception as e:
            self.logger.error(f"Error writing accounts to file {output_file}: {e}")

    def _find_accounts_by_field(self, field_name: str, field_value: str) -> List[Dict]:
        try:
            query = f"SELECT Id, Name FROM Account WHERE {field_name} = '{field_value}'"
            result = self.sf.query(query)
            return result['records']
        except Exception as e:
            self.logger.error(f"Error finding accounts by {field_name}: {e}")
            return []


def main():
    parser = argparse.ArgumentParser(
        description='Salesforce Account Manager - Create and update Salesforce accounts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s create --name "Acme Corp" --type "Customer"
  %(prog)s update --id "001XX000003DHP0" --name "New Name"
  %(prog)s list --limit 5
        """
    )
    
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--dry-run', action='store_true', help='Preview operations without making changes')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    create_parser = subparsers.add_parser('create', help='Create a new account')
    create_parser.add_argument('--name', required=True, help='Account name (required)')
    create_parser.add_argument('--type', help='Account type (e.g., Customer, Prospect)')
    create_parser.add_argument('--industry', help='Industry')
    create_parser.add_argument('--phone', help='Phone number')
    create_parser.add_argument('--website', help='Website URL')
    create_parser.add_argument('--billing-street', help='Billing street address')
    create_parser.add_argument('--billing-city', help='Billing city')
    create_parser.add_argument('--billing-state', help='Billing state')
    create_parser.add_argument('--billing-postal-code', help='Billing postal code')
    create_parser.add_argument('--billing-country', help='Billing country')
    create_parser.add_argument('--account-number', help='Account number')
    
    update_parser = subparsers.add_parser('update', help='Update an existing account')
    update_group = update_parser.add_mutually_exclusive_group(required=True)
    update_group.add_argument('--id', help='Account ID')
    update_group.add_argument('--account-number', help='Account Number')
    update_parser.add_argument('--name', help='Account name')
    update_parser.add_argument('--type', help='Account type')
    update_parser.add_argument('--industry', help='Industry')
    update_parser.add_argument('--phone', help='Phone number')
    update_parser.add_argument('--website', help='Website URL')
    update_parser.add_argument('--billing-street', help='Billing street address')
    update_parser.add_argument('--billing-city', help='Billing city')
    update_parser.add_argument('--billing-state', help='Billing state')
    update_parser.add_argument('--billing-postal-code', help='Billing postal code')
    update_parser.add_argument('--billing-country', help='Billing country')
    
    list_parser = subparsers.add_parser('list', help='List accounts')
    list_parser.add_argument('--limit', type=int, default=10, help='Number of records to return (default: 10, 0 for all)')
    list_parser.add_argument('--filter', help='SOQL WHERE clause filter')
    list_parser.add_argument('--output-file', help='Output results to text file (one record per line)')
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()
    
    try:
        manager = SalesforceAccountManager(config_path=args.config, verbose=args.verbose)
        
        if args.command == 'create':
            account_data = {'Name': args.name}
            
            field_mapping = {
                'type': 'Type',
                'industry': 'Industry', 
                'phone': 'Phone',
                'website': 'Website',
                'billing_street': 'BillingStreet',
                'billing_city': 'BillingCity',
                'billing_state': 'BillingState',
                'billing_postal_code': 'BillingPostalCode',
                'billing_country': 'BillingCountry',
                'account_number': 'AccountNumber'
            }
            
            for arg_name, sf_field in field_mapping.items():
                value = getattr(args, arg_name.replace('_', '_'))
                if value:
                    account_data[sf_field] = value
            
            account_id = manager.create_account(account_data, dry_run=args.dry_run)
            if account_id and not args.dry_run:
                print(f"Created account with ID: {account_id}")
            elif account_id and args.dry_run:
                print("Dry run completed successfully")
            else:
                print("Failed to create account")
                sys.exit(1)
                
        elif args.command == 'update':
            account_data = {}
            
            field_mapping = {
                'name': 'Name',
                'type': 'Type',
                'industry': 'Industry',
                'phone': 'Phone', 
                'website': 'Website',
                'billing_street': 'BillingStreet',
                'billing_city': 'BillingCity',
                'billing_state': 'BillingState',
                'billing_postal_code': 'BillingPostalCode',
                'billing_country': 'BillingCountry'
            }
            
            for arg_name, sf_field in field_mapping.items():
                value = getattr(args, arg_name)
                if value:
                    account_data[sf_field] = value
            
            if not account_data:
                print("No fields to update specified")
                sys.exit(1)
            
            if args.id:
                success = manager.update_account(args.id, account_data, 'Id', dry_run=args.dry_run)
            else:
                success = manager.update_account(args.account_number, account_data, 'AccountNumber', dry_run=args.dry_run)
            
            if success:
                print("Account updated successfully" if not args.dry_run else "Dry run completed successfully")
            else:
                print("Failed to update account")
                sys.exit(1)
                
        elif args.command == 'list':
            output_file = getattr(args, 'output_file', None)
            accounts = manager.list_accounts(limit=args.limit, filter_clause=args.filter, output_file=output_file)
            if accounts is not None:
                if accounts:
                    if output_file:
                        print(f"Successfully wrote {len(accounts)} accounts to {output_file}")
                    else:
                        print(f"{'ID':<18} {'Name':<25} {'Type':<12} {'Industry':<15} {'Phone':<15} {'Website':<25} {'Domain':<20}")
                        print("-" * 135)
                        for account in accounts:
                            print(f"{account['Id']:<18} {(account.get('Name') or '')[:24]:<25} "
                                  f"{(account.get('Type') or '')[:11]:<12} {(account.get('Industry') or '')[:14]:<15} "
                                  f"{(account.get('Phone') or '')[:14]:<15} {(account.get('Website') or '')[:24]:<25} "
                                  f"{(account.get('Domain__c') or '')[:19]:<20}")
                else:
                    print("No accounts found")
            else:
                print("Failed to retrieve accounts")
                sys.exit(1)
                
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()