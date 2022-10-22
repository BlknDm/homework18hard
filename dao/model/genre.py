from marshmallow import Schema, fields
from setup_db import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Genre(db.Model):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
