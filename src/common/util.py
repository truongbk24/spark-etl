import os
from dotenv import load_dotenv

load_dotenv()

RDBMS_USER= os.environ['RDBMS_USER']
RDBMS_PASSWORD= os.environ['RDBMS_PASSWORD']
RDBMS_DRIVER_NAME= os.environ['RDBMS_DRIVER_NAME']
RDBMS_URL= os.environ['RDBMS_URL']