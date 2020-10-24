from flask_restful import Resource
from flask import request
from models import db, Note, User
from functions.summary import sumit


class Summarizer(Resource):

    def post(self):
        header = request.headers['Authorization']
        json_data = request.get_json(force=True)

        if not header:
            return {"Messege" : "No api key!"}, 400
        else:
            user = User.query.filter_by(api_key=header).first()
            if user:
                note = Note( 
                    title = json_data['title'],
                    user_id = user.id,
                    note = json_data['note'],
                    retention= json_data['retention']
                )
                
                result = sumit(note.note, note.retention)
                # result = Note.serialize(result)
                return {"status": 'success', 'data': result}, 201
            else:
                return {"Messege" : "No user with that api key"}, 402