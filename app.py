import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Azurefreak!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/kevin')
def hello():
    return 'I am a Kevin'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
