import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hallo, Herzlich Willkommen!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/Bechtle')
def hello():
    return 'Bechtle GmbH IT-Systemhaus Nuernberg :)'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
