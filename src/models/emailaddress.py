from pydantic import BaseModel

class EmailAddress(BaseModel):
    _id: object
    email: str
    home_adress: str
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "email" : "iheadingham2@java.com",
                "home_adress" : "05 Moulton Court"
            }
        }