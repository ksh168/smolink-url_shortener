from flask import Blueprint, render_template, request, redirect

from .extensions import db
from .models import Link
from .auth import requires_auth
from .utils import UrlValidator, generate_short_link


short = Blueprint('short', __name__)

# end points
# for actual short urls


@short.route('/<short_url>')
def redirect_to_url(short_url):
    # query the database
    # if not found return 404
    link = Link.query.filter_by(short_url=short_url).first_or_404()

    # each time a website is visited using genereated short_url, increment the counter
    link.visits = link.visits + 1
    # commit this to database
    db.session.commit()

    return redirect(link.original_url)


@short.route('/')
# @requires_auth
def index():
    return render_template('index.html')


# processing url and then showing user the url
@short.route('/add_link', methods=['POST'])  # will take POST requests
# @requires_auth
def add_link():
    original_url = request.form.get('original_url')
    custom_end = request.form.get('custom_end')      
    
    #start input validation
    if original_url is None:
        return "original_url field is required", 400

    if not UrlValidator.validate(original_url):
        return "Invalid url", 400
    
    #remove all spaces in custom_end
    custom_end = custom_end.replace(" ", "")

    if len(custom_end) > 64:
        return "custom_url is longer than 64 characters", 400      
    
    if len(original_url) > 512:
        return "original_url is longer than 512 characters", 400     

    #allow alphanumeric characters, -, _ only in custom_end
    regex = '[a-zA-z0-9_-]$'
    
    if((custom_end is not None) and (not re.search(regex, custom_end))):
        return "custom_url contains invalid characters", 400
    #end input validation     

    already_exists = Link.query.filter_by(short_url=custom_end).first()

    if already_exists and already_exists.short_url:
        return render_template('index.html',
                               custom_end=custom_end, original_url=original_url, message="custom end already exists")

    if custom_end:
        link = Link(original_url=original_url, short_url=custom_end)
    else:
        generated_end = generate_short_link(Link)
        link = Link(original_url=original_url, short_url=generated_end)

    db.session.add(link)
    try:
        db.session.commit()
    except:
        return "couldn't add to database", 500

    return render_template('link_added.html',
                           new_link=link.short_url, original_url=link.original_url)


# for statistics
@short.route('/stats')
@requires_auth
def stats():
    links = Link.query.all()

    return render_template('stats.html', links=links)


# error handling for rogue input
@short.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#for individual stats
@short.route('/<short_url>/stats')
def individual_stats(short_url):
    # links = Link.query.all()
    links = Link.query.filter_by(short_url=short_url).all()

    return render_template('stats.html', links=links)
