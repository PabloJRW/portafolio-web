from flask import render_template, request
from app.main import main_bp


# Página principal
@main_bp.route('/')
def index():
    return render_template('main/index.html')



# Proyecto 1
@main_bp.route('/proyecto1')
def proyecto_1():
    return render_template('proyectos/api-rest.html')