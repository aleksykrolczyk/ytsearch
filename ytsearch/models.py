from .configs import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    joined = db.Column(db.DateTime, default=func.now())
    queries = db.relationship('Query')

    def __repr_(self):
        return f'<User {self.id} -- {self.username}>'

    def create_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add_query(self, query):
        query = Query(user_id=self.id, content=query)
        db.session.add(query)
        db.session.commit()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Query(db.Model):
    __tablename__ = 'queries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.String)
    date = db.Column(db.DateTime, default=func.now())
