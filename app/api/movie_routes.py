from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.movies import Movie
from app.models.movie_genres import MovieGenres
from app.models.genres import Genre

movie_routes = Blueprint('movies', __name__)

## get all movies
@movie_routes.route('/all', methods=["GET"])
@login_required
def get_movies():
    movies = Movie.query.all()
    if movies:
        movieobj = [movie.to_dict() for movie in movies]
        return jsonify(movieobj)
    return jsonify({'errors': 'Unable to get movies'}, 401)

## get movie by id (just in case)
@movie_routes.route('/<int:movieId>', methods=["GET"])
@login_required
def get_movie_byid(movieId):
    movie = Movie.query.get(movieId)
    if movie:
        movobj = [movie.to_dict()]
        return jsonify(movobj)
    return jsonify({'errors': 'Unable to find movie'}, 404)

## get movies by genre (put in diff reducer)
@movie_routes.route('/<int:genreId>/all', methods=["GET"])
@login_required
def get_movie_bygenre(genreId):
    movieGenreCombo = MovieGenres.query.filter(MovieGenres.genre_id == genreId)
    # print("**************", movieGenreCombo)
    movies = []
    if not movieGenreCombo:
        return jsonify({'errors': 'No movies under that genre'}, 404)
    for combo in movieGenreCombo:
        # print(combo.movie_id)
        movie = Movie.query.get(combo.movie_id)
        movies.append(movie.to_dict())
    return jsonify(movies)
