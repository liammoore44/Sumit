from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    password = db.Column(db.String())
    emailaddress = db.Column(db.String())
    api_key = db.Column(db.String())

    def __init__(self, api_key, firstname, lastname, emailaddress, password, username):
        self.api_key = api_key
        self.firstname = firstname
        self.lastname = lastname
        self.emailaddress = emailaddress
        self.password = password
        self.username = username

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'api_key' : self.api_key,
            'id' : self.id,
            'username' : self.username,
            'firstname' : self.firstname,
            'lastname' : self.lastname,
            'password' : self.password,
            'emailaddress' : self.emailaddress, 
        }

# class Note(db.Model):
#     __tablename__ = 'notes'

#     id = db.Column(db.Integer(), primary_key=True)
#     user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
#     title = db.Column(db.String())
#     note = db.Column(db.String())


#     def __init__(self, title, user_id, note, retention=None):
#         self.title = title
#         self.user_id = user_id
#         self.note = note
#         self.retention = retention

#     def __repr__(self):
#         return '<id {}>'.format(self.id)

#     def serialize(self):
#         return {
#             'title' : self.title,
#             'user_id' : self.user_id,
#             'id' : self.id,
#             'note' : self.note,
#             'retention': self.retention
#         }
class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    title = db.Column(db.String())
    note = db.Column(db.String())


    def __init__(self, title, user_id, note, retention=None):
        self.title = title
        self.user_id = user_id
        self.note = note
        self.retention = retention

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'title' : self.title,
            'user_id' : self.user_id,
            'id' : self.id,
            'note' : self.note,
            'retention': self.retention
        }

class TradeData:
    def __init__(self, symbol, qty, side, _type, time_in_force):
        self.symbol = symbol
        self.qty = qty
        self.side = side
        self._type = _type
        self.time_in_force = time_in_force

    # def __repr__(self):
    #     return '<id {}>'.format(self.id)

    def serialize(self):
        return {
        'symbol': self.symbol, 
        'qty': self.qty,
        'side': self.side,
        'type': self._type, 
        'time_in_force': self.time_in_force
        }