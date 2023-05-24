import argparse
import os

from dotenv import load_dotenv

# Load environment variables before other imports to ensure
# database methods have required configuration
load_dotenv()

from db import insert
from app import app

def createDatabaseTable():
    print(f"Creating database tbl_shortened_urls at {os.environ.get('DB_HOST')} in schema {os.environ.get('DB_SCHEMA')}")
    sql = """
            CREATE TABLE IF NOT EXISTS tbl_shortened_urls(
                urlID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                hash VARCHAR(500) NOT NULL COMMENT "The hashed key appended to the shortened url",
                originalUrl TEXT NOT NULL COMMENT "The original URL that was shortened. Used for redirection when a user clicks the shortened version of the link",
                INDEX (hash)
            );
          """

    insert(sql, ())

    print(f"Database table tbl_shortened_urls created at {os.environ.get('DB_HOST')} in schema {os.environ.get('DB_SCHEMA')}")

def start():
    if __name__ == '__main__':
        app.run()

parser = argparse.ArgumentParser()
parser.add_argument('script', choices=['start', 'create-db'])
args = parser.parse_args()

if args.script == 'create-db':
    createDatabaseTable()
elif args.script == 'start':
    start()
else:
    print("Invalid script option")
