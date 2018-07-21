import docker
from flask import Blueprint, render_template, redirect

pocker = Blueprint('pocker', __name__, url_prefix='/docker')

#dc = docker.DockerClient('tcp://192.168.0.200:2376')

@pocker.route('')
def home():
	c = dc.containers.get('flask-app')
	return render_template('docker.html', container=c)

@pocker.route('/start')
def start():
	c = dc.containers.get('flask-app')
	c.start()
	return redirect('/docker')

@pocker.route('/stop')
def stop():
	c = dc.containers.get('flask-app')
	c.stop()
	return redirect('/docker')