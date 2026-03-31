/*
 * =================================================
 * Step 2: Insert Companies Manigo Relations
 * =================================================
 */

INSERT INTO public.companies_manigo_relations (
    id_company_relation,
    company_id_banpay,
    company_id_manigo,
    type_of_business_verification_status,
    external_company_id,
    external_user_id,
    external_group_id,
    deleted_at,
    created_at,
    modified_at,
    client_manigo_id
) VALUES (
    nextval('companies_manigo_relations_id_company_relation_seq'::regclass),
    currval('companies_id_company_seq'::regclass),
    0,
    '1',
    'acct_J0Jj3ijKNoyefGwAOgaYjA', -- {external_company_id}
    'acct_J0Jj3ijKNoyefGwAOgaYjA', -- {external_user_id}
    NULL, -- {external_group_id}
    NULL,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    5 -- default id: 5 for airwallex
);