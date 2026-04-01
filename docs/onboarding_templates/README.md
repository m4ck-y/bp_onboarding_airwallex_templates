# Onboarding Templates

## Purpose
Reusable SQL and MongoDB templates for company onboarding. Execute in numerical order.

## Execution Order
1. `01_companies.sql` - Insert company record
2. `02_companies_manigo_relations.sql` - Link company to Airwallex
3. `03_banpay_accounts.sql` - Create Banpay account
4. `04_users.sql` - Insert admin user
5. `05_users_info.sql` - Add user address info
6. `06_users_manigo_relations.sql` - Link user to Airwallex
7. `07_user_sessions.sql` - Create user session
8. `08_transfer_rules_profiles.js` - MongoDB: transfer rules + user profiles

## Template Variables
Replace placeholders in templates:
- `{external_company_id}` - Airwallex account ID
- `{external_user_id}` - Airwallex user ID
- `{sumsub: field}` - Data from Sumsub verification
- `{risk_score}` - Company risk score (1-10)
- `{state_iso}` - State ISO code from address

## Dependencies
PostgreSQL sequences: `companies_id_company_seq`, `users_id_user_seq`, `banpay_accounts_id_banpay_account_seq`, `user_sessions_id_user_session_seq`, `companies_manigo_relations_id_company_relation_seq`, `users_manigo_relations_id_user_relation_seq`, `users_info_id_user_info_seq`

## Related
- Reference: `../reference_flow/perfil_transaccional.md`
- Completed examples: `../completed_onboardings/`