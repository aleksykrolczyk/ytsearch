from ytsearch.configs import db
from ytsearch.models import User
from .app import app


@app.shell_context_processor
def make_shell_context():
    ctx = {
        'db': db,
        'User': User,
    }

    return ctx
