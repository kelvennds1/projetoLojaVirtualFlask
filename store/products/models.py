from enum import unique
from store import db


class Brands(db.Model):
    id=db.Column(db.Interger, primary_key=True)
    name=db.Column(db.String(30), nullable=False,unique=True)

class Category(db.Model):
    id=db.Column(db.Interger, primary_key=True)
    name=db.Column(db.String(30), nullable=False,unique=True)

db.create_all()