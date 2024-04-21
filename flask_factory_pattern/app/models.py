from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from datetime import datetime


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

@dataclass
class ExampleModel(Base):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(255))
    description: str = db.Column(db.String(255))
    