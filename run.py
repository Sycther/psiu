from http.client import HTTPException
import os

from flask import Flask, render_template, send_file
from werkzeug.exceptions import HTTPException

import db
import json

# create and configure the app
application = Flask(__name__, instance_relative_config=True)
application.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(application.instance_path, 'flaskr.sqlite'),
)

@application.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@application.route('/brothers')
def our_brothers():
    return render_template("brothers.html", content=db.client.execute(db.queryBrothers))



@application.route('/events')
def hello():
    return render_template("events.html", content=db.client.execute(db.queryEvents))

@application.route('/contact')
def contact():
    return render_template("contact.html")

@application.errorhandler(Exception)
def err(e):
    if isinstance(e, HTTPException):
        return render_template("err.html",e=e)
        
    return render_template("err.html", e="500. Internal Server Error. ")


if __name__ == "__main__":
    application.debug = True
    application.run()