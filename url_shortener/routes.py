from flask import Blueprint, render_template, request, redirect

from .extensions import db
from .models import Link
from .auth import requires_auth
from .utils import UrlValidator


short = Blueprint('short', __name__)

#end points
#for actual short urls
@short.route('/<short_url>')
def redirect_to_url(short_url):
    #query the database
    link = Link.query.filter_by(short_url = short_url).first_or_404()#if not found return 404

    #each time a website is visited using genereated short_url, increment the counter
    link.visits = link.visits + 1
    #commit this to database
    db.session.commit()

    return redirect(link.original_url)


@short.route('/')
#@requires_auth
def index():
    return render_template('index.html')


#processing url and then showing user the url
@short.route('/add_link', methods = ['POST'])#will take POST requests
#@requires_auth
def add_link():
    original_url = request.form['original_url']
    custom_end = request.form['custom_end']

    if UrlValidator.validate(original_url) is None:
        return "Invalid url", 400

    link = Link(original_url = original_url, short_url = custom_end)

    #add both short and original url into database
    db.session.add(link)
    db.session.commit()

    return render_template('link_added.html', 
        new_link = link.short_url, original_url = link.original_url)



#for statistics
@short.route('/stats')
@requires_auth
def stats():
    links = Link.query.all()

    return render_template('stats.html', links = links)


#error handling for rogue input
@short.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404