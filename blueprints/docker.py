from flask import Blueprint, render_template

docker = Blueprint('docker', __name__, url_prefix='/docker')

@docker.route('')
def home():
    return render_template('docker.html')
