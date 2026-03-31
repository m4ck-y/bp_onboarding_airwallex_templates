interface mongo_lead {
    lead_id: number,
    password: string,
}


interface sumsub_ubu_director_representative {
    first_name: string,
}


interface sumsub_company {
    ubu_representative: sumsub_ubu_director_representative,
    comercial_name: string,
    fiscal_register_number: string,
    phone_number: string,
    email: string,
    state: string,
    city: string,
    address_1: string,
    address_2: string,
    postal_code: string,
}

interface payload_onboarding_airwallex {
    mongo: mongo_lead,
    sumsub_company: sumsub_company,
    support_data: support_data,
}


interface support_

interface support_data {

    risk_score: number,
}

var example_data:payload_onboarding_airwallex = {
    mongo: {
        lead_id: 378,
        password: "some_password"
    },
    sumsub_company: {
        ubu_representative: {
            first_name: "JUAN CARLOS"
        },
        comercial_name: "COMERCIALIZADORA TOPIK SA DE CV",
        fiscal_register_number: "CTO210813AM5",
        phone_number: "+526142472438",
        email: "comercializadora.topik@outlook.com",
        state: "PUEBLA",
        city: "SAN PEDRO CHOLULA",
        address_1: "CALLE 12 ORIENTE, NÚMERO 603, INTERIOR 06",
        address_2: "06",
        postal_code: "77024"
    },
    support_data: {
        risk_score: 5,
        
    }
}

/**
 *
COMERCIALIZADORA TOPIK SA DE CV
Risk score: 5
Outbound transactions:

Per transaction: $7,000 CAD
Daily: $10,000 CAD
Monthly: $16,667 CAD


ESTRUCTURAS DROPO SA DE CV
Risk score: 4
Outbound transactions:

Per transaction: $7,000 CAD
Daily: $10,000 CAD
Monthly: $16,667 CAD


INJURY ANGELS INC
Risk score: 2
Outbound transactions:

Per transaction: $7,000 CAD
Daily: $10,000 CAD
Monthly: $16,667 CAD
 */

var datas


var search_id_country_postgres = (country: string) => -666
var search_iso_code = (country: string) => `{TODO: ISO CODE(${country})}`

var template_step_1 =`
INSERT INTO public.companies (
    id_company, country_id, company_type_id, company_name, registration_number, legal_representative, kyb_status, phone_number, email, state, city,
    address_line_1, address_line_2, zip_code, country_risk, verification_status, active, created_in_manigo, deleted_at, created_at, modified_at, state_iso
) VALUES (
    nextval('companies_id_company_seq'::regclass), ${search_id_country_postgres(example_data.sumsub_company.state)}, 7, '${example_data.sumsub_company.comercial_name}', '${example_data.sumsub_company.fiscal_register_number}', '', 'completed/GREEN', '${example_data.sumsub_company.phone_number}', '${example_data.sumsub_company.email}', '${example_data.sumsub_company.state}', '${example_data.sumsub_company.city}',
    '${example_data.sumsub_company.address_1}', '${example_data.sumsub_company.address_2}', '${example_data.sumsub_company.postal_code}', ${example_data.support_data.risk_score}, 0, true, true, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '${search_iso_code(example_data.sumsub_company.state)}'
);`



