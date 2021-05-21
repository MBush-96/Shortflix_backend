import os
from dotenv import load_dotenv
from flask import Flask, request
import sqlalchemy
import models

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
models.db.init_app(app)

@app.route('/', methods=["GET"])
def connect():
    return 'ok'

if __name__ == '__main__':
    port = os.environ.get('PORT') or 5000
    app.run(port=port, debug=True)