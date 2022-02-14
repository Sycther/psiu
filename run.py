from http.client import HTTPException
from msilib.schema import AppId
import os

from flask import Flask, render_template, send_file
from werkzeug.exceptions import HTTPException

import db

# create and configure the app
application = Flask(__name__, instance_relative_config=True)
application.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(application.instance_path, 'flaskr.sqlite'),
)

# a simple page that says hello
@application.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@application.route('/brothers')
def our_brothers():
    return render_template("brothers.html", content=db.client.execute(db.queryBrothers))

@application.route('/events')
def hello():
    return render_template("events.html", content=db.client.execute(db.queryEvents))

@application.errorhandler(Exception)
def err(e):
    if isinstance(e, HTTPException):
        return render_template("err.html",e=e)
        
    return render_template("err.html", e="500. Internal Server Error. ")


if __name__ == "__main__":
    application.debug = False
    application.run()