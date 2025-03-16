from pydantic import BaseModel

class Items(BaseModel):
    _id: object
    items: list = [str]
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "items" : [ "Beets" ]
            }
        }