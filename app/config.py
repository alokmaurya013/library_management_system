import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'  #Using SQLite for local dev
    SQLALCHEMY_TRACK_MODIFICATIONS = False
