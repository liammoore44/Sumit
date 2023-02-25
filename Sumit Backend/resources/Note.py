from flask_restful import Resource
from flask import request
from models import db, User, Note


class Notes(Resource):

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
                )
                db.session.add(note) 
                db.session.commit()

                result = Note.serialize(note)
                return {"status": 'success', 'data': result}, 201
            else:
                return {"Messege" : "No user with that api key"}, 402

    def get(self):
        # print('hello')
        result = []
        # json_data = request.get_json(force=True)
        header = request.headers['Authorization']

        if not header:
            return {"Messege" : "No api key!"}, 400
        else:
            user = User.query.filter_by(api_key=header).first()
            if user:
                notes = Note.query.filter_by(user_id=user.id).all()
                for note in notes:
                    result.append(Note.serialize(note))


            return {"status": 'success', 'data': result}, 201