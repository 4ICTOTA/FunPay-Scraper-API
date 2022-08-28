import requests, time, random, re
from bs4 import BeautifulSoup


def get_user(
    start: int = 1,
    end: int = 10
):
    """ Method to get user info
    """

    i = start

    while i <= end:

        try:

            url = f"https://funpay.com/users/{i}/"

            userpage = requests.get(
                url = url)

            if userpage.status_code == 200:

                soup = BeautifulSoup(userpage.text, "lxml")

                try:
                    username = soup.find(
                        name = "span", 
                        class_= "mr4").getText()

                except:
                    username = None 

                try:
                    usermoder = soup.find(
                        name = "span", 
                        class_ = "label label-success").getText()

                except:
                    usermoder = None

                try:
                    status = soup.find(
                        name = "span", 
                        class_ = "media-user-status").getText()
                    
                    userstatus = re.sub(" +", " ", status.strip())
                except:
                    userstatus = None

                try: 
                    userblock = soup.find(
                        name = "span", 
                        class_ = "label label-danger").getText()

                except:
                    userblock = None

            print(f"""
            userid = {i}
            username = {username}
            usermoder = {usermoder}
            userstatus = {userstatus}
            userblock = {userblock}""")

            

        except:
            print("Соединение не было установлено.")

        i += 1
        time.sleep(random.randint(1, 5))