INSERT INTO public.users (
    id_user,
    company_id,
    country_id,
    first_name,
    last_name,
    phone_number,
    terms_and_conditions,
    privacy_policy,
    kyc,
    services_contract,
    newsletter,
    birthdate,
    status,
    verified_email,
    user_type_id,
    working_position,
    deleted_at,
    created_at,
    modified_at,
    "owner",
    ext_id_user,
    country_risk,
    role_id,
    banpay_account_id,
    lead_id
) VALUES (
    nextval('users_id_user_seq'::regclass),
    currval('companies_id_company_seq'::regclass),
    139, --{ fk country_id}
    'ELISA', -- {sumsub : nombre} {sumsub: 1.1 }#DUDA: se extra de informacion personal o del cuestionario?
    'JIMENEZ BACILIO', -- {sumsub : apellido} { sumsub: 1.3 }
    '+522441054986', -- {sumsub : telefono} {sumsub: 1.4}
    true,
    true,
    'completed/GREEN',
    false,
    false,
    NULL,
    1,
    true,
    2,
    'Business Admin',
    NULL,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    true,
    uuid_generate_v4(),
    5, -- {country_risk}
    1,
    currval('banpay_accounts_id_banpay_account_seq'::regclass),
    'a790c509-519b-4467-8175-d42b7a2aadc1' -- {lead_id} #TODO: consultar colleccion de mongo
);