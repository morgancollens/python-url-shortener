import os
import mysql.connector

db = mysql.connector.connect(
  host=os.environ.get('DB_HOST'),
  user=os.environ.get('DB_USER'),
  password=os.environ.get('DB_PASSWORD'),
)

def getCursor():
    return db.cursor()

def insert(sql, values=()):
    cursor = getCursor()
    cursor.execute(sql, values)

    db.commit()

    insertId = cursor.lastrowid

    cursor.close()

    return insertId


def select(sql, values=()):
    cursor = getCursor()
    cursor.execute(sql, values)

    result = cursor.fetchall()

    cursor.close()

    return result

