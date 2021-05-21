import os
from types import MethodDescriptorType
from dotenv import load_dotenv
from flask import Flask, request
import sqlalchemy
import models

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
models.db.init_app(app)

@app.route('/', methods=["GET"])
def connect():
    return 'ok'

@app.route('/users/signup', methods=['POST'])
def signup():
    user = models.User(
        username = request.json["username"],
        email = request.json["email"],
        password = request.json["password"]
    )

    models.db.session.add(user)
    models.db.session.commit()

    return {
        'user': user.to_json()
    }

@app.route('/users/login', methods=['POST'])
def login():
    user = models.User.query.filter_by(email=request.json["email"]).first()

    if user.password == request.json["password"]:
        return {
            'user': user.to_json()
        }
    return { 'Login': 'Unauthorized'}

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = models.User.query.filter_by(id=id).first()

    user.password = request.json["password"]

    models.db.session.add(user)
    models.db.session.commit()

    return {
        'updated': user.to_json()
    }

@app.route('/movies/create', methods=['POST'])
def create_movie():
    movie = models.Movie(
        title = request.json["title"],
        description = request.json["description"],
        movie_src = request.json["movie_src"],
        rating = request.json["rating"]
    )

    models.db.session.add(movie)
    models.db.session.commit()

    return {
        'Created Movie': movie.to_json()
    }

@app.route('/movies/<int:movie_id>', methods=['GET', 'PUT', 'DELETE'])
def get_movie(movie_id):
    movie = models.Movie.query.filter_by(id=movie_id).first()
    if request.method == 'GET':
        return {
            'Movie': movie.to_json()
        }
    elif request.method == 'PUT':
        movie.title = request.json["title"]
        movie.description = request.json["description"]
        
        models.db.session.add(movie)
        models.db.session.commit()
        return { 
            movie.to_json ()
        }
    elif request.method == 'DELETE':
        models.db.session.delete(movie)
        models.db.session.commit()
        return {
            'Deleted Movie': movie.to_json()
        }
    return {'no'}

@app.route('/movies', methods=['GET'])
def all_movies():
    movie = models.Movie.query.all()

    return { 'Movies': [m.to_json() for m in movie]}

@app.route('/tag', methods=['POST'])
def create_tag():
    tag = models.Tag(
        genre = request.json["genre"],
        movie_id = request.json["movie_id"]
    )

    models.db.session.add(tag)
    models.db.session.commit()

    return {
        tag.to_json()
    }

@app.route('/rating/movies/<int:movie_id>', methods=['GET'])
def get_all_ratings_of_movie(movie_id):
    ratings = models.Rating.query.filter_by(id=movie_id).all()

    return { 'Ratings': [r.to_json() for r in ratings]}

if __name__ == '__main__':
    port = os.environ.get('PORT') or 5000
    app.run(port=port, debug=True)