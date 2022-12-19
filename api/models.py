from api import db
from datetime import datetime
import string
import random


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    ingredients = db.Column(db.String(600), nullable=False)
    steps = db.Column(db.String(600), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    favorite = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Event %r>' % self.name

    def __init__(self, name, ingredients, steps, rating, favorite):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        if rating > 0 and rating <= 5:
            self.rating = rating
        else:
            self.rating = 1
        self.favorite = favorite
