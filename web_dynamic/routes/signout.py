from flask import Blueprint, session, redirect, url_for

bp = Blueprint('signout', __name__)

@bp.route('/signout')
def signout():
    # Clear the user session
    session.clear()

    # Redirect to the home page
    return redirect(url_for('home.home'))
