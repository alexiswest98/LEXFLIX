from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models.tv_shows import TVShow
from app.models.tv_show_genres import TVShowGenres

tv_routes = Blueprint('tv_shows', __name__)

## get all tv shows
@tv_routes.route('/all', methods=["GET"])
@login_required
def get_tv_shows():
    tv_shows = TVShow.query.all()
    if tv_shows:
        tvobj = [tv.to_dict() for tv in tv_shows]
        return jsonify(tvobj)
    return jsonify({'errors': 'Unable to get tv shows'}, 401)

## get tv show by id
@tv_routes.route('/<int:tvId>', methods=["GET"])
@login_required
def get_tv_byid(tvId):
    tv = TVShow.query.get(tvId)
    if tv:
        tvobj = [tv.to_dict()]
        return jsonify(tvobj)
    return jsonify({'errors': 'Unable to find tv show'}, 404)

##get tv show by genre
@tv_routes.route('/genre/<int:genreId>/all', methods=["GET"])
@login_required
def get_tv_bygenre(genreId):
    tvGenreCombo = TVShowGenres.query.filter(TVShowGenres.genre_id == genreId)
    # print("**************", tvGenreCombo)
    tv_shows = []
    if not tvGenreCombo:
        return jsonify({'errors': 'No tv shows under that genre'}, 404)
    for combo in tvGenreCombo:
        # print(combo.tv_show_id)
        tv = TVShow.query.get(combo.tv_id)
        tv_shows.append(tv.to_dict())
    return jsonify(tv_shows)
