from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#Create App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mystore.db'
app.config['SECRET_KEY'] = 'kelvendslite1'
db = SQLAlchemy(app)

#Crypting passwords
bcrypt = Bcrypt(app)

#Import routes
from store.admin import routes
from store.products import routes