from flask import render_template, request, Blueprint
from ytsearch.addons.scraper import get_videos
from flask_login import current_user

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@main_bp.route('/homepage')
def homepage():
    return render_template('homepage.html')


@main_bp.route('/query', methods=['GET'])
def query():
    query = request.args['query']
    if query in (None, ''):
        query = 'rick astley'
    videos = get_videos(query=query)

    if current_user.is_authenticated:
        current_user.add_query(query)
    return render_template('search.html', query=query, videos=videos)
