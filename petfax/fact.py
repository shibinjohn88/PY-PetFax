from flask import (Blueprint, render_template)

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new_facts():
    return render_template('/new.html')