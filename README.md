# EMG SFC Tools - Evolution Media Group Salesforce Tools

A collection of command-line tools for managing Salesforce data at Evolution Media Group.

## Features

### Salesforce Account Manager (`sf_account_manager.py`)
A comprehensive Python CLI tool for managing Salesforce Account objects via REST API.

#### Capabilities
- **Create** new accounts with custom field support
- **Update** existing accounts by ID or Account Number
- **List** accounts with advanced filtering and pagination
- **Export** account data to text files (pipe-delimited format)
- **Automatic pagination** for large datasets (>2000 records)
- **Extract** Website and Domain fields from accounts

## Installation

### Prerequisites
- Python 3.7 or higher
- Salesforce org with API access
- Connected App configured in Salesforce

### Setup Steps

1. Clone the repository:
```bash
git clone https://github.com/evolutionmediagroup/EMG_SFC_tools.git
cd EMG_SFC_tools
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure credentials:
```bash
# Copy example config file
cp config.ini.example config.ini

# Edit config.ini with your Salesforce credentials
# Or use environment variables (see .env.example)
```

## Configuration

### Method 1: Configuration File
Edit `config.ini` with your credentials:
```ini
[salesforce]
username = your_email@company.com
password = your_password
security_token = your_security_token
domain = login  # or 'test' for sandbox
consumer_key = your_consumer_key
consumer_secret = your_consumer_secret
```

### Method 2: Environment Variables
Set these environment variables:
- `SF_USERNAME`
- `SF_PASSWORD`
- `SF_SECURITY_TOKEN`
- `SF_DOMAIN`
- `SF_CONSUMER_KEY`
- `SF_CONSUMER_SECRET`

## Usage Examples

### List Accounts
```bash
# List 10 most recent accounts
python sf_account_manager.py --config config.ini list --limit 10

# List all accounts with specific record type
python sf_account_manager.py --config config.ini list --limit 0 --filter "RecordType.Name='Dealership'"

# Export to file
python sf_account_manager.py --config config.ini list --limit 0 --output-file accounts.txt
```

### Create Account
```bash
python sf_account_manager.py --config config.ini create \
  --name "Test Company" \
  --type "Prospect" \
  --industry "Technology"
```

### Update Account
```bash
python sf_account_manager.py --config config.ini update \
  --id "001XX000003DHP0" \
  --phone "555-1234" \
  --website "https://example.com"
```

### Advanced Filtering
```bash
# Filter by multiple criteria
python sf_account_manager.py --config config.ini list \
  --filter "Type='Customer' AND Industry='Technology'" \
  --limit 50

# Search by name pattern
python sf_account_manager.py --config config.ini list \
  --filter "Name LIKE '%Automotive%'"

# Filter by custom fields
python sf_account_manager.py --config config.ini list \
  --filter "Sub_Industry__c='Group' AND RecordType.Name='Client'"
```

## Output Format

### Console Output
Displays accounts in a formatted table with columns:
- ID
- Name
- Type
- Industry
- Phone
- Website
- Domain

### File Output
Pipe-delimited format with one account per line:
```
ID|Name|Type|Industry|Phone|Website|Domain|BillingCity|BillingState|CreatedDate
```

## Features

### Automatic Pagination
- Handles results beyond Salesforce's 2000 record limit
- Use `--limit 0` to fetch ALL records
- Pagination happens automatically without user intervention

### Field Extraction
The tool extracts these standard and custom fields:
- Standard: Id, Name, Type, Industry, Phone, BillingCity, BillingState, CreatedDate
- Web fields: Website, Domain__c
- Custom fields can be added as needed

## Salesforce Setup

### Creating a Connected App
1. Go to Setup → App Manager → New Connected App
2. Enable OAuth Settings
3. Add required OAuth scopes:
   - Access and manage your data (api)
   - Perform requests at any time (refresh_token, offline_access)
4. Save and note the Consumer Key and Consumer Secret

### Security Token
1. Go to Setup → My Personal Information → Reset My Security Token
2. Check email for the security token
3. Add to your configuration

## Troubleshooting

### Authentication Issues
- Verify username and password are correct
- Ensure security token is current (reset if needed)
- Check domain: use 'login' for production, 'test' for sandbox
- Verify Connected App is properly configured

### Field Errors
- Custom fields must include '__c' suffix
- Check field API names in Setup → Object Manager → Account → Fields

### Rate Limits
- The tool respects Salesforce API rate limits
- Large exports may take time due to pagination

## Contributing
Please follow existing code patterns and include documentation for any new features.

## License
Property of Evolution Media Group

## Support
For issues or questions, contact the EMG development team.