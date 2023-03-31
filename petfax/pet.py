from flask import ( Blueprint, render_template )
import json

bp = Blueprint('pet', __name__, url_prefix="/pets")
pets = json.load(open('pets.json'))
print(pets)

@bp.route('/')
def index ():
    return render_template ('index.html', pets=pets)

@bp.route('/<int:id>')
def show (id):
    selected_pet = pets[int(id) -1]
    return render_template ('show.html', pet = selected_pet)




