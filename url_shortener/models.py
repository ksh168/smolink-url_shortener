import string
from datetime import datetime

from random import choices

from .extensions import db

class Link(db.model):
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.String(512))#upto 512 characters in riginal url
    
    short_url = db.Column(db.String(3), unique = True)#no. of characters in the custom url is 3
    #to track no of visits
    visits = db.Column(db.Integer, default = 0)
    #date the url was created
    date_created = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, **kwargs):
        #kwargs->keyword arguments
        super.__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):#only self because it's the method of the class
        characters = string.digits + string.ascii_letters
        #join returns list and so it takes individual elements and join them together in one string
        short_url = ''.join(choices(characters, k = 3))#k->no. of characters in short url

        #make sure that it's unique 
        link = self.query.filter_by(short_url = short_url).first()

        #check for uniqueness
        if link:
            #if the 3 charactes generated already exist, recursively call to generate a new url
            return self.generate_short_link()
        
        return short_url