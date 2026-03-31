/*
 * =====================================================
 * Step 6: Insert Users Manigo Relations
 * =====================================================
 */

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