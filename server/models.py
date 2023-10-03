from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, Integer, String, Float
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    magnitude = Column(Float, nullable=False)
    year = Column(Integer, nullable=False)

    serialize_only = ("id", "location", "magnitude", "year")
