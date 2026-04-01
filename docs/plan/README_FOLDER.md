# Plan Folder

## Purpose
Design documents and implementation plans for template-based onboarding script generation.

## Content
- `README.md` - Main plan: template design, schema mapping, validation approach
- `schema_to_template_mapping.md` - Complete variable mapping between schemas and templates
- `reference_schema_example.py` - Example schema populated with reference flow data

## Usage
Review these documents before implementing the template generation system. They provide the blueprint for:
1. How templates should use `${variable}` placeholders
2. Which schema fields map to which template variables
3. How to validate generated scripts against reference flows

## Related
- Templates: `../onboarding_templates/`
- Reference: `../reference_flow/perfil_transaccional.md`
- Schemas: `../../app/schemas/`