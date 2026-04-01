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
    '{#TODO: mongo.password}', -- # TODO: mongo de leads collections?
    NULL,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP,
    NULL,
    NULL,
    false,
    false
);