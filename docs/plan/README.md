# Plan: Template Generation from Schema

## Objective
Design replaceable templates that generate onboarding SQL/MongoDB scripts from Pydantic schemas, validated against reference flow.

## Current State

### Schemas (app/schemas/)
- `airwallex_onboarding.py` - Main schema combining all data
- `sumsub.py` - Company and representative data from Sumsub
- `support_info.py` - Risk score and transaction limits
- `mongo_lead.py` - MongoDB lead data (password, lead_id)

### Reference Flow
- `docs/reference_flow/perfil_transaccional.md` - Complete example with real data

### Templates
- `docs/onboarding_templates/` - 8 SQL/JS files with placeholders

## Design Approach

### 1. Template Placeholder Strategy

Use Python string templates with `${variable}` syntax:

```python
# Template example
INSERT INTO public.companies(
    company_name, 
    email
) VALUES (
    '${company_name}',  # From sumsub.comercial_name
    '${email}'          # From sumsub.email
);
```

**Why `${variable}`?**
- Clear visual distinction from SQL/JS syntax
- Easy to parse with `string.Template` or regex
- No conflicts with SQL `$1`, `$2` or JS template literals

### 2. Schema to Template Mapping

Create mapping file: `docs/plan/schema_to_template_mapping.md`

| Template Variable | Schema Path | Example Value |
|-------------------|-------------|---------------|
| `${company_name}` | sumsub_company.comercial_name | 'BEATNORTH LLC' |
| `${fiscal_register}` | sumsub_company.fiscal_register_number | '384385483' |
| `${representative_first}` | sumsub_company.ubu_representative.first_name | 'JESUS' |
| `${representative_last}` | sumsub_company.ubu_representative.last_name | 'GOMEZ MARTINEZ' |
| `${email}` | sumsub_company.email | 'serviciosadmonycontrol@grupontemx.com' |
| `${phone}` | sumsub_company.phone_number | '+525580008233' |
| `${state}` | sumsub_company.state | 'TEXAS' |
| `${city}` | sumsub_company.city | 'HOUSTON' |
| `${address_1}` | sumsub_company.address_1 | '8588 KATY FREEWAY SUITE 435' |
| `${address_2}` | sumsub_company.address_2 | '' |
| `${postal_code}` | sumsub_company.postal_code | '77024' |
| `${risk_score}` | support_info.risk_score | 9 |
| `${outbound_per_txn}` | support_info.outbound_transactions.per_transaction | 7000 |
| `${outbound_daily}` | support_info.outbound_transactions.daily | 10000 |
| `${outbound_monthly}` | support_info.outbound_transactions.monthly | 16667 |
| `${password}` | mongo_data.user_information.password | '$2b$12$...' |
| `${lead_id}` | mongo_data.administration.lead_id | 'a790c509-...' |
| `${external_company_id}` | (generated) | 'acct_hV_DwqCVOrOk6aSzdz_WMA' |
| `${external_user_id}` | (generated) | 'acct_hV_DwqCVOrOk6aSzdz_WMA' |

### 3. Implementation Steps

#### Step 1: Create Template Loader
```python
# app/template_loader.py
from string import Template
from pathlib import Path

def load_template(template_name: str) -> Template:
    path = Path(f"docs/onboarding_templates/{template_name}")
    return Template(path.read_text())

def render_template(template: Template, data: dict) -> str:
    return template.safe_substitute(data)
```

#### Step 2: Create Data Mapper
```python
# app/data_mapper.py
from app.schemas.airwallex_onboarding import schema_airwallex_onboarding

def schema_to_template_vars(schema: schema_airwallex_onboarding) -> dict:
    return {
        'company_name': schema.sumsub_company.comercial_name,
        'fiscal_register': schema.sumsub_company.fiscal_register_number,
        'representative_first': schema.sumsub_company.ubu_representative.first_name,
        'representative_last': schema.sumsub_company.ubu_representative.last_name,
        # ... all other mappings
    }
```

#### Step 3: Create Script Generator
```python
# app/script_generator.py
def generate_onboarding_script(schema: schema_airwallex_onboarding) -> str:
    vars = schema_to_template_vars(schema)
    
    steps = []
    for i in range(1, 9):
        template_file = f"{i:02d}_*.sql" if i < 8 else f"{i:02d}_*.js"
        template = load_template(template_file)
        steps.append(render_template(template, vars))
    
    return "\n\n".join(steps)
```

#### Step 4: Create Validator
```python
# app/validator.py
def compare_with_reference(generated: str, reference_path: str) -> dict:
    reference = Path(reference_path).read_text()
    
    # Normalize whitespace
    gen_normalized = normalize(generated)
    ref_normalized = normalize(reference)
    
    # Compare section by section
    return {
        'match': gen_normalized == ref_normalized,
        'differences': find_differences(gen_normalized, ref_normalized),
        'similarity_score': calculate_similarity(gen_normalized, ref_normalized)
    }
```

### 4. Testing with perfil_transaccional.md

#### Step 1: Extract Data from Reference
```python
# Extract from perfil_transaccional.md lines 1-86
reference_data = schema_airwallex_onboarding(
    sumsub_company=schema_sumsub_company(
        ubu_representative=schema_ubu_representative(
            first_name="JESUS",
            last_name="GOMEZ MARTINEZ",
        ),
        comercial_name="BEATNORTH LLC",
        fiscal_register_number="384385483",
        phone_number="+525580008233",
        email="serviciosadmonycontrol@grupontemx.com",
        state="TEXAS",
        city="HOUSTON",
        address_1="8588 KATY FREEWAY SUITE 435",
        address_2="",
        postal_code="77024",
    ),
    mongo_data=schema_mongo_lead(
        user_information=schema_user_information(
            password="$2b$12$MyiF5Quj8F94jnx0AJbvaOyIq0K.kByAI61WqUC3wH1cIIsFotkDS"
        ),
        administration=schema_administration(
            lead_id="a790c509-519b-4467-8175-d42b7a2aadc1"
        ),
    ),
    support_info=schema_support_info(
        risk_score=9,
        outbound_transactions=schema_outbound(
            per_transaction=7000,
            daily=10000,
            monthly=16667,
        ),
    ),
)
```

#### Step 2: Generate Script
```python
generated = generate_onboarding_script(reference_data)
```

#### Step 3: Compare
```python
result = compare_with_reference(
    generated, 
    "docs/reference_flow/perfil_transaccional.md"
)
print(f"Match: {result['match']}")
print(f"Similarity: {result['similarity_score']}%")
```

### 5. File Structure

```
docs/
├── plan/
│   └── README.md                    # This file
├── onboarding_templates/
│   ├── 01_companies.sql             # Template with ${variables}
│   ├── 02_companies_manigo_relations.sql
│   ├── ...
│   └── 08_transfer_rules_profiles.js
├── reference_flow/
│   └── perfil_transaccional.md      # Reference for validation
└── completed_onboardings/           # Real examples

app/
├── schemas/                         # Existing Pydantic schemas
├── template_loader.py               # NEW: Load and render templates
├── data_mapper.py                   # NEW: Schema → template vars
├── script_generator.py              # NEW: Generate complete script
└── validator.py                     # NEW: Compare with reference
```

### 6. Validation Criteria

**Success Metrics:**
- Similarity score ≥ 95% (allowing for whitespace differences)
- All SQL statements syntactically valid
- All MongoDB operations syntactically valid
- Sequence references (`currval`, `nextval`) correctly placed
- Comments preserved where applicable

**Known Differences to Handle:**
- Whitespace variations (acceptable)
- Comment placement (acceptable)
- Line breaks (acceptable)
- Actual data values must match exactly

### 7. Next Steps

1. [ ] Create `schema_to_template_mapping.md` with complete variable list
2. [ ] Update templates in `onboarding_templates/` to use `${variable}` syntax
3. [ ] Implement `template_loader.py`
4. [ ] Implement `data_mapper.py`
5. [ ] Implement `script_generator.py`
6. [ ] Implement `validator.py`
7. [ ] Test with `perfil_transaccional.md` reference
8. [ ] Document results in `docs/plan/validation_results.md`

## Benefits

- **Reusable**: One schema generates complete onboarding script
- **Validated**: Reference flow ensures correctness
- **Maintainable**: Templates separate from logic
- **Testable**: Automated comparison with known good output
- **Scalable**: Add new templates without changing generator logic