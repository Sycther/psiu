import os
import json, urllib

from flask import Flask, render_template
from butter_cms import ButterCMS

# FIXME Fallback onto previously loaded file

client = ButterCMS('857e1fbc8fccc396318e1c6bd4e023489dcc159f')

def loadJsonFile(url : str) -> str:
    f = urllib.request.urlopen(url)
    data = json.load(f)
    return data

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
    return render_template("brothers.html", content=loadJsonFile("https://drive.google.com/uc?id=1y1wkroIhPU56XrPR-_ePwlX-msqYpsOA"))

@application.route('/events')
def hello():
    return render_template("events.html", content=loadJsonFile("https://drive.google.com/uc?id=154Nx1RkquXmvy_w0zJPsxOlvlQ9xofO3"))

if __name__ == "__main__":
    application.debug = False
    application.run()