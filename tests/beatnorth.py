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
    filename = f"tests/output/{company_name_normalized}.txt"
    save_text_to_file(content, filename)


if __name__ == "__main__":
    generate_txt_with_copany_name("BEATNORTH LLC", data_final_beatnorth)





