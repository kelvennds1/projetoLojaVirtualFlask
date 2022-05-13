import email
from turtle import title
from flask import render_template, session, request, redirect, url_for, flash

from store import app, db, bcrypt
from .forms import LoginForm, RegistrationForm
from .models import User    
import os

#Index
@app.route('/home')
def home():
    return render_template('admin/index.html', title = 'Pagina Administrativa')

#Form Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name = form.name.data, username = form.username.data, email = form.email.data,
                    password = hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.name.data} o registro foi efetuado com sucesso. Obrigado!', 'success')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Pagina de registro")

#Form Login

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user= User.query.filter_by(email=form.email.data).first()
    form = LoginForm(request.form)
    return render_template('admin/login.html', form = form, title = 'Pagina de Login')