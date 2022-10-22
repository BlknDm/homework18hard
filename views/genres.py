from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema, Genre

from container import genre_service


genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        try:
            genres = genre_service.get_all()
            return genres_schema.dump(genres), 200
        except Exception as e:
            return e, 404


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre)
               # return 'No such movie', 200
            #return genre_schema.dump(genre), 200
        except Exception as e:
            return e, 404
