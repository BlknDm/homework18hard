from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema, Director

from container import director_service


director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        try:
            directors = director_service.get_all()
            return directors_schema.dump(directors), 200
        except Exception as e:
            return e, 404


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director)
        except Exception as e:
            return e, 404
