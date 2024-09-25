from dotenv import load_dotenv
import os

load_dotenv('/opt/airflow/.env')

VAULT_ADDR = os.getenv('VAULT_ADDR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')

GMAIL_USER = os.getenv('GMAIL_USER')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
SEND_EMAIL = os.getenv('SEND_EMAIL')