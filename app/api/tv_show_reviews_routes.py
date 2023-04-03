from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
# from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.tv_show_reviews import TVReview
from app.forms.tv_review_form import CreateTVReviewForm

tv_show_review_routes = Blueprint('tv_show_reviews', __name__)

##get all reviews for a profile user
@tv_show_review_routes.route('/profile/<int:profileId>/all', methods=["GET"])
@login_required
def get_tv_review_byprofile(profileId):
    tvreviews = TVReview.query.filter(TVReview.profile_id == profileId)
    if tvreviews:
        tvreviewobj = [tvreview.to_dict() for tvreview in tvreviews]
        return jsonify(tvreviewobj)
    return jsonify({'errors': 'Unable to find tv show reviews'}, 404)

##get rating for a tv show by profile user
@tv_show_review_routes.route('/<int:tvId>/profile/<int:profileId>', methods=["GET"])
@login_required
def get_tv_review_rating_byprofile(tvId, profileId):
    tvreview = TVReview.query.filter(TVReview.profile_id == profileId, TVReview.tv_id == tvId).first()
    if tvreview:
        tvreviewobj = tvreview.to_dict()
        return jsonify(tvreviewobj)
    return jsonify({'errors': 'Unable to find tv show review'}, 404)

##make a tv review rating 
@tv_show_review_routes.route('/<int:tvId>/profile/<int:profileId>', methods=["POST"])
@login_required
#front end set up: if it has a review and they click again it will delete it or edit it
def make_tv_review(tvId, profileId):
    form = CreateTVReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    if form.validate_on_submit():
        newTVReview = TVReview(
            tv_id = data['tv_id'],
            profile_id = data['profile_id'],
            rating = data['rating']
        )
        db.session.add(newTVReview)
        db.session.commit()
        return jsonify(newTVReview.to_dict())
    return jsonify(form.errors)

##edit a tv review rating
@tv_show_review_routes.route('/<int:tvreviewId>/edit', methods=["PUT"])
@login_required
def edit_tv_review(tvreviewId):
    form = CreateTVReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data

    if form.validate_on_submit():
        tvreview = TVReview.query.get(tvreviewId)
        if tvreview:
            tvreview.rating = data['rating']
            db.session.commit()
            return jsonify(tvreview.to_dict())
        return jsonify({'errors': 'Unable to find tv show review'}, 404)
    return jsonify(form.errors)

##delete a tv review rating
@tv_show_review_routes.route('/<int:tvreviewId>/delete', methods=["DELETE"])
@login_required
def delete_tv_review(tvreviewId):
    tvreview = TVReview.query.get(tvreviewId)
    if tvreview: 
        db.session.delete(tvreview)
        db.session.commit()
        return jsonify('Successfully deleted TV review') 
    return {'errors': ['TV show review not found']}, 404
