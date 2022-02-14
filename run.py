import os
import json, urllib

from flask import Flask, render_template

import db

def createApp() -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/', methods=['GET'])
    def home():
        return render_template("home.html")

    @app.route('/brothers')
    def our_brothers():
        return render_template("brothers.html", content=db.client.execute(db.queryBrothers))

    @app.route('/events')
    def hello():
        return render_template("events.html", content=db.client.execute(db.queryEvents))

    return app

if __name__ == "__main__":
    application = createApp()
    application.debug = False
    application.run()