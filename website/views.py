from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db 
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/2015')
@login_required
def yr2015():
    return render_template("yr2015.html", user=current_user)




