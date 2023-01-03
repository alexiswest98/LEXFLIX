from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.reviews import Review
from app.forms.review_form import CreateReviewForm

movie_review_routes = Blueprint('movieReview', __name__)

## get all reviews for profile user
## added after need this may not need bottom route
@movie_review_routes.route('/profile/<int:profileId>/all', methods=["GET"])
@login_required
def get_prof_reviews(profileId):
    reviews = Review.query.filter(Review.profile_id==profileId).all()
    reviewsobj = []
    if reviews:
        for rev in reviews:
            reviewsobj.append(rev.to_dict())
        return jsonify(reviewsobj)
    return jsonify({'errors': 'Profile user has no reviews'}, 404)

## get rating for a movie based off profile
@movie_review_routes.route('/profile/<int:profileId>/movie/<int:movieId>', methods=["GET"])
@login_required
def get_user_movie_review(profileId, movieId):
    ##really only one unique review for profile & movie but ok in backend
    review = Review.query.filter(Review.movie_id==movieId and Review.profile_id==profileId).all()
    if review:
        for rev in review:
            # print(rev.to_dict())
            return jsonify(rev.to_dict())
    return jsonify({'errors': 'Review for this movie not found'}, 404)

## make a rating for a movie
@movie_review_routes.route('/profile/<int:profileId>/movie/<int:movieId>', methods=["POST"])
@login_required
def make_movie_review(profileId, movieId):
    review = Review.query.filter(Review.movie_id==movieId and Review.profile_id==profileId).all()
    if review: 
        return jsonify({'errors': 'Profile user can only have one review per movie'}, 400)
    else:
        form = CreateReviewForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        data = form.data
        if form.validate_on_submit():
            newReview = Review(
                movie_id = data['movie_id'],
                profile_id = data['profile_id'],
                rating = data['rating']
            )
            db.session.add(newReview)
            db.session.commit()
            return jsonify(newReview.to_dict())
        return jsonify(form.errors)


## edit a rating for a movie 
@movie_review_routes.route('/<int:reviewId>/edit', methods=["PUT"])
@login_required
def edit_movie_review(reviewId):
    form = CreateReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    review = Review.query.get(reviewId)
    # print("!!!!!!!!!!!!!!!!!", review.id)

    if not review:
        return {'errors': ['Review not found']}, 404
    if review and form.validate_on_submit():
        # review.movie_id = data['movie_id'],
        # review.profile_id = data['profile_id'],
        review.rating = data['rating']
        db.session.commit()
        # print("!!!!!!!!!!!!!!!!!", review.to_dict())
        return jsonify(review.to_dict())
    else:
        return jsonify(form.errors)


## delete a rating for a movie
@movie_review_routes.route('/<int:reviewId>/delete', methods=["DELETE"])
@login_required
def delete_movie_review(reviewId):
    review = Review.query.get(reviewId)
    if review: 
        db.session.delete(review)
        db.session.commit()
        return jsonify('Successfully deleted review') 
    return {'errors': ['Review not found']}, 404
