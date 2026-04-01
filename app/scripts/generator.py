from app.schemas.airwallex_onboarding import schema_airwallex_onboarding


COMPANY_TYPE_ID = 7

DB_INITIAL_USER_ID = 376
DB_INITIAL_COMPANY_ID = 333

DB_NEXT_USER_ID = DB_INITIAL_USER_ID + 1
DB_NEXT_COMPANY_ID = DB_INITIAL_COMPANY_ID + 1


def generate_scripts_db(payload: schema_airwallex_onboarding):
    DB_NEXT_COMPANY_ID = DB_INITIAL_COMPANY_ID + 1
    DB_NEXT_USER_ID = DB_INITIAL_USER_ID + 1

    return f"""

INSERT INTO public.companies(
    id_company, country_id, company_type_id, company_name, registration_number,
    legal_representative, kyb_status, phone_number, email, state,
    city, address_line_1, address_line_2, zip_code, country_risk,
    verification_status, active, created_in_manigo, deleted_at, created_at,
    modified_at, state_iso)
VALUES(
    nextval('companies_id_company_seq'::regclass), {payload.sumsub_company.get_country_id()}, {COMPANY_TYPE_ID}, '{payload.sumsub_company.comercial_name}', '{payload.sumsub_company.fiscal_register_number}',
    '', 'completed/GREEN', '{payload.sumsub_company.phone_number}', '{payload.sumsub_company.email}', '{payload.sumsub_company.state}',
    '{payload.sumsub_company.city}', '{payload.sumsub_company.address_1}', '{payload.sumsub_company.address_2}', '{payload.sumsub_company.postal_code}', {payload.support_info.risk_score},
    0, true, true, NULL, CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP, '{payload.sumsub_company.get_state_iso()}');

INSERT INTO public.companies_manigo_relations(
    id_company_relation, company_id_banpay, company_id_manigo, type_of_business_verification_status, external_company_id,
    external_user_id, external_group_id, deleted_at, created_at, modified_at,
    client_manigo_id)
VALUES(
    nextval('companies_manigo_relations_id_company_relation_seq'::regclass), currval('companies_id_company_seq'::regclass), 0, '1', '{payload.get_airwalllex_account_id()}',
    '{payload.get_airwalllex_account_id()}', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,
    5);

INSERT INTO public.banpay_accounts(
    id_banpay_account, company_id, banpay_account_type_id, status, external_id,
    created_at, modified_at, deleted_at)
VALUES(
    nextval('banpay_accounts_id_banpay_account_seq'::regclass), currval('companies_id_company_seq'::regclass), 1, 1, uuid_generate_v4(),
    CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL);

INSERT INTO public.users(
    id_user, company_id, country_id, first_name, last_name,
    phone_number, terms_and_conditions, privacy_policy, kyc, services_contract,
    newsletter, birthdate, status, verified_email, user_type_id,
    working_position, deleted_at, created_at, modified_at, "owner",
    ext_id_user, country_risk, role_id, banpay_account_id, lead_id)
VALUES(
    nextval('users_id_user_seq'::regclass), currval('companies_id_company_seq'::regclass), {payload.sumsub_company.ubu_representative.get_country_id()}, '{payload.sumsub_company.ubu_representative.first_name}', '{payload.sumsub_company.ubu_representative.last_name}',
    '{payload.sumsub_company.ubu_representative.phone_number}', true, true, 'completed/GREEN', false,
    false, NULL, 1, true, 2,
    'Business Admin', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, true,
    uuid_generate_v4(), 9, 1, currval('banpay_accounts_id_banpay_account_seq'::regclass), 'a790c509-519b-4467-8175-d42b7a2aadc1'
    );

INSERT INTO public.users_info(
    id_user_info, user_id, state, city, address_line_1,
    address_line_2, zip_code, state_iso)
VALUES(
    nextval('users_info_id_user_info_seq'::regclass), currval('users_id_user_seq'::regclass), '{payload.sumsub_company.ubu_representative.state}', '{payload.sumsub_company.ubu_representative.city}', '{payload.sumsub_company.ubu_representative.address_line_1}',
    '{payload.sumsub_company.ubu_representative.address_line_2}', '{payload.sumsub_company.ubu_representative.postal_code}', '{payload.sumsub_company.ubu_representative.get_state_iso()}');

INSERT INTO public.users_manigo_relations(
    id_user_relation, user_id_banpay, user_id_manigo, client_id, external_user_id, deleted_at,
    created_at, modified_at, member_id, ext_member_id, ext_account_id, ext_contact_id
)
VALUES(
    nextval('users_manigo_relations_id_user_relation_seq'::regclass), currval('users_id_user_seq'::regclass), NULL, 5, '{payload.get_airwalllex_account_id()}', NULL,
    CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL, NULL, '{payload.get_airwalllex_account_id()}', '{payload.get_airwalllex_account_id()}');

INSERT INTO public.user_sessions(
    id_user_session, user_id, email, "password", deleted_at,
    created_at, modified_at, mfa_device_name, mfa_last_updated, has_mfa_mobile,
    has_mfa_business_app
)
VALUES(
    nextval('user_sessions_id_user_session_seq'::regclass), currval('users_id_user_seq'::regclass), '{payload.sumsub_company.email}', '{payload.mongo_data.user_information.password}', NULL,
    CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL, NULL, false, 
    false
);

profile_doc = {{
    profile: "{payload.sumsub_company.comercial_name}",
    max_txn_per_day: 10,
    max_amount_per_day: {payload.support_info.outbound_transactions.daily},
    min_time_between_txn: 1,
    currency: ["CAD", "USD", "EUR", "MXN", "GBP"],
    specified_income: {payload.support_info.outbound_transactions.monthly},
    max_score_kyt: 30,
    max_txn_same_amount: 5,
    max_txn_consecutive: 5,
    max_consecutive_amount: 5,
    min_consecutive_amount: 10,
    max_days_inactive: 90,
    max_amount_per_txn: {payload.support_info.outbound_transactions.per_transaction},
    created_at: new Date(),
    updated_at: new Date()
}};

result_transfer_rules = db.TransferRules.insertOne(profile_doc);

inserted_id_str = result_transfer_rules.insertedId.toString();

db.UsersProfileRules.insertOne({{
    user_id: {DB_NEXT_USER_ID},
    username: "{payload.sumsub_company.ubu_representative.first_name} {payload.sumsub_company.ubu_representative.last_name}",
    email: "{payload.sumsub_company.email}",
    profile_id: inserted_id_str,
    company_id: {DB_NEXT_COMPANY_ID}
}});

db.UserProfiles.insertOne({{
    "IdUserBanpay": {DB_NEXT_USER_ID},
    "UserNickname": "",
    "UserPin": "",
    "UserAvatar": "",
    "FavoriteCurrency": "CAD",
    "FavoriteTimezone": "America/Vancouver (PDT)"
}});
"""
