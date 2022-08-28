from fastapi import APIRouter, status
from .services import _get_users
from .schemas import UsersRequest


router = APIRouter(
    prefix = "/users",
    tags = ["Users parser"])


@router.post(
    path = "/parse",
    status_code = status.HTTP_200_OK)
async def get_users(
    request: UsersRequest
):
    """ Endpoint to get FunPay users
    """

    response = await _get_users(
        value = request)

    return response