import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST","db-1"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD", '12345678'),
        database=os.getenv("DB_NAME")
    )
    return connection       

    