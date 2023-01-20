from pydantic import BaseModel, SecretStr, HttpUrl, Json

class Employee(BaseModel):
    ID: str
    pwd: SecretStr
    salary: int
    details: Json     
    FBProfile: HttpUrl

    @validator('ID')
    def alphanum(cls, x):
        if x.isalnum()==False:
            raise (ValueError('Must be alphanumeric'))

