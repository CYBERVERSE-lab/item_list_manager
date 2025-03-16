from fastapi import APIRouter, Body, Request, status
from src.models.namegender import NameGender

import src.rules.namegender as namegender

router = APIRouter(prefix="/namegender", tags=["NameGender"])

@router.get("/{name}", response_description="Get name and gender", status_code=status.HTTP_200_OK,response_model=NameGender)
async def getNameAndGender(request: Request, name: str):
    return namegender.getNameAndGender(request, name)

@router.post("/updateFirstName/{first_name}/{new_first_name}", response_description="Update first name", status_code=status.HTTP_202_ACCEPTED, response_model=NameGender)
async def updateFirstName(request: Request, first_name: str, new_first_name: str):
    return namegender.updateFirstName(request, first_name, new_first_name)

@router.post("/updateLastName/{last_name}/{new_last_name}", response_description="Update last name", status_code=status.HTTP_202_ACCEPTED, response_model=NameGender)
async def updateLastName(request: Request, last_name: str, new_last_name: str):
    return namegender.updateLastName(request, last_name, new_last_name)

@router.post("/updateGender/{gender}/{new_gender}", response_description="Updating gender information", status_code=status.HTTP_202_ACCEPTED, response_model=NameGender)
async def updateGender(request: Request, gender: str, new_gender: str):
    return namegender.updateGender(request, gender, new_gender)