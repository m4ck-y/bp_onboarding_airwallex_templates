/*
 * ================================================
 * Step 3: Insert Banpay Accounts
 * ================================================
 */

INSERT INTO public.banpay_accounts (
    id_banpay_account,
    company_id,
    banpay_account_type_id,
    status,
    external_id,
    created_at,
    modified_at,
    deleted_at
) VALUES (
    nextval('banpay_accounts_id_banpay_account_seq'::regclass),
    currval('companies_id_company_seq'::regclass),
    1,
    1,
    uuid_generate_v4(),
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    NULL
);