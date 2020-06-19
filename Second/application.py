from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Learn Web Programming with Phython and JS with CS50 Online course!"
    return render_template("index.html",headline=headline)
