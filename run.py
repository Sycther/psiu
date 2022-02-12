import os
import json, urllib

from flask import Flask, render_template

def loadJsonFile(url, static=False):
    if(static):
        f = open(url)
    else:
        f = urllib.request.urlopen(url)
    return json.load(f)

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
    return render_template("brothers.html", content=loadJsonFile("static/our-brothers.json", True)) #content=loadJsonFile("https://our-brothers.s3.amazonaws.com/our-brothers.json",))

@application.route('/events')
def hello():
    return render_template("events.html", content=loadJsonFile("static/events.json", True))

if __name__ == "__main__":
    application.debug = True
    application.run()