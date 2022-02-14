import os
import json, urllib

from flask import Flask, render_template

import db

# create and configure the app
application = Flask(__name__, instance_relative_config=True)
application.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(application.instance_path, 'flaskr.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(application.instance_path)
except OSError:
    pass

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

if __name__ == "__main__":
    application.debug = False
    application.run()