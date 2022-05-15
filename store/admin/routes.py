import email
from turtle import title
from flask import render_template, session, request, redirect, url_for, flash
from store.products.models import Addproduto
from store import app, db, bcrypt
from .forms import LoginForm, RegistrationForm
from .models import User    
import os

#Admin page
@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Por favor fazer login!', 'success')
        return redirect(url_for('login'))
    produtos = Addproduto.query.all()

    return render_template('admin/index.html', title = 'Pagina Administrativa', produtos = produtos)

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
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="Pagina de registro")

#Form Login

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'{form.email.data} o login foi efetuado com sucesso. Obrigado!', 'success')
            return redirect(request.args.get('next')or url_for('admin'))
        else:
            flash(f'Usuario ou Senha incorretos', 'danger')
    form = LoginForm(request.form)
    return render_template('admin/login.html', form = form, title = 'Pagina de Login')
