from flask import Blueprint
from flask_restful import Api
from resources.Register import Register
from resources.Note import Notes
from resources.Signin import Signin
from resources.User import Users
from resources.Search import NoteSearch, UserSearch
from resources.Summarize import Summarizer
from resources.Trade import MakeTrade


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Register, '/register')

api.add_resource(Signin, '/signin')

api.add_resource(Users, '/users')

api.add_resource(Notes, '/notes')

api.add_resource(Summarizer, '/notes/summarize')

api.add_resource(NoteSearch, '/notes/search/<search_term>')

api.add_resource(UserSearch, '/users/search/<search_term>')

api.add_resource(MakeTrade, '/trade')


