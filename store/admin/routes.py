import email
from turtle import title
from flask import render_template, session, request, redirect, url_for, flash

from store import app, db, bcrypt
from .forms import RegistrationForm
from .models import User    
import os

#Index
@app.route('/home')
def home():
    return "Seja bem vindo!"

#Form Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name = form.name.data, username = form.username.data, email = form.email.data,
                    password = hash_password)
        db.session.add(user)
        flash('Registro efetuado com sucesso. Obrigado!')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Pagina de registro")


