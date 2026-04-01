# AGENTS.md

## Purpose
Instructions for AI agents working with this documentation structure.

## Directory Structure

### reference_flow/
Contains complete onboarding flow examples used as validation reference.

**Action**: Always create `README.md` explaining:
- Purpose of the folder
- Content description
- Usage guidelines
- Related folders

### onboarding_templates/
Reference templates showing SQL/MongoDB structure. Historical examples; actual generation uses Pydantic schemas.

**Action**: Always create `README.md` explaining:
- Purpose of the folder
- Template files (reference only)
- Schema structure
- Usage with generator
- Related folders

### completed_onboardings/
Real onboarding flows executed for actual companies.

**Action**: Always create `README.md` explaining:
- Purpose of the folder
- File naming convention (YYYY_MM_DD_COMPANY_NAME.md)
- Usage guidelines
- Related folders

## Current Generation Method

**Primary**: `app/scripts/generator.py` - Generates scripts from Pydantic schemas
**Schemas**: `app/schemas/` - Pydantic models for data validation
**Production Script**: `scripts/generate_onboarding.py` - Generates real BD scripts
**Test Script**: `tests/BEATNORTH_LLC_original.py` - Validates against reference

## Quick Commands
```bash
# Generate real BD scripts (output: data/)
python scripts/generate_onboarding.py

# Validate against reference (output: tests/)
python -m tests.BEATNORTH_LLC_original
```

## README.md Requirements

All README.md files MUST:
- Be written in English
- Be compact but understandable for AI
- Include: Purpose, Content/Structure, Usage, Related sections
- Use clear headers and bullet points
- Avoid unnecessary human-oriented explanations
- Reference the generator and schemas when applicable
- Include "Quick Commands" section with execution commands

## File Naming

- README.md - Directory documentation (always lowercase)
- AGENTS.md - AI agent instructions (always uppercase)
- SQL files - `NN_descriptive_name.sql` (numerical prefix)
- JS files - `NN_descriptive_name.js` (numerical prefix)
- MD files - `YYYY_MM_DD_COMPANY_NAME.md` (for completed onboardings)

## When Creating New Folders

1. Create the folder
2. Create README.md following the template above
3. Update this AGENTS.md if new patterns emerge
4. Keep documentation minimal and AI-focused
5. Reference the generator and schemas when applicable
6. Include "Quick Commands" section with execution commands