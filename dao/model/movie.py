from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from dao.model.director import DirectorSchema
from dao.model.genre import GenreSchema
from setup_db import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Movie(db.Model):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    director_id = Column(Integer, ForeignKey('director.id'))
    genre = relationship('Genre')
    director = relationship('Director')


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre = fields.Pluck(field_name='name', nested=GenreSchema)
    director = fields.Pluck(field_name='name', nested=DirectorSchema)
