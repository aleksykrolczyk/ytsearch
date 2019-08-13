from ytsearch.blueprints.forms.controller import forms_bp
from ytsearch.blueprints.main.controller import main_bp


def init_blueprints(app):
    app.register_blueprint(forms_bp)
    app.register_blueprint(main_bp)
