import string
from datetime import datetime

from random import choices

from .extensions import db

# import secrets         #use if secrets.token method is used


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    original_url = db.Column(db.String(512))  # upto 512 characters
    short_url = db.Column(db.String(6), unique=True)  # upto 6 characters
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "<Link %r, %r, %r>" % (self.id, self.original_url, self.short_url)
