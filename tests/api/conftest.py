import os
from dotenv import load_dotenv

load_dotenv()
base_url = "https://api.litres.ru/foundation/api"
email = os.getenv('USER_EMAIL')
password = os.getenv('USER_PASSWORD')
invalid_password = os.getenv('UNREGISTERED_USER_PASSWORD')