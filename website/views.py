from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/web-design')
@login_required
def webdesign():
    pass

@views.route('/software-tech')
@login_required
def software_tech():
    pass

@views.route('/investing-finance')
@login_required
def investing_finance():
    pass

@views.route('business-admin')
@login_required
def business_admin():
    pass

@views.route('/interactive-design')
@login_required
def interactive_design():
    pass

