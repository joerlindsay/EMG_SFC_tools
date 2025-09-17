# Salesforce Account Tools Extension Plan
## Comprehensive Data Element Coverage for Evolution Media Group

---

## Executive Summary

This document outlines a comprehensive plan to extend the existing Salesforce Account tools to support all available data elements in Evolution Media Group's Salesforce Account object. The plan addresses standard fields, custom fields, validation rules, relationships, and metadata management to create a complete Account data management solution.

**Current State:** Basic field coverage (10 fields)
**Target State:** Complete field coverage (150+ fields estimated)
**Timeline:** 6-8 weeks
**Priority:** High - Critical for business operations

---

## 1. Current State Analysis

### 1.1 Currently Supported Fields

**Standard Fields (7):**
- Id (Salesforce Record ID)
- Name (Account Name)
- Type (Customer/Prospect)
- Industry
- Phone
- BillingCity
- BillingState

**Custom Fields (2):**
- Website
- Domain__c

**Total Coverage:** ~6% of available fields

### 1.2 Discovered Custom Fields (Via Validation Errors)

**Required Custom Fields:**
- Credit_Terms__c (Picklist - Required)
- Short_Name__c (Text - Required)
- Primary_Advertiser_ID__c (Text - Required for Customer type)
- Platform_Default_Tracking_ID__c (Text - Required for Customer type)

**Validation Rules Discovered:**
- Cannot set Type="Customer" if Closed Opportunity Count < 1
- Credit Terms must be selected
- Primary Advertiser ID required for Customer accounts
- Short Name is mandatory
- Platform Default Tracking ID required for Customer accounts

### 1.3 Known Data Volumes
- 20,378 Dealership records
- 2,000+ general Account records
- RecordTypes in use: Dealership, Client, Customer, Prospect

---

## 2. Comprehensive Field Discovery Plan

### 2.1 Metadata Discovery Tool

**New Tool: `sf_account_metadata_analyzer.py`**

```python
class AccountMetadataAnalyzer:
    """
    Discovers and documents all Account object fields and metadata
    """

    def discover_all_fields(self):
        """Use Salesforce describe API to get all field metadata"""
        # GET /services/data/vXX.0/sobjects/Account/describe
        return {
            'standard_fields': [],
            'custom_fields': [],
            'system_fields': [],
            'formula_fields': [],
            'lookup_relationships': [],
            'master_detail_relationships': []
        }

    def analyze_field_properties(self, field):
        """Extract field properties for documentation"""
        return {
            'api_name': field['name'],
            'label': field['label'],
            'type': field['type'],
            'length': field['length'],
            'precision': field['precision'],
            'required': field['required'],
            'unique': field['unique'],
            'updateable': field['updateable'],
            'createable': field['createable'],
            'picklist_values': field['picklistValues'],
            'default_value': field['defaultValue'],
            'reference_to': field['referenceTo']
        }

    def discover_validation_rules(self):
        """Query validation rules via Tooling API"""
        # Query ValidationRule object
        pass

    def discover_record_types(self):
        """Get all RecordTypes for Account"""
        # Query RecordType object
        pass

    def generate_field_documentation(self):
        """Create comprehensive field documentation"""
        pass
```

### 2.2 Expected Field Categories

**Standard Salesforce Account Fields (~50):**
- Basic Information (Name, Type, Industry, etc.)
- Address Fields (Billing, Shipping)
- Contact Information (Phone, Fax, Website)
- Ownership & Classification (Owner, Parent Account)
- Financial Information (Annual Revenue, Number of Employees)
- System Fields (Created Date, Last Modified)

**Evolution Media Group Custom Fields (~100+ expected):**
- Advertising/Marketing Fields
  - Primary_Advertiser_ID__c
  - Platform_Default_Tracking_ID__c
  - Campaign_Attribution__c

- Financial/Credit Fields
  - Credit_Terms__c
  - Credit_Limit__c
  - Payment_Terms__c

- Automotive Industry Fields (for Dealerships)
  - Dealership_Group__c
  - OEM_Brands__c
  - Service_Territory__c

- Media/Platform Fields
  - Media_Platforms__c
  - Active_Campaigns_Count__c
  - Total_Spend_YTD__c

---

## 3. Enhanced Data Model Design

### 3.1 Field Management Architecture

```python
class FieldDefinition:
    """Represents a Salesforce field with full metadata"""

    def __init__(self, api_name, metadata):
        self.api_name = api_name
        self.label = metadata['label']
        self.field_type = metadata['type']
        self.required = metadata['required']
        self.validation_rules = []
        self.dependencies = []

    def validate(self, value):
        """Validate value against field constraints"""
        pass

    def transform(self, value, direction='to_salesforce'):
        """Transform value for Salesforce compatibility"""
        pass
```

### 3.2 Field Registry Pattern

```python
class AccountFieldRegistry:
    """Central registry of all Account fields"""

    # Standard Fields
    STANDARD_FIELDS = {
        'Name': FieldDefinition('Name', {...}),
        'Type': FieldDefinition('Type', {...}),
        'Industry': FieldDefinition('Industry', {...}),
        # ... 50+ standard fields
    }

    # Custom Fields
    CUSTOM_FIELDS = {
        'Credit_Terms__c': FieldDefinition('Credit_Terms__c', {
            'type': 'Picklist',
            'required': True,
            'values': ['Net 30', 'Net 60', 'Net 90', 'Prepay']
        }),
        'Short_Name__c': FieldDefinition('Short_Name__c', {
            'type': 'Text',
            'required': True,
            'length': 50
        }),
        # ... 100+ custom fields
    }

    # Relationship Fields
    RELATIONSHIP_FIELDS = {
        'ParentId': FieldDefinition('ParentId', {
            'type': 'Lookup',
            'referenceTo': 'Account'
        }),
        'OwnerId': FieldDefinition('OwnerId', {
            'type': 'Lookup',
            'referenceTo': 'User'
        })
    }
```

### 3.3 Validation Engine

```python
class AccountValidationEngine:
    """Comprehensive validation for Account data"""

    def __init__(self, field_registry):
        self.field_registry = field_registry
        self.validation_rules = []

    def validate_required_fields(self, account_data):
        """Check all required fields are present"""
        pass

    def validate_field_types(self, account_data):
        """Ensure field values match expected types"""
        pass

    def validate_business_rules(self, account_data):
        """Apply Evolution Media Group specific rules"""
        rules = [
            CustomerTypeRule(),  # Can't be Customer without closed opps
            CreditTermsRule(),   # Credit terms required
            AdvertiserIDRule(),  # Advertiser ID for customers
            DealershipRule()     # Special rules for dealerships
        ]
        pass

    def validate_relationships(self, account_data):
        """Validate lookup relationships exist"""
        pass
```

---

## 4. Implementation Phases

### Phase 1: Metadata Discovery (Week 1-2)

**Deliverables:**
1. **sf_account_metadata_analyzer.py** - Tool to discover all fields
2. **account_fields_catalog.json** - Complete field documentation
3. **validation_rules_catalog.json** - All validation rules
4. **record_types_catalog.json** - RecordType definitions

**Tasks:**
```python
# 1. Create metadata analyzer
analyzer = AccountMetadataAnalyzer(config)
analyzer.authenticate()

# 2. Discover all fields
all_fields = analyzer.discover_all_fields()

# 3. Document field properties
field_catalog = analyzer.generate_field_documentation()

# 4. Export to JSON
with open('account_fields_catalog.json', 'w') as f:
    json.dump(field_catalog, f, indent=2)
```

### Phase 2: Field Registry Implementation (Week 2-3)

**Deliverables:**
1. **field_definitions.py** - FieldDefinition classes
2. **account_field_registry.py** - Complete field registry
3. **field_transformers.py** - Data type transformations
4. **field_validators.py** - Field-level validation

**Structure:**
```
utility/salesforce_base/
├── field_definitions.py
├── account_field_registry.py
├── field_transformers.py
├── field_validators.py
└── validation_rules/
    ├── customer_type_rule.py
    ├── credit_terms_rule.py
    └── dealership_rule.py
```

### Phase 3: Enhanced Account Manager (Week 3-4)

**Upgrade sf_account_manager.py:**

```python
class EnhancedSalesforceAccountManager(SalesforceAccountManager):
    """Extended Account manager with full field support"""

    def __init__(self, config_path=None):
        super().__init__(config_path)
        self.field_registry = AccountFieldRegistry()
        self.validation_engine = AccountValidationEngine(self.field_registry)
        self.load_field_metadata()

    def create_account_full(self, account_data):
        """Create account with all fields"""
        # Validate all fields
        validation_result = self.validation_engine.validate(account_data)
        if not validation_result.is_valid:
            return validation_result.errors

        # Transform data for Salesforce
        sf_data = self.transform_to_salesforce(account_data)

        # Create with full field set
        return self.sf.Account.create(sf_data)

    def get_account_full(self, account_id):
        """Retrieve account with all fields"""
        fields = self.field_registry.get_all_field_names()
        soql = f"SELECT {','.join(fields)} FROM Account WHERE Id = '{account_id}'"
        return self.sf.query(soql)

    def update_account_selective(self, account_id, updates):
        """Update only specified fields"""
        # Validate only updated fields
        validation_result = self.validation_engine.validate_partial(updates)
        if not validation_result.is_valid:
            return validation_result.errors

        # Apply updates
        return self.sf.Account.update(account_id, updates)
```

### Phase 4: Bulk Operations Support (Week 4-5)

**New Tool: `sf_account_bulk_manager.py`**

```python
class AccountBulkManager:
    """Handles large-scale Account operations"""

    def __init__(self, config):
        self.sf = Salesforce(**config)
        self.bulk_api = self.sf.bulk

    def bulk_create_accounts(self, accounts_data, batch_size=10000):
        """Create thousands of accounts efficiently"""
        job = self.bulk_api.Account.insert(accounts_data, batch_size=batch_size)
        return self.monitor_job(job)

    def bulk_update_accounts(self, updates_data, batch_size=10000):
        """Update thousands of accounts efficiently"""
        job = self.bulk_api.Account.update(updates_data, batch_size=batch_size)
        return self.monitor_job(job)

    def bulk_upsert_accounts(self, upsert_data, external_id='External_ID__c'):
        """Upsert based on external ID"""
        job = self.bulk_api.Account.upsert(upsert_data, external_id)
        return self.monitor_job(job)

    def export_all_accounts(self, output_format='csv'):
        """Export all accounts with all fields"""
        fields = AccountFieldRegistry.get_all_field_names()
        soql = f"SELECT {','.join(fields)} FROM Account"

        # Use Bulk API for large exports
        job = self.bulk_api.query(soql)
        return self.download_results(job, output_format)
```

### Phase 5: Data Migration Tools (Week 5-6)

**New Tool: `sf_account_migrator.py`**

```python
class AccountDataMigrator:
    """Migrate account data between environments"""

    def __init__(self, source_config, target_config):
        self.source_sf = Salesforce(**source_config)
        self.target_sf = Salesforce(**target_config)
        self.field_mapper = FieldMapper()

    def migrate_accounts(self, filter_criteria=None):
        """Migrate accounts from source to target"""
        # 1. Extract from source
        accounts = self.extract_accounts(filter_criteria)

        # 2. Transform for target
        transformed = self.transform_accounts(accounts)

        # 3. Load to target
        results = self.load_accounts(transformed)

        return results

    def map_record_types(self):
        """Map RecordTypes between environments"""
        pass

    def map_users(self):
        """Map Owner IDs between environments"""
        pass

    def preserve_relationships(self):
        """Maintain parent-child relationships"""
        pass
```

### Phase 6: Testing & Validation (Week 6-7)

**Test Suite Structure:**
```
utility/testing/
├── test_field_discovery.py
├── test_field_validation.py
├── test_bulk_operations.py
├── test_data_migration.py
├── test_validation_rules.py
├── fixtures/
│   ├── sample_accounts.json
│   ├── validation_test_cases.json
│   └── bulk_test_data.csv
└── integration/
    ├── test_production_fields.py
    └── test_sandbox_migration.py
```

**Test Coverage Requirements:**
- All standard fields read/write
- All custom fields read/write
- Validation rules enforcement
- Bulk operations (10K+ records)
- Data type transformations
- Relationship preservation
- Error handling

### Phase 7: Documentation & Training (Week 7-8)

**Documentation Deliverables:**
1. **Field Catalog** - Complete field reference
2. **Validation Rules Guide** - Business rule documentation
3. **API Usage Guide** - Developer documentation
4. **Migration Playbook** - Step-by-step migration guide
5. **Best Practices** - Performance and security guidelines

---

## 5. Technical Implementation Details

### 5.1 Field Type Handlers

```python
class FieldTypeHandlers:
    """Type-specific field handling"""

    @staticmethod
    def handle_picklist(field, value):
        """Validate and transform picklist values"""
        valid_values = field.metadata['picklistValues']
        if value not in valid_values:
            raise ValueError(f"Invalid picklist value: {value}")
        return value

    @staticmethod
    def handle_multipicklist(field, values):
        """Handle multi-select picklists"""
        if isinstance(values, list):
            return ';'.join(values)
        return values

    @staticmethod
    def handle_date(field, value):
        """Format dates for Salesforce"""
        if isinstance(value, datetime):
            return value.strftime('%Y-%m-%d')
        return value

    @staticmethod
    def handle_datetime(field, value):
        """Format datetime for Salesforce"""
        if isinstance(value, datetime):
            return value.isoformat()
        return value

    @staticmethod
    def handle_currency(field, value):
        """Handle currency fields with precision"""
        if field.metadata['precision']:
            return round(float(value), field.metadata['precision'])
        return float(value)

    @staticmethod
    def handle_reference(field, value):
        """Validate lookup relationships"""
        # Verify referenced record exists
        reference_object = field.metadata['referenceTo'][0]
        # Query to validate
        return value
```

### 5.2 Performance Optimizations

```python
class PerformanceOptimizer:
    """Optimize Salesforce API usage"""

    def __init__(self):
        self.query_cache = {}
        self.field_cache = {}
        self.batch_queue = []

    def optimize_soql_query(self, fields, conditions):
        """Build optimized SOQL queries"""
        # Select only needed fields
        # Use indexed fields in WHERE clause
        # Limit results when possible
        pass

    def batch_api_calls(self, operations):
        """Batch multiple operations"""
        # Group similar operations
        # Use composite API for mixed operations
        # Respect API limits
        pass

    def implement_caching(self):
        """Cache frequently accessed data"""
        # Cache field metadata
        # Cache picklist values
        # Cache record types
        pass
```

### 5.3 Error Recovery

```python
class ErrorRecoveryManager:
    """Handle and recover from errors"""

    def __init__(self):
        self.error_log = []
        self.retry_queue = []

    def handle_validation_error(self, error, record):
        """Process validation errors"""
        # Log detailed error
        # Attempt auto-correction
        # Queue for manual review
        pass

    def handle_api_limit_error(self, error):
        """Handle rate limiting"""
        # Implement exponential backoff
        # Queue for retry
        # Alert if persistent
        pass

    def generate_error_report(self):
        """Create detailed error report"""
        # Categorize errors
        # Provide resolution steps
        # Export for review
        pass
```

---

## 6. Security Considerations

### 6.1 Field-Level Security
```python
class FieldLevelSecurity:
    """Enforce field-level security"""

    def check_field_access(self, field_name, operation='read'):
        """Verify user has field access"""
        # Check field-level security
        # Check profile permissions
        # Check permission sets
        pass

    def filter_fields_by_access(self, fields, user_profile):
        """Filter fields based on user access"""
        # Remove inaccessible fields
        # Handle encrypted fields
        # Apply data masking
        pass
```

### 6.2 Data Privacy
```python
class DataPrivacyManager:
    """Handle sensitive data"""

    SENSITIVE_FIELDS = [
        'SSN__c',
        'Tax_ID__c',
        'Bank_Account__c'
    ]

    def mask_sensitive_data(self, record):
        """Mask sensitive fields in logs/exports"""
        pass

    def encrypt_at_rest(self, data):
        """Encrypt sensitive data storage"""
        pass

    def audit_data_access(self, user, fields, operation):
        """Log data access for compliance"""
        pass
```

---

## 7. Integration Patterns

### 7.1 Airtable Integration
```javascript
// Airtable script for full Account sync
class AccountFullSync {
    constructor(salesforceAuth) {
        this.sf = salesforceAuth;
        this.fieldMappings = loadFieldMappings();
    }

    async syncAllFields(airtableRecord) {
        // Map all Airtable fields to Salesforce
        const sfData = this.mapToSalesforce(airtableRecord);

        // Validate against field registry
        const validation = await this.validateFields(sfData);

        // Sync to Salesforce
        if (validation.success) {
            return await this.sf.Account.upsert(sfData);
        }
    }
}
```

### 7.2 ETL Pipeline
```python
class AccountETLPipeline:
    """ETL pipeline for Account data"""

    def extract_from_source(self, source_system):
        """Extract account data from source"""
        pass

    def transform_to_salesforce(self, source_data):
        """Transform to Salesforce format"""
        # Map fields
        # Apply business rules
        # Validate data
        pass

    def load_to_salesforce(self, transformed_data):
        """Load data to Salesforce"""
        # Use Bulk API for large datasets
        # Handle errors
        # Report results
        pass
```

---

## 8. Success Metrics

### 8.1 Coverage Metrics
- **Field Coverage:** From 10 fields → 150+ fields (1500% increase)
- **Custom Field Support:** 0 → 100+ custom fields
- **Validation Rules:** 0 → 20+ business rules implemented
- **RecordType Support:** Basic → Full RecordType handling

### 8.2 Performance Metrics
- **Bulk Operations:** Support 50,000+ records per operation
- **API Efficiency:** Reduce API calls by 60% through optimization
- **Processing Speed:** 10x improvement for large datasets
- **Error Rate:** < 0.1% for validated data

### 8.3 Business Impact
- **Data Completeness:** 100% field coverage for business needs
- **Automation:** 80% reduction in manual data entry
- **Accuracy:** 99.9% data accuracy through validation
- **Compliance:** Full audit trail and data governance

---

## 9. Risk Mitigation

### 9.1 Technical Risks
| Risk | Mitigation |
|------|------------|
| API Limits | Implement caching, batching, and Bulk API |
| Data Loss | Comprehensive backup before operations |
| Field Changes | Dynamic field discovery, not hardcoded |
| Performance | Async processing, queue management |

### 9.2 Business Risks
| Risk | Mitigation |
|------|------------|
| Data Quality | Validation engine with business rules |
| Compliance | Audit logging, field-level security |
| User Adoption | Comprehensive documentation and training |
| Integration Failures | Retry logic, error recovery |

---

## 10. Timeline & Milestones

### Development Schedule

**Week 1-2: Discovery Phase**
- [ ] Deploy metadata analyzer
- [ ] Document all fields
- [ ] Catalog validation rules
- [ ] Map relationships

**Week 3-4: Core Development**
- [ ] Build field registry
- [ ] Implement validation engine
- [ ] Enhance account manager
- [ ] Create transformers

**Week 5-6: Advanced Features**
- [ ] Bulk operations
- [ ] Data migration tools
- [ ] Performance optimization
- [ ] Error recovery

**Week 7-8: Testing & Deployment**
- [ ] Unit testing
- [ ] Integration testing
- [ ] Documentation
- [ ] Production deployment

### Key Milestones
1. **Milestone 1** (Week 2): Complete field catalog delivered
2. **Milestone 2** (Week 4): Enhanced account manager operational
3. **Milestone 3** (Week 6): Bulk operations tested
4. **Milestone 4** (Week 8): Production deployment complete

---

## 11. Resource Requirements

### 11.1 Technical Resources
- **Development Environment:** Python 3.8+, Node.js 14+
- **Salesforce Access:** Full API access, System Administrator profile
- **Testing Environment:** Salesforce Sandbox
- **Infrastructure:** AWS Lambda for bulk processing (optional)

### 11.2 Team Resources
- **Lead Developer:** 1 FTE for 8 weeks
- **Salesforce Admin:** 0.5 FTE for configuration
- **QA Tester:** 0.5 FTE weeks 6-8
- **Technical Writer:** 0.25 FTE for documentation

### 11.3 Budget Estimate
- **Development:** 320 hours @ $150/hr = $48,000
- **Testing:** 80 hours @ $100/hr = $8,000
- **Documentation:** 40 hours @ $75/hr = $3,000
- **Infrastructure:** $500/month ongoing
- **Total Project Cost:** ~$60,000

---

## 12. Next Steps

### Immediate Actions (Week 1)
1. **Review and approve plan** with stakeholders
2. **Set up development environment** with Sandbox access
3. **Begin field discovery** using metadata analyzer
4. **Document current validation rules** from production

### Prerequisites
- [ ] Salesforce Sandbox provisioned
- [ ] API access credentials configured
- [ ] Development environment setup
- [ ] Project repository access granted
- [ ] Test data identified

### Communication Plan
- **Weekly Status Reports** to stakeholders
- **Bi-weekly Demos** of new functionality
- **Daily Standups** during development
- **Final Presentation** at project completion

---

## Appendix A: Sample Field Catalog Structure

```json
{
  "account_fields": {
    "standard_fields": [
      {
        "api_name": "Name",
        "label": "Account Name",
        "type": "string",
        "length": 255,
        "required": true,
        "updateable": true,
        "description": "The name of the account"
      },
      {
        "api_name": "Type",
        "label": "Account Type",
        "type": "picklist",
        "required": false,
        "values": ["Prospect", "Customer", "Partner"],
        "description": "The type of account"
      }
    ],
    "custom_fields": [
      {
        "api_name": "Credit_Terms__c",
        "label": "Credit Terms",
        "type": "picklist",
        "required": true,
        "values": ["Net 30", "Net 60", "Net 90", "Prepay"],
        "description": "Payment terms for the account"
      },
      {
        "api_name": "Primary_Advertiser_ID__c",
        "label": "Primary Advertiser ID",
        "type": "string",
        "length": 50,
        "required_when": "Type == 'Customer'",
        "description": "The primary advertiser identifier"
      }
    ]
  }
}
```

---

## Appendix B: Validation Rule Examples

```python
class CustomerTypeValidation:
    """Validates Customer type requirements"""

    def validate(self, account_data):
        if account_data.get('Type') == 'Customer':
            # Check closed opportunity count
            opp_count = self.get_closed_opportunity_count(account_data.get('Id'))
            if opp_count < 1:
                return ValidationError("Cannot set Type to Customer without closed opportunities")

            # Check required fields for Customer
            required = ['Primary_Advertiser_ID__c', 'Platform_Default_Tracking_ID__c']
            for field in required:
                if not account_data.get(field):
                    return ValidationError(f"{field} is required for Customer accounts")

        return ValidationSuccess()
```

---

## Appendix C: Migration Script Example

```python
# migrate_accounts.py
import argparse
from sf_account_migrator import AccountDataMigrator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True, help='Source environment config')
    parser.add_argument('--target', required=True, help='Target environment config')
    parser.add_argument('--filter', help='SOQL filter for accounts')
    parser.add_argument('--batch-size', type=int, default=10000)

    args = parser.parse_args()

    # Initialize migrator
    migrator = AccountDataMigrator(
        source_config=load_config(args.source),
        target_config=load_config(args.target)
    )

    # Run migration
    results = migrator.migrate_accounts(
        filter_criteria=args.filter,
        batch_size=args.batch_size
    )

    # Report results
    print(f"Migration complete: {results['success']} succeeded, {results['errors']} failed")

if __name__ == '__main__':
    main()
```

---

*Document Version: 1.0.0*
*Created: 2024-09-17*
*Author: Evolution Media Group Development Team*
*Status: Draft - Pending Review*