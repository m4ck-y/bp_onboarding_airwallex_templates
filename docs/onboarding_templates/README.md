# Onboarding Templates

## Purpose
Reference templates showing SQL/MongoDB structure for company onboarding. These are historical examples; actual generation uses Pydantic schemas.

## Current Generation Method
**Primary**: `app/scripts/generator.py` - Generates scripts from Pydantic schemas
**Schemas**: `app/schemas/` - Pydantic models for data validation
**Tests**: `tests/beatnorth.py` - Example usage with real data

## Template Files (Reference Only)
Execution order for onboarding flow:
1. `01_companies.sql` - Insert company record
2. `02_companies_manigo_relations.sql` - Link company to Airwallex
3. `03_banpay_accounts.sql` - Create Banpay account
4. `04_users.sql` - Insert admin user
5. `05_users_info.sql` - Add user address
6. `06_users_manigo_relations.sql` - Link user to Airwallex
7. `07_user_sessions.sql` - Create user session
8. `08_transfer_rules_profiles.js` - MongoDB: transfer rules + profiles

## Schema Structure
```
schema_airwallex_onboarding
├── sumsub_company: schema_sumsub_company
│   ├── ubu_representative: schema_ubu_representative
│   ├── comercial_name, fiscal_register_number
│   ├── address_1, address_2, city, state, postal_code, country
│   ├── phone_number, email
│   └── get_country_id(), get_state_iso()
├── mongo_data: schema_mongo_lead
│   ├── user_information: schema_user_information (password)
│   └── administration: schema_administration (lead_id)
└── support_info: schema_support_info
    ├── risk_score: int
    └── outbound_transactions: schema_outbound
        ├── per_transaction, daily, monthly
```

## Usage
```python
from app.scripts.generator import generate_scripts_db
from app.schemas.airwallex_onboarding import schema_airwallex_onboarding

# Create schema instance with data
payload = schema_airwallex_onboarding(...)

# Generate complete SQL/MongoDB script
script = generate_scripts_db(payload)
```

## Related
- Generator: `../../app/scripts/generator.py`
- Schemas: `../../app/schemas/`
- Tests: `../../tests/beatnorth.py`
- Reference: `../reference_flow/perfil_transaccional.md`