import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USER_EMAIL = os.getenv('USER_EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    BASE_URL = os.getenv('BASE_URL')