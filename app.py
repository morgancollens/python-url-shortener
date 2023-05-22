from flask import Flask, render_template, request, Response

app = Flask(__name__)

# Base route that returns a simple form to the user to enter
# their original url
@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')


if __name__ == '__main__':
    app.run()