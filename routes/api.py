from fastapi import APIRouter
from src.endpoints import namegender, emailaddress, items

router = APIRouter()
router.include_router(namegender.router)
# router.include_router(email.router)
# router.include_router(address.router)
# router.include_router(items.router)