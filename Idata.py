#Import function
from flask_sqlalchemy import SQLAlchemy
#from internal_web import db
#define db
db = SQLAlchemy()

#create database
class userdat(db.Model):
	_id = db.Column ("id", db.Integer , primary_key=True)
	name = db.Column ("name", db.String(100))
	telp = db.Column ("no hp", db.Integer)
	_date = db.Column ("Last login", db.DateTime())
	def __init__(self,name,telp,_date):
		self.name = name
		self.telp = telp
		self._date = _date

class user(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    role = db.Column("admin_role",db.Boolean)
    name = db.Column("name",db.String(32))
    _pass = db.Column("password",db.String(128))
    def __init__(self,role,name,_pass):
        self.role = role
        self.name = name
        self._pass = _pass