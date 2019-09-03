from flask import Blueprint, request, render_template, session, abort, redirect, url_for
from ui.forms.registration import  OwnerRegistrationForm
from ui.forms.login import OwnerLoginForm
from models.owners import Owner
from models import db
from flask_login import login_user, login_required, logout_user
import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()
from werkzeug.security import generate_password_hash, check_password_hash
blueprint = Blueprint(name='Owner', import_name='Owner',url_prefix='/owner',template_folder='ui/templates')

@blueprint.route('/register', methods=['GET','POST'])
def index():
    form = OwnerRegistrationForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        owner = Owner(name=form.name.data,email=form.email.data,password=generate_password_hash(form.password.data))
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for("Owner.thankyou"))
    return render_template('owner/register.html',form=form)

@blueprint.route('/thankyou')
def thankyou():
    return render_template('owner/thankyou.html')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out!!')
    return redirect(url_for('Owner.home'))

@blueprint.route('/login',methods=['GET','POST'])
def login():
    logger.info("Form recieved")
    form = OwnerLoginForm()
    logger.info("Form recieved")
    if form.validate_on_submit():
        logger.info("Form validated")
        owner = Owner.query.filter_by(email=form.email.data).first()
        logger.info(str(owner))
        check = owner.check_password(form.password.data)
        logger.info("{}".format(check))
        if owner.check_password(form.password.data) and owner is not None:
            logger.info(str(owner))
            login_user(owner)
            #flash("Logged in successfully!!")
            next = request.args.get('next')
            if next == None or not next[0] =='/':
                next = url_for('Owner.welcome')
            return redirect(next)

    return render_template('owner/login.html',form=form)


@blueprint.route('/welcome')
@login_required
def welcome():
    return render_template('owner/welcome.html')

@blueprint.route('/hello')
@login_required
def hello():
    return render_template('hello.html')


@blueprint.route('/',methods=['GET','POST'])
@login_required
def home():
    return render_template('owner/home.html')
