from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads
from werkzeug.utils import secure_filename
import os

#import Database to uploads
basedir=os.path.abspath(os.path.dirname(__file__))


#Create App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mystore.db'
app.config['SECRET_KEY'] = 'aasfesqfagasegaeg'
db = SQLAlchemy(app)

#Selecting dir for photos
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, (photos))  
app.config["MAX_CONTENT_LENGTH"] = 120 * 1024 * 1024


#Crypting passwords
bcrypt = Bcrypt(app)

#Import routes
from store.admin import routes
from store.products import routes