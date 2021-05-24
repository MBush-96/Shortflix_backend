from flask_sqlalchemy import SQLAlchemy
import hashlib
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password    
        }

    def validate_pass(self, p):
        p = p.encode()
        z = hashlib.sha256(p).hexdigest()
        if self.password == z:
            return True

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    movie_src = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    movie_cover = db.Column(db.String, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'movie_src': self.movie_src,
            'rating': self.rating
        }

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'genre': self.genre
        }

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'rating': self.rating,
            'user_id': self.user_id
        }