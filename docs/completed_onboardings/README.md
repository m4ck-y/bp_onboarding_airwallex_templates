# Completed Onboardings

## Purpose
Real onboarding flows executed for actual companies. Each file contains complete SQL and MongoDB operations with real data.

## Content
- `YYYY_MM_DD_COMPANY_NAME.md` - Completed onboarding with all inserts and configurations

## File Naming Convention
Format: `YYYY_MM_DD_COMPANY_NAME.md`
- `YYYY` - Year (4 digits)
- `MM` - Month (2 digits)
- `DD` - Day (2 digits)
- `COMPANY_NAME` - Company name in UPPERCASE with underscores

## Current Generation Method
**Primary**: `app/scripts/generator.py` - Generates scripts from Pydantic schemas
**Schemas**: `app/schemas/` - Pydantic models for data validation
**Tests**: `tests/beatnorth.py` - Example usage with real data

## Usage
Reference for:
- Understanding real onboarding data patterns
- Debugging onboarding issues
- Creating new schemas based on successful onboardings

## Related
- Generator: `../../app/scripts/generator.py`
- Schemas: `../../app/schemas/`
- Tests: `../../tests/beatnorth.py`
- Reference: `../reference_flow/perfil_transaccional.md`