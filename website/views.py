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

@views.route('/2016')
@login_required
def yr2016():
    return render_template("yr2016.html", user=current_user)

@views.route('/2017')
@login_required
def yr2017():
    return render_template("yr2017.html", user=current_user)

@views.route('/2018')
@login_required
def yr2018():
    return render_template("yr2018.html", user=current_user)

@views.route('/2019')
@login_required
def yr2019():
    return render_template("yr2019.html", user=current_user)

@views.route('/2020')
@login_required
def yr2020():
    return render_template("yr2020.html", user=current_user)

@views.route('/2021')
@login_required
def yr2021():
    return render_template("yr2021.html", user=current_user)

@views.route('/2022')
@login_required
def yr2022():
    return render_template("yr2022.html", user=current_user)

@views.route('/2023')
@login_required
def yr2023():
    return render_template("yr2023.html", user=current_user)


