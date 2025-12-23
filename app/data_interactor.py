from dotenv import load_dotenv
import os
from mysql import connector
from config import connection

class Queries:
    def insert_contants(institution):
        sql = """INSERT INTO contacts(first_name,last_name,phone_number)
        VALUES(%s, %s, %s)
        """
        cursor = connection.cursor
        cursor.execute(sql,institution)
        return cursor.fetchall()

    query2="SELECT * FROM contacts"
    query3=
    query4="DELETE contact" \
    "WHERE id = %s"