import jenkins
from flask import Blueprint, render_template, redirect

jk = Blueprint('jk', __name__, url_prefix='/jenkins')
jc = jenkins.Jenkins('http://192.168.0.200:8080', username='admin', password='4linux')

@jk.route('')
def home():
	for job in jc.get_jobs():
		if job['name'] == 'pipeline':
			pipeline = job
			break
	else:
		pipeline = {'name' : 'Nenhum job encontrado'}
	if pipeline['color'] == 'blue':
		pipeline['color'] = 'Sucesso'
	elif pipeline['color'] == 'red':
		pipeline['color'] = 'Falha'
	else:
		pipeline['color'] = "Unknow"

	#pipeline['color'] = 'Construiu' if pipeline['color'] == 'blue' else 'Falhou'
	return render_template('jenkins.html', job=job)

