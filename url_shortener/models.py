import string
from datetime import datetime

from random import choices

from .extensions import db

#import secrets         #use if secrets.token method is used

class Link(db.Model):
    id = db.Column(db.Integer, primary_key = True)#it's primary key
    #id = db.Column(db.Integer)

    original_url = db.Column(db.String(512))#upto 512 characters in original url
    
    short_url = db.Column(db.String(6), unique = True)#no. of characters in the custom url is 6
    #short_url = db.Column(db.String(6), primary_key = True)

    #to track no of visits
    visits = db.Column(db.Integer, default = 0)
    #date the url was created
    date_created = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, **kwargs):
        #kwargs->keyword arguments
        super().__init__(**kwargs)
        if not self.short_url:
            self.short_url = self.generate_short_link()

    def generate_short_link(self):#only self because it's the method of the class
        characters = string.digits + string.ascii_letters
        
        #join returns list and so it takes individual elements and join them together in one string
        short_url = ''.join(choices(characters, k = 6))#k->no. of characters in short url

        #short_url = secrets.token_hex(3)#another method to generate string(will generate 6 characters)

        #make sure that it's unique 
        link = self.query.filter_by(short_url = short_url).first()

        #check for uniqueness
        if link:
            #if the 6 charactes generated already exist, recursively call to generate a new url
            return self.generate_short_link()
        
        return short_url
