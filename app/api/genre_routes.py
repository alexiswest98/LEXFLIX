from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.genres import Genre
from app.models.movie_genres import MovieGenres

genre_routes = Blueprint('genres', __name__)

## get all genres
@genre_routes.route('/all', methods=["GET"])
@login_required
def get_genres():
    genres = Genre.query.all()
    genresobj = []
    if genres:
        for genre in genres:
            genresobj.append(genre.to_dict())
        return jsonify(genresobj)
    else:
        return {'errors': ['Could not find genres']}, 404
    
## get genre by id
@genre_routes.route('/<int:genreId>', methods=["GET"])
@login_required
def get_genre_byid(genreId):
    genre = Genre.query.get(genreId)
    if genre:
        return jsonify(genre.to_dict())
    return {'errors': ['Could not find genre']}, 404

## get all genres a movie has
@genre_routes.route('/movie/<int:movieId>', methods=["GET"])
@login_required
def get_movie_genres(movieId):
    moviegenres = MovieGenres.query.filter(MovieGenres.movie_id==movieId).all()
    # print(moviegenres)
    moviegenresobj = []
    if moviegenres:
        for mov in moviegenres:
            moviegenresobj.append(mov.to_dict())
        return jsonify(moviegenresobj)
    else:
        return {'errors': ['Could not find genres for movie']}, 404
