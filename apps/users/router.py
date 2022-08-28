from fastapi import APIRouter, status


router = APIRouter(
    prefix = "/users",
    tags = ["Users parser"])


@router.post(
    path = "/parse",
    status_code = status.HTTP_200_OK)
async def get_users():
    """ Endpoint to get FunPay users
    """