from pydantic import BaseModel


class schema_ubu_representative(BaseModel):
    "questionnaire: 0005"

    first_name: str
    "1.1 First Name"

    last_name: str
    "1.3 Last Name"

    phone_number: str
    "1.4 Phone"

    address_line_1: str
    "2.1 Address Line 1"

    address_line_2: str
    "2.2 Address Line 2"

    city: str
    "2.4 City"

    postal_code: str
    "2.5 Zip/Postal Code"

    state: str
    "2.6 State or Province"

    country: str
    "2.7 Country"

    def get_country_id(self, id:int=None):
        return id or f"{{ #TODO:country_id.{self.country}}}"
    
    def get_state_iso(self, iso:str=None):
        return iso or f"{{ #TODO:state_iso.{self.state}}}"



class schema_sumsub_company(BaseModel):
    "questionnaire: 0001_2"

    ubu_representative: schema_ubu_representative # poncentaje mayor? , director, representative, si es el mismo, agarrar el primero

    comercial_name: str
    "1.1 Nombre Comercial Registrado"

    fiscal_register_number: str
    "1.4 Número de Registro Fiscal"

    address_1: str
    "1.5 Domicilio de la empresa"

    address_2: str
    "1.6 Número de Edificio / Piso"

    city: str
    "1.7 Ciudad"

    state: str
    "1.8 Provincia, Estado, o Territorio"

    postal_code: str
    "1.9 Código Postal - Zip Code"

    country: str
    "1.10 País"

    phone_number: str
    "1.11 Número Telefónico de la Compañía"
    
    email: str
    "1.12 Correo Electrónico de Contacto Corporativo"

    def get_country_id(self, id:int=None):
        return id or f"{{ #TODO:country_id.{self.country}}}"
    
    def get_state_iso(self, iso:str=None):
        return iso or f"{{ #TODO:state_iso.{self.state}}}"

