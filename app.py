#!/usr/bin/python3

from flask import Flask, render_template
from blueprints.docker import docker

app = Flask(__name__)
app.register_blueprint(docker)

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)
