from pydantic import BaseModel, field_validator

class NameGender(BaseModel):
    _id: object
    first_name: str
    last_name: str
    gender: str

    @field_validator('gender')
    def gender_validate(cls, gender):
        genderList = ["Male", "Female", "Others"]
        if gender not in genderList:
            raise ValueError(f"Gender must be either of Male, Female or Others")
        return gender
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "first_name" : "Innis",
                "last_name" : "Headingham",
                "gender" : "Male",
            }
        }