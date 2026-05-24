import pyodbc

from config.settings import (
    DB_SERVER,
    DB_DATABASE,
    DB_DRIVER
)

connection_string = f"""
DRIVER={{{DB_DRIVER}}};
SERVER={DB_SERVER};
DATABASE={DB_DATABASE};
Trusted_Connection=yes;
TrustServerCertificate=yes;
"""


def get_connection():

    return pyodbc.connect(
        connection_string
    )