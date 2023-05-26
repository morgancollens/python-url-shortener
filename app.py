from hashlib import sha256
from flask import Flask, render_template, request, Response, abort, send_from_directory
from db import insert, select
import validators


app = Flask(__name__)

# A generic method designed to handle error responses back to the client.
def handleError(httpStatus, errorMessage):
    status = httpStatus or 500
    message = errorMessage or "Internal Server Error"
    return abort(status, message)

# Base route that returns a simple form to the user to enter
# their original url
@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')

# Simple route to return a favicon and prevent the app from throwing an error when serving pages
@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/x-icon')

# Endpoint that will accept the original URL, shorten it and persist the
# original endpoint in our database.
@app.route('/submit', methods=['POST'])
def submit():
    url = request.form.get('url')

    if validators.url(url):
        sql = """
                INSERT INTO tbl_shortened_urls(originalUrl, hash)
                VALUES(%s, %s)
            """

        baseUrl = "http://localhost:5000/"
        urlHash = sha256(str(url).encode()).hexdigest()
        shortenedUrl = f"{baseUrl}{urlHash}"

        insert(sql, (url, urlHash))

        return render_template('response.html', url=shortenedUrl)
    else:
        return render_template('form.html', error="The link you provided is not a valid URL. Please try another link.")



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

    if len(data) != 0:
        originalUrl = data[0][0]
        response = Response(status=302)
        response.headers["Location"] = originalUrl
        return response
    else:
        return handleError(404, "We could not locate an associated URL. Sorry!")



