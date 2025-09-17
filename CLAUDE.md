# Salesforce API Tools Project
## Claude Code Configuration and Development Guide

---

## Project Overview

This repository contains Salesforce API automation tools for Evolution Media Group, supporting both **Python scripts** and **Airtable JavaScript automations**:

**Python Tools:**
- **sf_account_manager.py v1.0.0** - Complete CRUD operations for Salesforce Account objects
- **Salesforce Base Framework** - Reusable authentication and API patterns
- **Data Migration Tools** - Bulk import/export utilities for Salesforce data
- **Custom Object Managers** - Dynamic tools for custom Salesforce objects

**Airtable JavaScript Automations:**
- **Salesforce Sync Libraries** - Two-way data synchronization between Airtable and Salesforce
- **Real-time Validation** - Salesforce field validation in Airtable interfaces
- **Automated Workflows** - Trigger-based Salesforce operations from Airtable events
- **Bulk Operations** - Efficient batch processing for large datasets

---

## Quick Commands

### Development & Testing
```bash
# Test Salesforce authentication
python account_tools/sf_account_manager.py --config account_tools/config.ini list --limit 1

# Validate configuration files
python -c "import configparser; c=configparser.ConfigParser(); c.read('account_tools/config.ini'); print('Config valid')"

# Test account creation (dry run)
python account_tools/sf_account_manager.py --config account_tools/config.ini create --name "Test Account" --type "Prospect" --dry-run

# Run comprehensive account export
python account_tools/sf_account_manager.py --config account_tools/config.ini list --limit 0 --output-file full_export.txt

# Check API rate limiting
python utility/testing/test_salesforce_rate_limits.py

# Validate SOQL queries
python utility/testing/validate_soql_queries.py
```

### Python Salesforce Operations
```bash
# List recent accounts with filtering
python account_tools/sf_account_manager.py --config account_tools/config.ini list --limit 50 --filter "Type='Customer'"

# Bulk account updates from CSV
python tools/bulk_account_updater.py --config account_tools/config.ini --input-file updates.csv

# Export specific record types
python account_tools/sf_account_manager.py --config account_tools/config.ini list --filter "RecordType.Name='Dealership'" --output-file dealerships.txt

# Custom object data management
python tools/custom_object_manager.py --config account_tools/config.ini --object "Custom_Object__c" --operation list
```

### Airtable JavaScript Validation
```bash
# Validate Airtable automation scripts with Salesforce integrations
node -c scripts/airtable/SalesforceSync.js
node -c scripts/airtable/SalesforceValidator.js

# Test Airtable-Salesforce connection
node utility/testing/test_airtable_sf_connection.js

# Validate Salesforce API responses in Airtable context
node utility/testing/validate_sf_responses_airtable.js
```

### Git Workflow for Salesforce Projects
```bash
# Version increment commit pattern for Salesforce tools
git add -A
git commit -m "feat: enhance Salesforce API authentication (v1.2.3)

- Added OAuth 2.0 JWT bearer flow support
- Enhanced session management for long-running operations
- Added automatic token refresh capabilities
- Why: Need secure, scalable authentication for production deployments

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

## Project Structure for Salesforce API Tools

### Salesforce-Specific Directory Layout
```
~/work/SFC_API/
├── docs/                                # Documentation
│   ├── prompts/                         # Development history
│   │   └── SFC_API_PromptHistory.md     # MANDATORY: Complete prompt history
│   ├── salesforce/                      # Salesforce-specific docs
│   │   ├── object-schemas/              # Salesforce object documentation
│   │   ├── field-mappings/              # Custom field documentation
│   │   └── api-limits/                  # Rate limiting documentation
│   └── integration-guides/              # Third-party integration docs
├── account_tools/                       # Python account management tools
│   ├── sf_account_manager.py            # Main account CRUD tool
│   ├── config.ini                       # Salesforce credentials
│   ├── requirements.txt                 # Python dependencies
│   └── README.md                        # Tool documentation
├── tools/                               # Additional Python Salesforce tools
│   ├── contact_manager/                 # Contact CRUD operations
│   ├── opportunity_manager/             # Opportunity management
│   ├── campaign_manager/                # Campaign operations
│   ├── bulk_operations/                 # Bulk data tools
│   └── custom_object_tools/             # Dynamic object managers
├── scripts/                             # Airtable JavaScript automations
│   ├── airtable/                        # Airtable automation scripts
│   │   ├── current/                     # Production Airtable automations
│   │   │   ├── SalesforceSync.js        # Two-way Airtable-Salesforce sync
│   │   │   ├── SalesforceValidator.js   # Real-time validation library
│   │   │   ├── AccountManager.js        # Account operations for Airtable
│   │   │   ├── ContactManager.js        # Contact operations for Airtable
│   │   │   └── BulkOperations.js        # Batch processing for Airtable
│   │   └── libraries/                   # Shared JavaScript libraries
│   │       ├── SalesforceAPI.js         # Core Salesforce API wrapper
│   │       ├── SalesforceAuth.js        # Authentication utilities
│   │       └── SalesforceLogger.js      # Logging for Airtable automations
├── utility/                             # Utilities and testing
│   ├── testing/                         # Test scripts (Python & JavaScript)
│   │   ├── test_authentication.py       # Python auth testing
│   │   ├── test_rate_limits.py          # Python rate limit testing
│   │   ├── validate_soql_queries.py     # SOQL validation
│   │   ├── test_airtable_sf_connection.js # Airtable-Salesforce connection test
│   │   └── validate_sf_responses_airtable.js # Airtable API response validation
│   ├── salesforce_base/                 # Base classes and utilities
│   │   ├── sf_base_manager.py           # Base authentication class
│   │   ├── sf_query_builder.py          # SOQL query utilities
│   │   └── sf_rate_limiter.py           # Rate limiting utilities
│   └── data_migration/                  # Migration utilities
│       ├── csv_importer.py              # CSV to Salesforce
│       ├── data_mapper.py               # Field mapping utilities
│       └── relationship_handler.py      # Related record management
├── config/                              # Configuration management
│   ├── environments/                    # Environment-specific configs
│   │   ├── config.ini                   # Production (no suffix)
│   │   ├── config-dev.ini               # Development
│   │   └── config-sandbox.ini           # Sandbox
│   ├── salesforce/                      # Salesforce configurations
│   │   ├── connected-apps.json          # Connected App settings
│   │   ├── object-mappings.json         # Object field mappings
│   │   └── api-versions.json            # Supported API versions
│   └── security/                        # Security configurations
│       ├── oauth-settings.json          # OAuth configurations
│       └── encryption-keys.json         # Encryption settings
├── data/                                # Data files and schemas
│   ├── schemas/                         # Salesforce object schemas
│   │   ├── Account_Schema.json          # Account object definition
│   │   ├── Contact_Schema.json          # Contact object definition
│   │   └── Custom_Objects_Schema.json   # Custom object definitions
│   ├── samples/                         # Sample data files
│   │   ├── sample_accounts.csv          # Sample account data
│   │   └── sample_contacts.csv          # Sample contact data
│   └── exports/                         # Data export files
│       └── (generated export files)
├── deploy/                              # Deployment configurations
│   ├── salesforce/                      # Salesforce deployment
│   │   ├── connected-app-setup.md       # Connected App setup guide
│   │   └── permission-sets.xml          # Required permissions
│   └── environments/                    # Environment deployment
│       ├── production/                  # Production deployment
│       └── sandbox/                     # Sandbox deployment
└── deprecated/                          # Legacy code
    └── versions/                        # Previous versions
```

---

## Salesforce API Development Conventions

This project supports dual-platform development for Salesforce API integrations:
- **Python Scripts**: Server-side automation, bulk operations, data migration
- **Airtable JavaScript**: Real-time validation, user interfaces, workflow automation

### Python Script Standards for Salesforce

#### Version Management for Salesforce Tools
```python
#!/usr/bin/env python3
"""
Salesforce Tool Name
Description of Salesforce functionality

@version X.Y.Z - Brief description of changes
@release-date YYYY-MM-DD
@status Production Ready|Development|Testing
@salesforce-api-version 58.0
@required-permissions API, Account:Read, Account:Write

CHANGELOG:
v1.2.0 (2024-12-19) - Enhanced bulk operations support
  - Added Bulk API 2.0 integration for large datasets
  - Enhanced error handling for partial failures
  - Added automatic retry logic for rate limit exceptions
  - Why: Need to handle 10K+ record operations efficiently

v1.1.0 (2024-12-18) - OAuth 2.0 JWT Bearer flow
  - Added JWT bearer authentication for server-to-server
  - Enhanced session management for long-running operations
  - Added automatic token refresh capabilities
  - Why: Username/password flow deprecated in production environments
"""

# Version constants - MANDATORY for all Salesforce tools
SCRIPT_VERSION = "1.2.0"
SCRIPT_NAME = "SalesforceAccountManager"
RELEASE_DATE = "2024-12-19"
SCRIPT_STATUS = "Production Ready"
SALESFORCE_API_VERSION = "58.0"
REQUIRED_PERMISSIONS = ["API", "Account:Read", "Account:Write"]
```

#### Salesforce Authentication Patterns

**Base Authentication Class:**
```python
import logging
from simple_salesforce import Salesforce
from simple_salesforce.exceptions import SalesforceAuthenticationFailed

class SalesforceBaseManager:
    """Base class for all Salesforce API tools with standardized authentication"""

    def __init__(self, config_path: str = None, verbose: bool = False):
        self.sf = None
        self.session_info = {}
        self.api_version = "58.0"
        self.setup_logging(verbose)
        self.load_configuration(config_path)

    def setup_logging(self, verbose: bool):
        """Standardized logging setup for Salesforce tools"""
        log_level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(f'{self.__class__.__name__.lower()}.log')
            ]
        )
        self.logger = logging.getLogger(self.__class__.__name__)

    def authenticate(self) -> bool:
        """Authenticate with Salesforce using configured method"""
        try:
            self.logger.info(f"Authenticating with Salesforce API v{self.api_version}...")

            auth_params = {
                'username': self.config['username'],
                'password': self.config['password'],
                'security_token': self.config['security_token'],
                'domain': self.config.get('domain', 'login'),
                'version': self.api_version
            }

            # Add Connected App credentials if available
            if self.config.get('consumer_key') and self.config.get('consumer_secret'):
                auth_params.update({
                    'consumer_key': self.config['consumer_key'],
                    'consumer_secret': self.config['consumer_secret']
                })

            self.sf = Salesforce(**auth_params)

            # Store session information
            self.session_info = {
                'session_id': self.sf.session_id,
                'server_url': self.sf.sf_instance,
                'api_version': self.api_version,
                'org_id': self._get_org_id()
            }

            self.logger.info(f"Successfully authenticated with {self.session_info['server_url']}")
            return True

        except SalesforceAuthenticationFailed as e:
            self.logger.error(f"Salesforce authentication failed: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected authentication error: {e}")
            return False

    def _get_org_id(self) -> str:
        """Get Salesforce organization ID"""
        try:
            org_query = self.sf.query("SELECT Id FROM Organization LIMIT 1")
            return org_query['records'][0]['Id'] if org_query['records'] else None
        except Exception as e:
            self.logger.warning(f"Could not retrieve Org ID: {e}")
            return None
```

#### Salesforce API Logging Standards

**Enhanced API Logging for Salesforce:**
```python
class SalesforceLogger:
    """Specialized logger for Salesforce API operations"""

    def __init__(self, script_name: str, version: str, org_id: str = None):
        self.script_name = script_name
        self.version = version
        self.org_id = org_id
        self.request_id = f"sf_{int(time.time())}"

    def log_soql_query(self, query: str, record_count: int = None, duration_ms: int = None):
        """Log SOQL query execution"""
        self.logger.info(f"🔍 SOQL QUERY [{self.request_id}]")
        self.logger.info(f"   Query: {query}")
        if record_count is not None:
            self.logger.info(f"   Records Returned: {record_count}")
        if duration_ms is not None:
            self.logger.info(f"   Duration: {duration_ms}ms")

    def log_dml_operation(self, operation: str, object_type: str, record_count: int,
                         success_count: int = None, error_count: int = None):
        """Log DML operations (Insert, Update, Delete)"""
        self.logger.info(f"📝 DML OPERATION [{self.request_id}]")
        self.logger.info(f"   Operation: {operation}")
        self.logger.info(f"   Object: {object_type}")
        self.logger.info(f"   Records Processed: {record_count}")
        if success_count is not None:
            self.logger.info(f"   Successful: {success_count}")
        if error_count is not None:
            self.logger.info(f"   Errors: {error_count}")

    def log_api_limits(self, limits_info: dict):
        """Log current API usage limits"""
        self.logger.info(f"📊 API LIMITS [{self.request_id}]")
        for limit_type, info in limits_info.items():
            if isinstance(info, dict) and 'Remaining' in info:
                remaining = info['Remaining']
                max_limit = info.get('Max', 'Unknown')
                self.logger.info(f"   {limit_type}: {remaining}/{max_limit} remaining")
```

#### Error Handling for Salesforce Operations

**Salesforce-Specific Error Patterns:**
```python
from simple_salesforce.exceptions import (
    SalesforceAuthenticationFailed,
    SalesforceResourceNotFound,
    SalesforceMoreThanOneRecord,
    SalesforceError
)

def handle_salesforce_errors(func):
    """Decorator for standardized Salesforce error handling"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SalesforceAuthenticationFailed as e:
            logger.error(f"Authentication failed: {e}")
            # Attempt re-authentication
            if hasattr(args[0], 'authenticate'):
                args[0].authenticate()
                return func(*args, **kwargs)
            raise
        except SalesforceResourceNotFound as e:
            logger.error(f"Resource not found: {e}")
            return None
        except SalesforceMoreThanOneRecord as e:
            logger.error(f"Multiple records found: {e}")
            raise ValueError("Query returned multiple records when expecting one")
        except SalesforceError as e:
            logger.error(f"Salesforce API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
    return wrapper

@handle_salesforce_errors
def get_account_by_id(self, account_id: str) -> dict:
    """Get account by ID with error handling"""
    return self.sf.Account.get(account_id)
```

### Airtable JavaScript Standards for Salesforce

#### Version Management for Airtable Salesforce Automations
```javascript
/**
 * Airtable Salesforce Integration Script
 * Description of Salesforce functionality for Airtable
 *
 * @version X.Y.Z - Brief description of changes
 * @release-date YYYY-MM-DD
 * @status Production Ready|Development|Testing
 * @salesforce-api-version 58.0
 * @airtable-blocks-sdk 1.0.0
 * @required-permissions Salesforce:API, Airtable:Read, Airtable:Write
 *
 * CHANGELOG:
 * v1.2.0 (2024-12-19) - Enhanced real-time sync capabilities
 *   - Added bidirectional field mapping between Airtable and Salesforce
 *   - Enhanced error handling for partial sync failures
 *   - Added progress indicators for long-running operations
 *   - Why: Need seamless data flow between Airtable interfaces and Salesforce
 *
 * v1.1.0 (2024-12-18) - OAuth 2.0 integration for Airtable
 *   - Added secure OAuth flow for Airtable automations
 *   - Enhanced session management for persistent connections
 *   - Added automatic token refresh in Airtable context
 *   - Why: Username/password not suitable for client-side Airtable automations
 */

// Version constants - MANDATORY for all Airtable Salesforce scripts
const SCRIPT_VERSION = "1.2.0";
const SCRIPT_NAME = "AirtableSalesforceSync";
const RELEASE_DATE = "2024-12-19";
const SCRIPT_STATUS = "Production Ready";
const SALESFORCE_API_VERSION = "58.0";
const AIRTABLE_BLOCKS_SDK_VERSION = "1.0.0";
const REQUIRED_PERMISSIONS = ["Salesforce:API", "Airtable:Read", "Airtable:Write"];
```

#### Airtable Salesforce Authentication Patterns

**Salesforce OAuth for Airtable Automations:**
```javascript
/**
 * Salesforce Authentication Manager for Airtable
 * Handles OAuth 2.0 flow and session management in Airtable context
 */
class AirtableSalesforceAuth {
    constructor(clientId, clientSecret, redirectUri, baseUrl = "https://login.salesforce.com") {
        this.clientId = clientId;
        this.clientSecret = clientSecret;
        this.redirectUri = redirectUri;
        this.baseUrl = baseUrl;
        this.accessToken = null;
        this.refreshToken = null;
        this.instanceUrl = null;
        this.apiVersion = "v58.0";
    }

    /**
     * Authenticate using OAuth 2.0 Authorization Code flow
     * Suitable for Airtable automations with user interaction
     */
    async authenticateOAuth(authorizationCode) {
        const logger = new AirtableSalesforceLogger(SCRIPT_NAME, SCRIPT_VERSION);

        try {
            logger.logStart("Starting OAuth authentication flow...");

            const tokenUrl = `${this.baseUrl}/services/oauth2/token`;
            const tokenParams = {
                grant_type: "authorization_code",
                client_id: this.clientId,
                client_secret: this.clientSecret,
                redirect_uri: this.redirectUri,
                code: authorizationCode
            };

            // Log OAuth request (without sensitive data)
            logger.logApiRequest("Salesforce OAuth", "POST", tokenUrl, {
                "Content-Type": "application/x-www-form-urlencoded"
            }, { grant_type: tokenParams.grant_type, client_id: tokenParams.client_id });

            const response = await this._makeHttpRequest(tokenUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: new URLSearchParams(tokenParams)
            });

            if (response.access_token) {
                this.accessToken = response.access_token;
                this.refreshToken = response.refresh_token;
                this.instanceUrl = response.instance_url;

                logger.logSuccess(`OAuth authentication successful. Instance: ${this.instanceUrl}`);
                return true;
            } else {
                logger.logError("OAuth authentication failed: No access token received");
                return false;
            }

        } catch (error) {
            logger.logError(`OAuth authentication error: ${error.message}`);
            return false;
        }
    }

    /**
     * Refresh access token using refresh token
     * Critical for long-running Airtable automations
     */
    async refreshAccessToken() {
        const logger = new AirtableSalesforceLogger(SCRIPT_NAME, SCRIPT_VERSION);

        if (!this.refreshToken) {
            logger.logError("No refresh token available for token refresh");
            return false;
        }

        try {
            const tokenUrl = `${this.baseUrl}/services/oauth2/token`;
            const tokenParams = {
                grant_type: "refresh_token",
                client_id: this.clientId,
                client_secret: this.clientSecret,
                refresh_token: this.refreshToken
            };

            logger.logApiRequest("Salesforce Token Refresh", "POST", tokenUrl, {
                "Content-Type": "application/x-www-form-urlencoded"
            }, { grant_type: tokenParams.grant_type });

            const response = await this._makeHttpRequest(tokenUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: new URLSearchParams(tokenParams)
            });

            if (response.access_token) {
                this.accessToken = response.access_token;
                logger.logSuccess("Access token refreshed successfully");
                return true;
            } else {
                logger.logError("Token refresh failed: No access token received");
                return false;
            }

        } catch (error) {
            logger.logError(`Token refresh error: ${error.message}`);
            return false;
        }
    }

    /**
     * Make authenticated HTTP request to Salesforce
     * Automatically handles token refresh on 401 errors
     */
    async makeAuthenticatedRequest(endpoint, options = {}) {
        const logger = new AirtableSalesforceLogger(SCRIPT_NAME, SCRIPT_VERSION);

        if (!this.accessToken) {
            throw new Error("No access token available. Please authenticate first.");
        }

        const url = `${this.instanceUrl}/services/data/${this.apiVersion}/${endpoint}`;
        const headers = {
            "Authorization": `Bearer ${this.accessToken}`,
            "Content-Type": "application/json",
            ...options.headers
        };

        const requestOptions = {
            ...options,
            headers
        };

        logger.logApiRequest("Salesforce API", options.method || "GET", url, headers, options.body);

        try {
            const response = await this._makeHttpRequest(url, requestOptions);
            logger.logApiResponse("Salesforce API", 200, {}, response, 0);
            return response;

        } catch (error) {
            // Handle 401 Unauthorized - attempt token refresh
            if (error.status === 401 && this.refreshToken) {
                logger.logWarning("Access token expired, attempting refresh...");

                const refreshSuccess = await this.refreshAccessToken();
                if (refreshSuccess) {
                    // Retry with new token
                    const retryHeaders = {
                        ...headers,
                        "Authorization": `Bearer ${this.accessToken}`
                    };
                    const retryOptions = { ...requestOptions, headers: retryHeaders };

                    logger.logApiRequest("Salesforce API Retry", options.method || "GET", url, retryHeaders, options.body);
                    const retryResponse = await this._makeHttpRequest(url, retryOptions);
                    logger.logApiResponse("Salesforce API Retry", 200, {}, retryResponse, 0);
                    return retryResponse;
                }
            }

            logger.logApiError("Salesforce API", error, { endpoint, method: options.method });
            throw error;
        }
    }

    async _makeHttpRequest(url, options) {
        const response = await fetch(url, options);
        const data = await response.json();

        if (!response.ok) {
            const error = new Error(data.error_description || data.message || 'HTTP request failed');
            error.status = response.status;
            error.data = data;
            throw error;
        }

        return data;
    }
}
```

#### Airtable Salesforce API Operations

**Salesforce CRUD Operations for Airtable:**
```javascript
/**
 * Salesforce API Manager for Airtable Automations
 * Provides CRUD operations optimized for Airtable workflows
 */
class AirtableSalesforceAPI {
    constructor(auth) {
        this.auth = auth;
        this.logger = new AirtableSalesforceLogger(SCRIPT_NAME, SCRIPT_VERSION);
    }

    /**
     * Query Salesforce records with SOQL
     * Returns data formatted for Airtable consumption
     */
    async query(soql) {
        try {
            this.logger.logSoqlQuery(soql);

            const startTime = Date.now();
            const response = await this.auth.makeAuthenticatedRequest(`query/?q=${encodeURIComponent(soql)}`);
            const duration = Date.now() - startTime;

            this.logger.logSoqlQueryResult(soql, response.records?.length || 0, duration);

            // Format for Airtable - flatten nested objects
            const airtableRecords = response.records?.map(record => this._formatForAirtable(record)) || [];

            return {
                success: true,
                records: airtableRecords,
                totalSize: response.totalSize,
                done: response.done
            };

        } catch (error) {
            this.logger.logError(`SOQL query failed: ${error.message}`);
            return {
                success: false,
                error: error.message,
                records: []
            };
        }
    }

    /**
     * Create Salesforce record from Airtable data
     * Handles field mapping and validation
     */
    async createRecord(objectType, airtableRecord, fieldMapping = {}) {
        try {
            this.logger.logDmlOperation("CREATE", objectType, 1);

            const salesforceData = this._mapAirtableToSalesforce(airtableRecord, fieldMapping);

            const response = await this.auth.makeAuthenticatedRequest(`sobjects/${objectType}/`, {
                method: "POST",
                body: JSON.stringify(salesforceData)
            });

            if (response.success) {
                this.logger.logSuccess(`Created ${objectType} record: ${response.id}`);
                return {
                    success: true,
                    id: response.id,
                    salesforceRecord: salesforceData
                };
            } else {
                this.logger.logError(`Create ${objectType} failed: ${JSON.stringify(response.errors)}`);
                return {
                    success: false,
                    errors: response.errors
                };
            }

        } catch (error) {
            this.logger.logError(`Create ${objectType} error: ${error.message}`);
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Update Salesforce record from Airtable data
     * Supports partial updates with change tracking
     */
    async updateRecord(objectType, recordId, airtableRecord, fieldMapping = {}) {
        try {
            this.logger.logDmlOperation("UPDATE", objectType, 1);

            const salesforceData = this._mapAirtableToSalesforce(airtableRecord, fieldMapping);

            const response = await this.auth.makeAuthenticatedRequest(`sobjects/${objectType}/${recordId}`, {
                method: "PATCH",
                body: JSON.stringify(salesforceData)
            });

            // Salesforce PATCH returns 204 No Content on success
            this.logger.logSuccess(`Updated ${objectType} record: ${recordId}`);
            return {
                success: true,
                id: recordId,
                salesforceRecord: salesforceData
            };

        } catch (error) {
            this.logger.logError(`Update ${objectType} error: ${error.message}`);
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Bulk operations for Airtable batch processing
     * Handles large datasets efficiently
     */
    async bulkOperation(operation, objectType, airtableRecords, fieldMapping = {}) {
        const batchSize = 200; // Salesforce API limit
        const results = [];

        this.logger.logDmlOperation(operation.toUpperCase(), objectType, airtableRecords.length);

        for (let i = 0; i < airtableRecords.length; i += batchSize) {
            const batch = airtableRecords.slice(i, i + batchSize);
            const batchResults = await this._processBatch(operation, objectType, batch, fieldMapping);
            results.push(...batchResults);

            // Progress indicator for Airtable UI
            const progress = Math.min(i + batchSize, airtableRecords.length);
            this.logger.logInfo(`Processed ${progress}/${airtableRecords.length} records`);
        }

        const successCount = results.filter(r => r.success).length;
        const errorCount = results.length - successCount;

        this.logger.logDmlOperationResult(operation.toUpperCase(), objectType, results.length, successCount, errorCount);

        return {
            success: errorCount === 0,
            totalProcessed: results.length,
            successCount,
            errorCount,
            results
        };
    }

    /**
     * Map Airtable field names to Salesforce field names
     * Handles data type conversion and validation
     */
    _mapAirtableToSalesforce(airtableRecord, fieldMapping) {
        const salesforceData = {};

        for (const [airtableField, salesforceField] of Object.entries(fieldMapping)) {
            if (airtableRecord[airtableField] !== undefined) {
                let value = airtableRecord[airtableField];

                // Handle Airtable-specific data types
                if (Array.isArray(value)) {
                    // Convert Airtable multi-select to Salesforce picklist
                    value = value.join(';');
                } else if (value instanceof Date) {
                    // Convert Airtable date to Salesforce ISO format
                    value = value.toISOString();
                } else if (typeof value === 'object' && value.url) {
                    // Handle Airtable attachment URLs
                    value = value.url;
                }

                salesforceData[salesforceField] = value;
            }
        }

        return salesforceData;
    }

    /**
     * Format Salesforce record for Airtable display
     * Handles nested objects and data type conversion
     */
    _formatForAirtable(salesforceRecord) {
        const airtableRecord = {};

        for (const [key, value] of Object.entries(salesforceRecord)) {
            if (key === 'attributes') {
                // Skip Salesforce metadata
                continue;
            }

            if (typeof value === 'object' && value !== null) {
                // Flatten relationship fields (e.g., Account.Name)
                for (const [subKey, subValue] of Object.entries(value)) {
                    if (subKey !== 'attributes') {
                        airtableRecord[`${key}.${subKey}`] = subValue;
                    }
                }
            } else {
                airtableRecord[key] = value;
            }
        }

        return airtableRecord;
    }
}
```

#### Airtable Salesforce Logging Standards

**Enhanced Logging for Airtable Automations:**
```javascript
/**
 * Specialized logger for Airtable-Salesforce operations
 * Optimized for Airtable automation console output
 */
class AirtableSalesforceLogger {
    constructor(scriptName, version, orgId = null) {
        this.scriptName = scriptName;
        this.version = version;
        this.orgId = orgId;
        this.requestId = `at_sf_${Date.now()}`;
        this.startTime = new Date();
    }

    logStart(message = null) {
        const versionInfo = `${this.scriptName} v${this.version}`;
        const defaultMessage = `${versionInfo} starting... [${this.requestId}]`;
        console.log(`🚀 ${message || defaultMessage}`);
    }

    logSuccess(message) {
        console.log(`✅ ${message} [${this.requestId}]`);
    }

    logError(message) {
        console.log(`❌ ${message} [${this.requestId}]`);
    }

    logWarning(message) {
        console.log(`⚠️ ${message} [${this.requestId}]`);
    }

    logInfo(message) {
        console.log(`ℹ️ ${message} [${this.requestId}]`);
    }

    // Airtable-specific: Log SOQL queries with Airtable context
    logSoqlQuery(query, airtableContext = null) {
        console.log(`🔍 SOQL QUERY [${this.requestId}]`);
        console.log(`   Query: ${query}`);
        if (airtableContext) {
            console.log(`   Airtable Context: ${JSON.stringify(airtableContext)}`);
        }
    }

    logSoqlQueryResult(query, recordCount, durationMs) {
        console.log(`🔍 SOQL RESULT [${this.requestId}]`);
        console.log(`   Records: ${recordCount}`);
        console.log(`   Duration: ${durationMs}ms`);
    }

    // Airtable-specific: Log DML operations with progress
    logDmlOperation(operation, objectType, recordCount) {
        console.log(`📝 ${operation} OPERATION [${this.requestId}]`);
        console.log(`   Object: ${objectType}`);
        console.log(`   Records: ${recordCount}`);
    }

    logDmlOperationResult(operation, objectType, totalCount, successCount, errorCount) {
        console.log(`📝 ${operation} COMPLETE [${this.requestId}]`);
        console.log(`   Object: ${objectType}`);
        console.log(`   Total: ${totalCount}`);
        console.log(`   Success: ${successCount}`);
        console.log(`   Errors: ${errorCount}`);
        console.log(`   Success Rate: ${((successCount / totalCount) * 100).toFixed(1)}%`);
    }

    // REQUIRED: Log ALL API requests with Airtable context
    logApiRequest(apiName, method, url, headers, body, airtableContext = null) {
        const timestamp = new Date().toISOString();
        console.log(`🌐 API REQUEST [${this.requestId}] ${timestamp}`);
        console.log(`   API: ${apiName}`);
        console.log(`   Method: ${method}`);
        console.log(`   URL: ${url}`);

        // Sanitize headers for Airtable console
        const sanitizedHeaders = this._sanitizeHeaders(headers);
        console.log(`   Headers: ${JSON.stringify(sanitizedHeaders, null, 2)}`);

        if (body) {
            const sanitizedBody = this._sanitizeBody(body);
            console.log(`   Body: ${JSON.stringify(sanitizedBody, null, 2)}`);
        }

        if (airtableContext) {
            console.log(`   Airtable Context: ${JSON.stringify(airtableContext, null, 2)}`);
        }
    }

    // REQUIRED: Log ALL API responses with duration
    logApiResponse(apiName, statusCode, headers, responseData, duration) {
        const timestamp = new Date().toISOString();
        console.log(`🌐 API RESPONSE [${this.requestId}] ${timestamp}`);
        console.log(`   API: ${apiName}`);
        console.log(`   Status: ${statusCode}`);
        console.log(`   Duration: ${duration}ms`);

        if (responseData) {
            const sanitizedResponse = this._sanitizeResponse(responseData);
            const responseStr = JSON.stringify(sanitizedResponse, null, 2);

            // Truncate large responses for Airtable console
            if (responseStr.length > 2000) {
                console.log(`   Response: ${responseStr.substring(0, 2000)}... [TRUNCATED - ${responseStr.length} chars total]`);
            } else {
                console.log(`   Response: ${responseStr}`);
            }
        }
    }

    logApiError(apiName, error, requestContext) {
        const timestamp = new Date().toISOString();
        console.log(`❌ API ERROR [${this.requestId}] ${timestamp}`);
        console.log(`   API: ${apiName}`);
        console.log(`   Error: ${error.message}`);
        console.log(`   Status: ${error.status || 'Unknown'}`);

        if (error.data) {
            console.log(`   Error Data: ${JSON.stringify(error.data, null, 2)}`);
        }

        if (requestContext) {
            console.log(`   Request Context: ${JSON.stringify(requestContext, null, 2)}`);
        }
    }

    _sanitizeHeaders(headers) {
        const sanitized = { ...headers };
        if (sanitized.Authorization) {
            sanitized.Authorization = 'Bearer [REDACTED]';
        }
        return sanitized;
    }

    _sanitizeBody(body) {
        try {
            const parsed = typeof body === 'string' ? JSON.parse(body) : body;
            // Remove sensitive fields but preserve structure
            return this._recursiveSanitize(parsed);
        } catch {
            return '[Unable to parse body]';
        }
    }

    _sanitizeResponse(data) {
        return this._recursiveSanitize(data);
    }

    _recursiveSanitize(obj) {
        if (typeof obj !== 'object' || obj === null) {
            return obj;
        }

        const sanitized = Array.isArray(obj) ? [] : {};
        const sensitiveFields = ['access_token', 'refresh_token', 'password', 'security_token'];

        for (const [key, value] of Object.entries(obj)) {
            if (sensitiveFields.some(field => key.toLowerCase().includes(field))) {
                sanitized[key] = '[REDACTED]';
            } else if (typeof value === 'object' && value !== null) {
                sanitized[key] = this._recursiveSanitize(value);
            } else {
                sanitized[key] = value;
            }
        }

        return sanitized;
    }
}
```

---

## Salesforce Security Best Practices

### Authentication Security
```python
# MANDATORY: Never store credentials in code
# Use configuration files with restricted permissions
import os
import stat

def secure_config_check(config_path: str):
    """Verify configuration file has secure permissions"""
    if os.path.exists(config_path):
        file_stat = os.stat(config_path)
        file_permissions = stat.filemode(file_stat.st_mode)

        # Check if file is readable by others
        if file_stat.st_mode & stat.S_IROTH:
            raise SecurityError(f"Config file {config_path} is readable by others. Fix with: chmod 600 {config_path}")
```

### Data Protection Patterns
```python
# MANDATORY: Sanitize sensitive data in logs
class SalesforceDataSanitizer:
    SENSITIVE_FIELDS = [
        'SSN__c', 'CreditCard__c', 'BankAccount__c',
        'PersonEmail', 'Phone', 'PersonMobilePhone'
    ]

    @staticmethod
    def sanitize_record(record: dict) -> dict:
        """Remove or mask sensitive data from records"""
        sanitized = record.copy()
        for field in SalesforceDataSanitizer.SENSITIVE_FIELDS:
            if field in sanitized:
                if sanitized[field]:
                    # Mask sensitive data but preserve format
                    sanitized[field] = SalesforceDataSanitizer._mask_value(sanitized[field])
        return sanitized

    @staticmethod
    def _mask_value(value: str) -> str:
        """Mask sensitive values while preserving length/format"""
        if len(value) <= 4:
            return '*' * len(value)
        return value[:2] + '*' * (len(value) - 4) + value[-2:]
```

---

## Testing Framework for Salesforce Tools

### Configuration Validation
```python
# utility/testing/test_salesforce_config.py
import pytest
from configparser import ConfigParser

def test_salesforce_config_complete():
    """Test that all required Salesforce configuration is present"""
    config = ConfigParser()
    config.read('account_tools/config.ini')

    required_fields = ['username', 'password', 'security_token', 'consumer_key', 'consumer_secret']

    assert 'salesforce' in config.sections()

    for field in required_fields:
        assert field in config['salesforce']
        assert config['salesforce'][field].strip() != ''

def test_connected_app_config():
    """Test Connected App configuration validity"""
    config = ConfigParser()
    config.read('account_tools/config.ini')

    consumer_key = config['salesforce']['consumer_key']
    consumer_secret = config['salesforce']['consumer_secret']

    # Consumer Key should be 85+ characters for Connected Apps
    assert len(consumer_key) >= 85
    # Consumer Secret should be 64+ characters
    assert len(consumer_secret) >= 64
```

### API Limit Testing
```python
# utility/testing/test_rate_limits.py
def test_api_limits_monitoring():
    """Test API limit monitoring and alerting"""
    manager = SalesforceAccountManager('account_tools/config.ini')

    # Get current API limits
    limits = manager.sf.limits()

    # Check critical limits
    daily_api_requests = limits['DailyApiRequests']
    remaining = daily_api_requests['Remaining']
    max_requests = daily_api_requests['Max']

    usage_percentage = ((max_requests - remaining) / max_requests) * 100

    # Alert if usage > 80%
    if usage_percentage > 80:
        logger.warning(f"API usage at {usage_percentage:.1f}% - consider throttling")

    assert remaining > 0, "Daily API limit exceeded"
```

---

## Common Salesforce Operations

### Account Management Patterns
```python
# Standard account creation with validation
def create_account_with_validation(self, account_data: dict) -> str:
    """Create account with business rule validation"""

    # Pre-validation
    if not account_data.get('Name'):
        raise ValueError("Account Name is required")

    # Check for duplicates
    existing = self.sf.query(f"SELECT Id FROM Account WHERE Name = '{account_data['Name']}'")
    if existing['records']:
        raise ValueError(f"Account with name '{account_data['Name']}' already exists")

    # Create with error handling
    try:
        result = self.sf.Account.create(account_data)
        self.logger.info(f"Created account: {result['id']}")
        return result['id']
    except SalesforceError as e:
        self.logger.error(f"Account creation failed: {e}")
        raise
```

### Bulk Operations Pattern
```python
# Bulk operations with progress tracking
def bulk_update_accounts(self, updates: list) -> dict:
    """Update multiple accounts with progress tracking"""

    results = {'success': 0, 'errors': 0, 'details': []}

    # Use Bulk API for large datasets
    if len(updates) > 200:
        return self._bulk_api_update(updates)

    # Process in batches for smaller datasets
    batch_size = 50
    for i in range(0, len(updates), batch_size):
        batch = updates[i:i + batch_size]

        try:
            batch_results = self.sf.bulk.Account.update(batch)
            for result in batch_results:
                if result['success']:
                    results['success'] += 1
                else:
                    results['errors'] += 1
                    results['details'].append(result['errors'])

        except Exception as e:
            self.logger.error(f"Batch update error: {e}")
            results['errors'] += len(batch)

    return results
```

---

## Troubleshooting Salesforce Issues

### Authentication Problems
```bash
# Test basic authentication
python -c "
from account_tools.sf_account_manager import SalesforceAccountManager
manager = SalesforceAccountManager('account_tools/config.ini', verbose=True)
success = manager.authenticate()
print(f'Authentication: {\"SUCCESS\" if success else \"FAILED\"}')
if success:
    print(f'Org ID: {manager.session_info[\"org_id\"]}')
    print(f'Instance: {manager.session_info[\"server_url\"]}')
"

# Verify Connected App settings
python utility/testing/verify_connected_app.py

# Check security token validity
python utility/testing/test_security_token.py
```

### API Limit Monitoring
```python
# Monitor API usage patterns
def monitor_api_usage(manager):
    """Monitor and report API usage"""
    limits = manager.sf.limits()

    critical_limits = ['DailyApiRequests', 'HourlyTimeBasedWorkflow', 'DailyBulkApiRequests']

    for limit_name in critical_limits:
        if limit_name in limits:
            limit_info = limits[limit_name]
            remaining = limit_info['Remaining']
            max_limit = limit_info['Max']
            usage_pct = ((max_limit - remaining) / max_limit) * 100

            print(f"{limit_name}: {remaining}/{max_limit} ({usage_pct:.1f}% used)")

            if usage_pct > 90:
                print(f"WARNING: {limit_name} usage critically high!")
```

---

## Deployment Guide for Salesforce Tools

### Connected App Setup
1. **Create Connected App in Salesforce Setup**
   - App Name: "EMG Salesforce API Tools"
   - Enable OAuth Settings: ✓
   - Callback URL: `http://localhost:8080/callback`
   - Selected OAuth Scopes:
     - Access and manage your data (api)
     - Perform requests at any time (refresh_token, offline_access)
     - Access unique user identifiers (openid)

2. **Configure Security Settings**
   - IP Relaxation: "Relax IP restrictions"
   - Refresh Token Policy: "Refresh token is valid until revoked"

3. **Permission Sets**
   - Create permission set: "API Integration User"
   - Object Settings: Account (Read, Create, Edit, Delete)
   - System Permissions: API Enabled, Bulk API Hard Delete

### Production Deployment Checklist
- [ ] Connected App configured with production callback URLs
- [ ] Security token generated for production user
- [ ] Configuration files secured (chmod 600)
- [ ] API limits monitored and alerting configured
- [ ] Error logging configured for production environment
- [ ] Backup and recovery procedures documented
- [ ] User permissions and profile settings verified

---

## Success Metrics for Salesforce API Tools

### sf_account_manager.py v1.0.0
- ✅ **Complete CRUD Operations** (Create, Read, Update, Delete)
- ✅ **Automatic Pagination** (handles 2000+ record limits)
- ✅ **Advanced Filtering** (SOQL WHERE clause support)
- ✅ **Export Capabilities** (pipe-delimited format)
- ✅ **Error Handling** (comprehensive exception management)

### Authentication Framework
- ✅ **Multiple Auth Methods** (Username/Password, Connected App)
- ✅ **Session Management** (automatic token refresh)
- ✅ **Security Best Practices** (credential protection)

### API Integration
- ✅ **Rate Limit Compliance** (automatic throttling)
- ✅ **Bulk Operations** (efficient large dataset handling)
- ✅ **Comprehensive Logging** (request/response tracking)

---

## CLAUDE.md Version History

### v2.0.0 (2024-09-17) - Complete Salesforce API optimization
- Replaced Creative Automation project structure with Salesforce-specific layout
- Added comprehensive Salesforce authentication patterns and security practices
- Added Salesforce API logging standards with SOQL/DML operation tracking
- Added testing framework for Salesforce configurations and API limits
- Added deployment guide for Connected Apps and production environments
- Added troubleshooting section for common Salesforce API issues
- Why: Optimize CLAUDE.md specifically for Salesforce API development and tools

---

*Last Updated: 2024-09-17*
*Claude Configuration Version: 2.0.0*
*Optimized for: Salesforce API Development*