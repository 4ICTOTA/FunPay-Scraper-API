import requests, re, time
from bs4 import BeautifulSoup
from fastapi import HTTPException, status
from .schemas import UsersRequest


async def _get_users(
    value: UsersRequest
):
    """ Method to get FunPay users
    """

    if value.end_id < value.start_id:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "End ID cannot be less than the start ID.")

    users = []

    while value.start_id <= value.end_id:

        try:

            url = f"https://funpay.com/users/{value.start_id}/"

            userpage = requests.get(
                url = url)

            # if the request is successful
            if userpage.status_code == 200:

                soup = BeautifulSoup(userpage.text, "lxml")

                # get username
                try:
                    username = soup.find(
                        name = "span", 
                        class_= "mr4").getText()

                except:
                    username = None 

                # get moderator status
                try:
                    usermoder = soup.find(
                        name = "span", 
                        class_ = "label label-success").getText()

                except:
                    usermoder = None

                # get user online or last time online    
                try:
                    useronline = soup.find(
                        name = "span", 
                        class_ = "media-user-status").getText()
                    
                    useronline = re.sub(" +", " ", useronline.strip())
                except:
                    useronline = None

                # get user block status
                try: 
                    userblock = soup.find(
                        name = "span", 
                        class_ = "label label-danger").getText()

                except:
                    userblock = None
            
            else:
                raise HTTPException(
                    status_code = userpage.status_code,
                    detail = "Failed request.")

            time.sleep(0.5)

        except Exception as e:
            raise HTTPException(
                    status_code = status.HTTP_400_BAD_REQUEST,
                    detail = f"Unexpected error.\n{e}")

        users.append(
            {
                "userid": value.start_id,
                "username": username,
                "usermoder": usermoder,
                "useronline": useronline,
                "userblock": userblock
            })

        value.start_id += 1

    return {
        "users": users 
    }   