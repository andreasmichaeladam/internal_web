#import function
from flask import Flask,redirect,url_for,render_template,request,session,jsonify,flash
from flask_sqlalchemy import SQLAlchemy
import logging

#define app
app = Flask(__name__)



''' import db
in cmd 
from internal_web.Idata import db
db.create_all()
'''
from .Idata import *

#import file
from .admin_page import admin_page
from internal_web import views

#Set config
app.secret_key='janganditebak'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///secure.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(admin_page, url_prefix="/admin")

db = SQLAlchemy(app)

if __name__ == "__main__":
	app.run(debug=True)
