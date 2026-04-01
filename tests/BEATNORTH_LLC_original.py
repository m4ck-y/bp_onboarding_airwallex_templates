from tests.original_data import data_final_beatnorth
from app.schemas.airwallex_onboarding import schema_airwallex_onboarding
from app.schemas.support_info import schema_support_info, schema_outbound
from app.schemas.sumsub import schema_sumsub_company, schema_ubu_representative
from app.schemas.mongo_lead import (
    schema_mongo_lead,
    schema_administration,
    schema_user_information,
)
from app.scripts.generator import generate_scripts_db

from app.utils.file import save_text_to_file
from app.utils.text import normalize_to_upper_snake


def generate_txt_with_copany_name(company_name: str, content: str):
    company_name_normalized = normalize_to_upper_snake(company_name)
    filename = f"tests/{company_name_normalized}.output.txt"
    save_text_to_file(content, filename)


data = schema_airwallex_onboarding(

    mongo_data=schema_mongo_lead(
        user_information=schema_user_information(
            password="#TODO:mongo.password"
        ),
        administration=schema_administration(
            lead_id="{#TODO:mongo.lead_id}"
        ),
    ),

    sumsub_company=schema_sumsub_company(
        comercial_name="BEATNORTH LLC",
        fiscal_register_number="384385483",
        address_1="8588 KATY FREEWAY SUITE 435",
        address_2="",
        city="HOUSTON",
        state="TEXAS",
        postal_code="77024",
        country="UNITED STATES OF AMERICA",
        phone_number="+525580008233",
        email="serviciosadmonycontrol@grupontemx.com",

        ubu_representative=schema_ubu_representative(
            first_name="JESUS",
            last_name="GOMEZ MARTINEZ",
            phone_number="+525543677677",
            address_line_1="JAVIER BARROS SIERRA 540",
            address_line_2="PISO 5, OFICINA 5021",
            city="CIUDAD DE MEXICO",
            postal_code="01210",
            state="CIUDAD DE MEXICO", # empty
            country="MEXICO",
        )

    ),

    support_info=schema_support_info(
        risk_score=9,
        outbound_transactions=schema_outbound(
            per_transaction=7000,
            daily=395000,
            monthly=470000
        )
    )

)


if __name__ == "__main__":
    data_str_output = generate_scripts_db(data)
    print("is same?", data_str_output == data_final_beatnorth)
    generate_txt_with_copany_name("BEATNORTH LLC", data_str_output)








