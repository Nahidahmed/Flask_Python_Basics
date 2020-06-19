# Flask_Python_Basics
Basics of Flask using Python


1. Setup Flask by following instruction on https://flask.palletsprojects.com/en/1.1.x/installation/
2. application.py
    This is the file when run with run will act as a web server. The contents of the files are:

              from flask import Flask

              app = Flask(__name__)

              @app.route("/")
              def index():
                  return "Hello World!!"

              @app.route("/nahid")
              def nahid():
                  return "Hello Nahid!!"


3. On the terminal, navigate to the folder which contains application.py and run the commands:

            a. Create environment: $ python3 -m venv venv
            b. Activate the environment: $ . venv/bin/activate
            c. Install Flask: $ pip install Flask
            d. Finally run the application.py: flask run (runs with debug mode off)
                    (This will start the web server and provide the url on which it is running)
            e. To run in dev mode: FLASK_ENV = development flask run 
