import os
from connection import get_connection
from model import Contact

class Queries:
    def insert_contacts(institution):
        sql = """
              INSERT INTO contacts(first_name,last_name,phone_number)
              VALUES(%s, %s, %s)
              """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql,institution)
        return cursor.fetchall()
    
    def get_all_contact():
        sql = """
              SELECT * FROM contacts
              """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    def update_contact():
        sql = """
              UPDATE contacts
              SET first_name= %s, last_name= %s, phone_number= %s
              WHERE ID = %s
              """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    def delete_contact():
        sql = """
              DELETE contact WHERE id = %s
              """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()