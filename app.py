#!/usr/bin/python3

from flask import Flask, render_template
from blueprints.pocker import pocker
from blueprints.jk import jk

app = Flask(__name__)
app.register_blueprint(pocker)
app.register_blueprint(jk)

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)