# Reference Flow

## Purpose
Complete onboarding flow example used as validation reference. Contains all SQL and MongoDB operations needed to onboard a company.

## Content
- `perfil_transaccional.md` - Full onboarding example with transactional profile, SQL inserts (companies, users, accounts, relations), and MongoDB operations (transfer rules, user profiles)

## Current Generation Method
**Primary**: `app/scripts/generator.py` - Generates scripts from Pydantic schemas
**Schemas**: `app/schemas/` - Pydantic models for data validation
**Tests**: `tests/beatnorth.py` - Example usage with real data

## Usage
Use this as reference to validate generated scripts. Compare output from `generate_scripts_db()` with this file to ensure correctness.

## Validation
```python
from app.scripts.generator import generate_scripts_db
from tests.original_data import data_final_beatnorth

# Generate script from schema
generated = generate_scripts_db(payload)

# Compare with reference
reference = open("docs/reference_flow/perfil_transaccional.md").read()
assert normalize(generated) == normalize(reference)
```

## Related
- Generator: `../../app/scripts/generator.py`
- Schemas: `../../app/schemas/`
- Tests: `../../tests/beatnorth.py`
- Templates: `../onboarding_templates/`