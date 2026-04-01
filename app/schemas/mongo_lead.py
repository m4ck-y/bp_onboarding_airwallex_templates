from pydantic import BaseModel


class schema_administration(BaseModel):
    lead_id: str

class schema_user_information(BaseModel):
    password: str


class schema_mongo_lead(BaseModel):
    user_information: schema_user_information
    administration: schema_administration