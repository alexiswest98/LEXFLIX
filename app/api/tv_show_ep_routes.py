from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
# from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.tv_show_episodes import TVShowEpisodes
from app.models.tv_shows import TVShow

tv_show_ep_routes = Blueprint('tv_show_episodes', __name__)

##get tv show episode by tv id
@tv_show_ep_routes.route('/tv/<int:tvId>/all', methods=["GET"])
@login_required
def get_tv_ep_bytv(tvId):
    tveps = TVShowEpisodes.query.filter(TVShowEpisodes.tv_id == tvId)
    if tveps:
        tvepobj = [tvep.to_dict() for tvep in tveps]
        return jsonify(tvepobj)
    return jsonify({'errors': 'Unable to find tv show episodes'}, 404)

## if i want to add more seasons later add other route
##filter by TVSHowEpisodes.season_number
