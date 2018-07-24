from flask import Blueprint, render_template, redirect
import requests

gt = Blueprint('gitlab', __name__, url_prefix='/gitlab')

TOKEN = '3rya92YYvqjzxS9dJ3Ew'
GITLAB = 'http://192.168.0.100/api/v4/{route}?private_token={tk}'

@gt.route('')
def home():
	users = requests.get(GITLAB.format(tk=TOKEN, route='users'))
	projects = requests.get(GITLAB.format(tk=TOKEN, route='projects'))
	return render_template('gitlab.html', users=users.json(), projects=projects.json())


