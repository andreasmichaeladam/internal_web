#import function
from internal_web import *
from flask import Flask,redirect,url_for,render_template,request,session,jsonify,flash
import requests

#error handler
@app.errorhandler(404)
def not_found(e):
	return render_template("404.html"),404

@app.route("/")
def home():
	return redirect(url_for('admin_page.login'))