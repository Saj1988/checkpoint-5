from flask import *
import datetime
import sqlite3

def get_name(phone):
    conn = sqlite3.connect("phone.db")
    cur = conn.cursor()
   
    cur.execute(f"SELECT name FROM phonelist WHERE phone = '{phone}';")
    rows = cur.fetchall()
    cur.close()
    return rows[0][0]
def get_phone(name):
    conn = sqlite3.connect("phone.db")
    cur = conn.cursor()    
    cur.execute(f"SELECT phone FROM phonelist WHERE name = '{name}';")
    rows = cur.fetchall()
    cur.close()
    return rows[0][0]

