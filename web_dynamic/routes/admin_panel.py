from flask import Blueprint, redirect, url_for, render_template, session

bp = Blueprint('admin_panel', __name__)

@bp.route('/admin', methods=['GET'])
def admin_panel():
    # Check if the user is authenticated as an admin
    if 'email' in session and session['email'] == 'admin@frb.com':
        return render_template('admin_panel.html')
    else:
        return redirect(url_for('signin'))
