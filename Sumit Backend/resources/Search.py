from flask_restful import Resource
from flask import request
from models import db, User, Note


class NoteSearch(Resource):
    
    def get(self, search_term):
        result = []
        notes = Note.query.filter(Note.title.like('%'+search_term+'%')).all()
        for note in notes:
            result.append(Note.serialize(note)) 

        if len(result) > 0:
            return {"status": "succes", "data": result}, 201
        else:
            return {"message": "No Notes Found"}, 201

class UserSearch(Resource):
    
    def get(self, search_term):
        result = []
        users = User.query.filter(User.username.like('%'+search_term+'%')).all()
        for user in users:
            result.append(User.serialize(user)) 

        if len(result) > 0:
            return {"status": "succes", "data": result}, 201
        else:
            return {"message": "No Users Found"}, 201









