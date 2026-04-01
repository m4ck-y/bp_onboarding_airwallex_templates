from pydantic import BaseModel


class schema_outbound(BaseModel):
    per_transaction: int
    daily: int
    monthly: int
    #currency

class schema_support_info(BaseModel):
    #datetime
    risk_score: int
    outbound_transactions: schema_outbound