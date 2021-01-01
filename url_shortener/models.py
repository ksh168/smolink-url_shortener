import string
from datetime import datetime
from random import choices

from .extensions import db

#import secrets         #use if secrets.token method is used

URL_LEN = 3 # Length of generated url
 
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
        self.short_url = "None" # Giving temperory link
        db.session.add(self)
        db.session.commit()
        self.short_url = self.generate_short_link()

    def generate_short_link(self):#only self because it's the method of the class
        characters = string.digits + string.ascii_letters
        
        # Set short url to id of element 
        short_url = str(self.id).rjust(URL_LEN, '0')

        #short_url = secrets.token_hex(3)#another method to generate string(will generate 6 characters)
        
        return short_url
