from flask import redirect, render_template, url_for, flash, request

from store import db, app

@app.route('/brandadd', methods=["GET", "POST"])
def brandadd():
    return render_template('/products/brandadd.hmtl')
