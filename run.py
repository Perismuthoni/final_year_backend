# Run a test server.
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



    