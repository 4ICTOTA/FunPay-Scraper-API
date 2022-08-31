import os
from dotenv import load_dotenv


# init .env parameters
load_dotenv()

PROJECT_HOST = os.getenv(
    key = "PROJECT_HOST")

PROJECT_PORT = os.getenv(
    key = "PROJECT_PORT")

PROJECT_NAME = os.getenv(
    key = "PROJECT_NAME")