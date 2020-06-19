from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!!"

@app.route("/nahid")
def test():
    return "Hello Nahid!!"

@app.route("/<string:name>")
def hello(name):
    return f"<h1>Hello, {name}!</h1>"
