from flask import render_template, request, Blueprint
from ytsearch.addons.scraper import get_videos

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@main_bp.route('/homepage')
def homepage():
    return render_template('homepage.html')


@main_bp.route('/query', methods=['GET'])
def query():
    query = request.args['query']
    videos = get_videos(query=query)
    return render_template('search.html', query=query, videos=videos)


@main_bp.route('/query_mock', methods=['GET'])
def query_mock():
    query = request.args['query']

    video = {
        'id': 'dQw4w9WgXcQ',
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'img_url': 'https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg',
        'title': 'Rick Astley - Never Gonna Give You Up'
    }

    videos = [video] * 6

    return render_template('search.html', query=query, videos=videos)
