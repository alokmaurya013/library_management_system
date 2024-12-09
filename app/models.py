from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)