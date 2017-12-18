from flask import Flask

app = Flask('flask-mpd')
@app.route("/")
def hello_world():
    return "Hello World"