from dotenv import load_dotenv

# Load environment variables before other imports to ensure
# database methods have required configuration
load_dotenv()

from hashlib import sha256
from flask import Flask, render_template, request, Response
from db import insert, select


app = Flask(__name__)

# Base route that returns a simple form to the user to enter
# their original url
@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')

# Endpoint that will accept the original URL, shorten it and persist the
# original endpoint in our database.
@app.route('/submit', methods=['POST'])
def submit():
    url = request.form.get('url')

    sql = """
            INSERT INTO tbl_shortened_urls(originalUrl, hash)
            VALUES(%s, %s)
          """

    baseUrl = "http://localhost:5000/"
    urlHash = sha256(str(url).encode()).hexdigest()
    shortenedUrl = f"{baseUrl}{urlHash}"

    insert(sql, (url, urlHash))

    return "Your shortened url is " + shortenedUrl

# Endpoint that will accept a shortened url, and use the hash to retrive the
# original url from our database.
@app.route('/<hash>', methods=['GET'])
def redirect(hash):
    sql = """
            SELECT originalURL FROM tbl_shortened_urls
            WHERE hash = %s
            LIMIT 1
          """

    data = select(sql, (hash,))
    originalUrl = data[0][0]

    response = Response(status=302)
    response.headers["Location"] = originalUrl
    return response



if __name__ == '__main__':
    app.run()