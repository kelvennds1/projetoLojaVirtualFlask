from flask import redirect, render_template, url_for, flash, request

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
