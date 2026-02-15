import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    DATABASE_NAME = 'nexus_db'
    JWT_SECRET = os.getenv('JWT_SECRET', 'supersecretkey')
    JWT_EXPIRATION_HOURS = 24
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASS = os.getenv('EMAIL_PASS')
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    STARTER_TOKENS = 3
    MAX_LOGIN_ATTEMPTS = 5
    OTP_EXPIRY_MINUTES = 5
    MAX_OTP_ATTEMPTS = 3
