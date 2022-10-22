from marshmallow import Schema, fields
from setup_db import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Director(db.Model):
    __tablename__ = 'director'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
