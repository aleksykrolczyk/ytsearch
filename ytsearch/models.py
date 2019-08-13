from .configs import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __repr_(self):
        return f'<User {self.id} -- {self.username}>'

    def create_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
