from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from .models import Company
import requests
from sqlalchemy import func, desc
from . import db, movie_api_key

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    company_name = request.form.get('company_name')
    company_number = request.form.get('company_number')
    company_email = request.form.get('company_email')
    company_address = request.form.get('company_address')
    if len(company_name) == 0 or len(company_number) == 0 or len(company_email) == 0 or len(company_address) == 0:
        return render_template('index.html')
    new_company = Company(company=company_name, email=company_email, phone_number=company_number, address=company_address)
    db.session.add(new_company)
    db.session.commit()
    thanks = "Thank You For Adding a New Record"
    
    return render_template('index.html', thanks=thanks)

@main.route('/list', methods=['GET'])    
def list():
    companies=Company.query.all()
    return render_template('list.html', companies=companies)
    
@main.route('/list/<phone_number>', methods=['GET', 'POST'])
def record(phone_number):
    info = Company.query.filter_by(phone_number=phone_number).first()
    if request.method == 'GET':
        return render_template('record.html', info=info)
    user_input = request.form['action']
    if user_input == 'update':
        print("hello")
        info.company = request.form.get('company_name')
        info.phone_number = request.form.get('company_number')
        info.email = request.form.get('company_email')
        info.address = request.form.get('company_address')
        db.session.commit()
        return redirect(f"/list/{info.phone_number}")
    elif user_input == 'delete':
        db.session.delete(info)
        db.commit()
        return render_template('list.html')
    
