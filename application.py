import os
import models
import sqlalchemy
import hashlib
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
import seed
import jwt

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
# .replace('postgres', 'postgresql')
models.db.init_app(app)

@app.route('/seed', methods=["POST"])
def seed_backend():
    seed.seed()

    return 'Seeded'

@app.route('/', methods=["GET"])
def connect():
    return 'ok'


@app.route('/users/signup', methods=['POST'])
def signup():
    try: 
        z = request.json["password"].encode()
        user = models.User(
            username = request.json["username"],
            email = request.json["email"],
            password = hashlib.sha256(z).hexdigest()
        )
        models.db.session.add(user)
        models.db.session.commit()

        return {
            'user': user.to_json()
        }
    except sqlalchemy.exc.IntegrityError:
        return {
            'error': 'error'
        }

@app.route('/users/login', methods=['POST'])
def login():
    try:
        user = models.User.query.filter_by(email=request.json["email"]).first()
        user_token = jwt.encode({'id': user.id}, os.environ.get("JWT_SECRET"))
        p = request.json["password"]
        if  user.validate_pass(p):
            return {
                'token': user_token,
                'user': user.to_json()
            }
        return { 'Login': 'Unauthorized' }
    except AttributeError:
        return { 'Login': 'Unauthorized'}

@app.route('/users/<int:id>', methods=['PUT', 'GET'])
def update_user(id):
    user = models.User.query.filter_by(id=id).first()
    if request.method == 'PUT':
        user.password = request.json["password"]

        models.db.session.add(user)
        models.db.session.commit()

        return {
            'updated': user.to_json()
        }
    elif request.method == 'GET':
        return {
            'User': user.to_json()
        }

@app.route('/user/update/<int:id>', methods=["PUT"])
def change_pass(id):
    user = models.User.query.filter_by(id=id).first()

    if user.validate_pass(request.json["cPassword"]):
        z = request.json["password"].encode()
        user.password = hashlib.sha256(z).hexdigest()
        

    models.db.session.add(user)
    models.db.session.commit()

    return {
        'Updated User': user.to_json()
    }

@app.route('/movies/create', methods=['POST'])
def create_movie():
    movie = models.Movie(
        title = request.json["title"],
        description = request.json["description"],
        movie_src = request.json["movie_src"],
        movie_cover = request.json["movie_cover"],
        rating = request.json["rating"]
    )

    models.db.session.add(movie)
    models.db.session.commit()

    return {
        'Created_Movie': movie.to_json()
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
        movie.movie_src = request.json["movie_src"]
        
        models.db.session.add(movie)
        models.db.session.commit()
        return { 
            'movie': movie.to_json()
        }
    elif request.method == 'DELETE':
        models.db.session.delete(movie)
        models.db.session.commit()
        return {
            'Deleted_Movie': movie.to_json()
        }
    return {'no'}

@app.route('/movies', methods=['GET'])
def all_movies():
    movie = models.Movie.query.all()

    return { 'Movies': [m.to_json() for m in movie]}

@app.route('/tag', methods=["POST"])
def create_tag():
    tag = models.Tag(
        genre = request.json["genre"],
        movie_id = request.json["movie_id"]
    )

    models.db.session.add(tag)
    models.db.session.commit()

    return {
        'tag': tag.to_json()
    }

@app.route('/tag/all', methods=["GET"])
def all_tags():
    tags = models.Tag.query.all()

    return {
        'Tags': [t.to_json() for t in tags]
    }

@app.route('/rating/<int:user_id>', methods=["POST"])
def get_user_rating(user_id):
    user_rating = models.Rating.query.filter_by(user_id=user_id).all()

    return {
        'Rating': [ur.to_json() for ur in user_rating]
    }

@app.route('/rating/movies/<int:movie_id>', methods=["GET", "POST", "PUT"])
def get_all_ratings_of_movie(movie_id):
    try:
        if request.method == "GET":
            ratings = models.Rating.query.filter_by(movie_id=movie_id).all()

            sum_of_ratings = 0
            for r in ratings:
                sum_of_ratings += r.rating

            avg = sum_of_ratings / len(ratings)
            
            return { 
                'average': avg,
                'Ratings': [r.to_json() for r in ratings]
            }
        elif request.method == "POST":
            ratings_new = models.Rating(
                movie_id = request.json["movie_id"],
                rating = float(request.json["rating"]),
                user_id = request.json["user_id"]
            )

            models.db.session.add(ratings_new)
            models.db.session.commit()

            return {
                'Rating': ratings_new.to_json()
            }
    except ZeroDivisionError:
        return {
            'average': 0
        }

@app.route('/rating/movies/update', methods=["PUT"])
def update_rating():
    if request.method == "PUT":
            ratings = models.Rating.query.filter_by(movie_id=request.json["movie_id"]).filter_by(user_id=request.json["user_id"]).first()

            ratings.rating = request.json["rating"]
            models.db.session.add(ratings)
            models.db.session.commit()

            all_ratings = models.Rating.query.filter_by(movie_id=request.json["movie_id"]).all()

            return {
                'All ratings': [r.to_json() for r in all_ratings],
                'Rating': ratings.to_json()
            }

@app.route('/user/verify', methods=['GET'])
def verify():
    decode = jwt.decode(request.headers["Authorization"], options={"verify_signature": False})
    user = models.User.query.filter_by(id=decode['id']).first()
    if user:
        return { 'user': user.to_json() }
    else:
        return { 'error': 'user not found' }, 404

@app.route('/review/new', methods=["POST"])
def new_review():
    review = models.Review(
        review_body = request.json["review_body"],
        movie_id = request.json["movie_id"],
        user_id = request.json["user_id"]
    )

    models.db.session.add(review)
    models.db.session.commit()

    return {
        'Review': review.to_json()
    }

@app.route('/review/all', methods=["GET"])
def all_reviews():
    reviews = models.Review.query.all()

    return {
        'Reviews': [r.to_json() for r in reviews]
    }

@app.route('/reviews/<int:movie_id>', methods=["GET"])
def get_movie_reviews(movie_id):
    reviews = models.Review.query.filter_by(movie_id=movie_id).all()

    return {
        'Reviews': [r.to_json() for r in reviews]
    }

if __name__ == '__main__':
    port = os.environ.get('PORT') or 5000
    app.run(host='0.0.0.0', port=port, debug=True)