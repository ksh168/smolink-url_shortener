from flask import Blueprint, render_template, request

from .extensions import db

from .models import Link

short = Blueprint('short', __name__)

#end points
#for actual short urls
@short.route('/<short_url>')
def redirect_to_url(short_url):
    pass


@short.route('/')
def index():
    return render_template('index.html')


#processing url and then showing user the url
@short.route('/add_link', methods = ['POST'])#will take POST requests
def add_link():
    original_url = request.form['original_url']
    link = Link(original_url = original_url)

    #add both short and original url into database
    db.session.add(link)
    db.session.commit()

    return render_template('link_added.html', 
        new_link = link.short_url, original_url = link.original_url)



#for statistics
@short.route('/stats')
def stats():
    pass


#error handling for rogue input
@short.errorhandler(404)
def page_not_found(e):
    return '', 404