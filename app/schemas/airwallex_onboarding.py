from pydantic import BaseModel

from app.schemas.mongo_lead import schema_mongo_lead
from app.schemas.sumsub import schema_sumsub_company
from app.schemas.support_info import schema_support_info


class schema_airwallex_onboarding(BaseModel):
    mongo_data: schema_mongo_lead
    sumsub_company: schema_sumsub_company
    support_info: schema_support_info


    def get_airwalllex_account_id(self, id:str=None): #acct_hV_DwqCVOrOk6aSzdz_WMA
        return id or f"{{ #TODO:airwallex.{self.sumsub_company.comercial_name}}}"