import os

from dotenv import load_dotenv


load_dotenv()


BASE_URL = os.getenv("BASE_URL")
API_TOKEN = os.getenv("API_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL")