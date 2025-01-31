from fastapi import APIRouter

from ..config import settings
from ..utils import BelvoAPIClient

client = BelvoAPIClient(
    base_url=settings.belvo_base_url,
    username=settings.belvo_username,
    password=settings.belvo_password,
)


router = APIRouter(
    tags=["belvo"],
    responses={404: {"description": "Not found"}},
)


@router.get("/institutions/")
def get_institutions():
    """Get all Belvo institutions that have been linked"""
    return client.get_institutions()


@router.get("/accounts/")
def get_accounts(institution: str):
    """Get all accounts for a given institution"""
    return client.get_accounts(institution)


@router.get("/transactions/")
def get_transactions(link: str, account: str):
    """Get all transactions for a given link and account"""
    return client.get_transactions(link, account)
