import pyodbc

from config.settings import (
    DB_SERVER,
    DB_DATABASE,
    DB_DRIVER,
    DB_USERNAME,
    DB_PASSWORD
)

if DB_USERNAME and DB_PASSWORD:

    connection_string = f"""
    DRIVER={{{DB_DRIVER}}};
    SERVER={DB_SERVER};
    DATABASE={DB_DATABASE};
    UID={DB_USERNAME};
    PWD={DB_PASSWORD};
    TrustServerCertificate=yes;
    """

else:

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