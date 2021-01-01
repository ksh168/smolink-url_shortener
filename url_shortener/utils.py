import re

class UrlValidator(object):
    pattern = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

    @classmethod
    def validate(cls, url_string):
        return cls.pattern.match(url_string)