from flask import (Blueprint, render_template, request, redirect)
from . import models

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new_facts():
    return render_template('facts/new.html')

@bp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        submitter = request.form['name']
        fact = request.form['fact']
        
        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit() 
        return redirect('/facts')
    results = models.Fact.query.all()
    for result in results:
        print(result)
    return render_template('facts/index.html', facts=results)

