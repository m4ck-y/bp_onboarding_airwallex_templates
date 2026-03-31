/*
 * ===========================================
 * Step 1: Insert Company - BEATNORTH LLC
 * ===========================================
 */

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