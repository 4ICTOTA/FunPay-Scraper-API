from pydantic import BaseModel
from typing import Optional


class UsersRequest(BaseModel):
    """ Request schema to get FunPay users
    """

    start_id: Optional[int] = 1
    end_id: Optional[int] = 10