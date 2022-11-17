import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')


wrong_email = "shevsyi"
wrong_password = 'неверный пароль'