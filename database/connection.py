import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
driver = os.getenv("DB_DRIVER")

connection_string = f"""
DRIVER={{{driver}}};
SERVER={server};
DATABASE={database};
Trusted_Connection=yes;
TrustServerCertificate=yes;
"""

def get_connection():
    return pyodbc.connect(connection_string)