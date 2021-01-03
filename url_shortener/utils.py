import re
from random import choices
import string

class UrlValidator(object):
    pattern = re.compile(
        "(?:http|ftp)[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

    @classmethod
    def validate(cls, url_string):
        return cls.pattern.match(url_string)


def generate_short_link(Link):

    def generator():
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=6))
        return short_url

    already_exists = True

    while already_exists:
        short_url = generator()
        res = Link.query.filter_by(short_url = short_url).first()
        if not res:
            already_exists = False
    
    return short_url