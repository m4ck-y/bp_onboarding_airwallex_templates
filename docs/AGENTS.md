# AGENTS.md

## Purpose
Instructions for AI agents working with this documentation structure.

## Directory Structure

### reference_flow/
Contains complete onboarding flow examples used as template sources.

**Action**: Always create `README.md` explaining:
- Purpose of the folder
- Content description
- Usage guidelines
- Related folders

### onboarding_templates/
Reusable SQL and MongoDB templates for company onboarding.

**Action**: Always create `README.md` explaining:
- Purpose of the folder
- Execution order (numerical)
- Template variables and placeholders
- Dependencies (sequences, collections)
- Related folders

### completed_onboardings/
Real onboarding flows executed for actual companies.

**Action**: Always create `README.md` explaining:
- Purpose of the folder
- File naming convention (YYYY_MM_DD_COMPANY_NAME.md)
- Usage guidelines
- Related folders

## README.md Requirements

All README.md files MUST:
- Be written in English
- Be compact but understandable for AI
- Include: Purpose, Content/Structure, Usage, Related sections
- Use clear headers and bullet points
- Avoid unnecessary human-oriented explanations

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