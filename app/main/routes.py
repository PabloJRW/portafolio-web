from flask import render_template, request
from app.main import main_bp


@main_bp.route('/')
def index():
    return render_template('index.html')