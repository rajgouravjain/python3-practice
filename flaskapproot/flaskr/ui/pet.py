from flask import Blueprint, render_template, session, abort, redirect, url_for
from ui.forms.registration import  PetRegistrationForm
from models.pets import Pet
from models import db

blueprint = Blueprint(name='Pet', import_name='Pet',url_prefix='/pet',template_folder='ui/templates')


@blueprint.route('/', methods=['GET','POST'])
def index():
    form = PetRegistrationForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['breed'] = form.breed.data
        pet = Pet(name=form.name.data,breed=form.breed.data)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for("Pet.thankyou"))
    return render_template('pet/home.html',form=form)

@blueprint.route('/thankyou')
def thankyou():
    return render_template('pet/thankyou.html')
