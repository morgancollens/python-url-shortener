import argparse
import os

from dotenv import load_dotenv

# Load environment variables before other imports to ensure
# database methods have required configuration
load_dotenv()

from db import insert, select
from app import app

db_schema = os.environ.get('DB_SCHEMA')
db_table = "tbl_shortened_urls"

def dropDatabaseTable():
    print(f"Dropping database table {db_table}...")

    sql = """
            DROP TABLE {}.{}
          """.format(db_schema, db_table)

    insert(sql)

    print(f"Dropped database table {db_table} successfully.")

def createSchema():
    print(f"Creating schema {db_schema} at {os.environ.get('DB_HOST')}...")

    selectSql = """
                    SHOW DATABASES LIKE "{}"
                """.format(db_schema)

    data = select(selectSql)

    if len(data) == 0:
        insertSql = """
                        CREATE DATABASE `{}`
                    """.format(db_schema)

        insert(insertSql)


    print(f"Schema {db_schema} at {os.environ.get('DB_HOST')} was successfully created.")


def createDatabaseTable():
    print(f"Creating database tbl_shortened_urls at {os.environ.get('DB_HOST')} in schema {db_schema}")
    sql = """
            CREATE TABLE IF NOT EXISTS {}.{}(
                urlID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                hash VARCHAR(500) NOT NULL COMMENT "The hashed key appended to the shortened url",
                originalUrl TEXT NOT NULL COMMENT "The original URL that was shortened. Used for redirection when a user clicks the shortened version of the link",
                INDEX (hash)
            );
          """.format(db_schema, db_table)

    insert(sql)

    print(f"Database table tbl_shortened_urls created at {os.environ.get('DB_HOST')} in schema {db_schema}")

def start():
        app.run()

parser = argparse.ArgumentParser()
parser.add_argument('script', choices=['start', 'create-db', 'refresh-db'])
args = parser.parse_args()

if __name__ == '__main__':
    if args.script == 'create-db':
        createSchema()
        createDatabaseTable()
    elif args.script == 'refresh-db':
        dropDatabaseTable()
        createDatabaseTable()
    elif args.script == 'start':
        start()
    else:
        print("Invalid script option")
