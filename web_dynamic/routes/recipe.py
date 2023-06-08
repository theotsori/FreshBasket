from flask import Blueprint, render_template

bp = Blueprint('recipe', __name__)

@bp.route('/recipe')
def recipe():
    # checks items on the cart
    cart_count = get_cart_count()
    return render_template('recipe.html', cart_count=cart_count)
