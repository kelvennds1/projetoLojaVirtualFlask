from ast import Add
from flask import redirect, render_template, url_for, flash, request
from .forms import Addprodutos
from store import db, app
from store.products.models import Marcas, Categorias

@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marcas(name=getmarca)
        db.session.add(marca)
        flash(f'A marca {getmarca} foi cadastrada com sucesso!', 'success')
        db.session.commit()
        return redirect(url_for('addmarca'))
    return render_template('products/addmarca.html', marcas='marcas')


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == "POST":
        getcat = request.form.get('categoria')
        cat = Categorias(name=getcat)
        db.session.add(cat)
        flash(f'A categoria {getcat} foi cadastrada com sucesso!', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addmarca.html')


@app.route('/addproduto', methods=['GET', 'POST'])
def addproduto():
    marcas = Marcas.query.all()
    categorias = Categorias.query.all()
    form = Addprodutos(request.form)

    return render_template('products/addproduto.html', title= "Cadastrar Produtos", form=form, marcas=marcas, categorias=categorias)