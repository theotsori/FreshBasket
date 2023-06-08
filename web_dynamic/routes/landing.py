from flask import Blueprint, render_template

bp = Blueprint('landing', __name__)

@bp.route('/')
def landing():
    return render_template('landing.html')
