from flask_restful import Resource


class Users(Resource):
    def get(self):
        return {"message": "Hello, World!"}


# from flask_restful import Resource
# from models import db, User, Note


# class Users(Resource):
#     def get(self):
#         user = User.query.filter_by(api_key=api_key).first()

#         if user:
#             return User.serialize(user)