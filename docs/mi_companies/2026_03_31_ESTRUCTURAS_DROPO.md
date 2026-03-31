<!-->
ESTRUCTURAS DROPO SA DE CV
Risk score: 4
Outbound transactions:

Per transaction: $7,000 CAD
Daily: $10,000 CAD
Monthly: $16,667 CAD
-->

```sql
INSERT INTO public.companies (
    id_company,
    country_id,
    company_type_id,
    company_name,
    registration_number,
    legal_representative,
    kyb_status,
    phone_number,
    email,
    state,
    city,
    address_line_1,
    address_line_2,
    zip_code,
    country_risk,
    verification_status,
    active,
    created_in_manigo,
    deleted_at,
    created_at,
    modified_at,
    state_iso
) VALUES (
    nextval('companies_id_company_seq'::regclass),
    240,
    7,
    'COMERCIALIZADORA TOPIK SA DE CV', -- 1.1 Nombre comercial registrado
    'CTO210813AM5', -- 1.4 Número de registro fiscal
    '',
    'completed/GREEN',
    '+526142472438',-- 1.11 Numero Telefonico de la compañía
    'comercializadora.topik@outlook.com', -- 1.12 Correo electrónico de contacto corporativo
    'PUEBLA', -- 1.8 Provincia, estado o territorio
    'SAN PEDRO CHOLULA', -- 1.7 ciudad
    'CALLE 12 ORIENTE, NÚMERO 603, INTERIOR 06', -- 1.5 domicilio de la empresa
    '06', --1.6 Numero de edificio / piso
    '77024', -- 1.9 codigo postal
    5, -- {risk_score}
    0,
    true,
    true,
    NULL,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    'PUE' -- {state_iso from 1.8}
);

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

INSERT INTO public.users_info (
    id_user_info,
    user_id,
    state,
    city,
    address_line_1,
    address_line_2,
    zip_code,
    state_iso
) VALUES (
    nextval('users_info_id_user_info_seq'::regclass),
    currval('users_id_user_seq'::regclass),
    'PUEBLA', -- sumsub 2.6 - state # DUDA el usuario no ingreso el estado
    'PUEBLA', -- # sumsub 2.4 city # no 
    'CALLE MAGNOLIAS NUMERO 6 FRACCIONAMIENTO VALLE REAL', -- {sumsub 2.1}
    '', -- # DUDA, este campo es nullable, no seria mejor dejarlo en null?
    '74367', -- {sumsub 2.1}
    'PUE'
);

INSERT INTO public.users_manigo_relations (
    id_user_relation,
    user_id_banpay,
    user_id_manigo,
    client_id,
    external_user_id,
    deleted_at,
    created_at,
    modified_at,
    member_id,
    ext_member_id,
    ext_account_id,
    ext_contact_id
) VALUES (
    nextval('users_manigo_relations_id_user_relation_seq'::regclass),
    currval('users_id_user_seq'::regclass),
    NULL,
    5,
    'acct_J0Jj3ijKNoyefGwAOgaYjA',
    NULL,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    NULL,
    NULL,
    'acct_J0Jj3ijKNoyefGwAOgaYjA',
    'acct_J0Jj3ijKNoyefGwAOgaYjA'
);



INSERT INTO public.user_sessions (
    id_user_session,
    user_id,
    email,
    "password",
    deleted_at,
    created_at,
    modified_at,
    mfa_device_name,
    mfa_last_updated,
    has_mfa_mobile,
    has_mfa_business_app
) VALUES (
    nextval('user_sessions_id_user_session_seq'::regclass),
    currval('users_id_user_seq'::regclass),
    'serviciosadmonycontrol@grupontemx.com', -- {sumsub: company_email}
    '{#TODO: mongo.password}',
    NULL,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    NULL,
    NULL,
    false,
    false
);
```

```js
profile_doc = {
    profile: "COMERCIALIZADORA TOPIK SA DE CV",
    max_txn_per_day: 10,
    max_amount_per_day: 10000, // outbound transactions daily
    min_time_between_txn: 1,
    currency: ["CAD", "USD", "EUR", "MXN", "GBP"],
    specified_income: 16667, // outbound transactions monthly
    max_score_kyt: 30,
    max_txn_same_amount: 5,
    max_txn_consecutive: 5,
    max_consecutive_amount: 5,
    min_consecutive_amount: 10,
    max_days_inactive: 90,
    max_amount_per_txn: 7000, // outbound transactions per transaction
    created_at: new Date(),
    updated_at: new Date()
};
result_transfer_rules = db.TransferRules.insertOne(profile_doc);

inserted_id_str = result_transfer_rules.insertedId.toString();

db.UsersProfileRules.insertOne({
    user_id: 378,
    username: "JESUS GOMEZ MARTINEZ", // sumsub benerificiary[director, representative]
    email: "serviciosadmonycontrol@grupontemx.com", // sumsub company email
    profile_id: inserted_id_str,
    company_id: 334
});

db.UserProfiles.insertOne({
    "IdUserBanpay": 378,
    "UserNickname": "",
    "UserPin": "",
    "UserAvatar": "",
    "FavoriteCurrency": "CAD",
    "FavoriteTimezone": "America/Vancouver (PDT)"
});
```