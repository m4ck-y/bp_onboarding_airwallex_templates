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