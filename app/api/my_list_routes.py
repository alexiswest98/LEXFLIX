from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.my_list import MyList
from app.forms.my_list_form import CreateMyListForm

my_list_routes = Blueprint('myList', __name__)

##get all media for profile user 
@my_list_routes.route('/profile/<int:profileId>/all', methods=["GET"])
@login_required
def get_prof_my_list(profileId):
    media = MyList.query.filter(MyList.profile_id==profileId).all()
    mediaobj = []
    if media:
        for show in media:
            mediaobj.append(show.to_dict())
        return jsonify(mediaobj)
    return jsonify({'errors': 'Profile user has no shows or movies in My-List'}, 404)

##add a movie to my list
@my_list_routes.route('/profile/<int:profileId>/movie/<int:movieId>', methods=["POST"])
@login_required
def add_my_list(profileId, movieId):
    form = CreateMyListForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    ##error validation
    media = MyList.query.filter(MyList.profile_id==profileId, MyList.movie_id==movieId).first()
    # print(media)

    if media:
        return jsonify({'errors': 'Profile user already has this movie in My-List'}, 400)

    if not media and form.validate_on_submit():
        newAddition = MyList(
            movie_id = data['movie_id'],
            profile_id = data['profile_id'],
        )
        db.session.add(newAddition)
        db.session.commit()
        return jsonify(newAddition.to_dict())
    return jsonify(form.errors)

##add a show to my list
@my_list_routes.route('/profile/<int:profileId>/tvshow/<int:showId>', methods=["POST"])
@login_required
def add_my_list_show(profileId, showId):
    form = CreateMyListForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    ##error validation
    media = MyList.query.filter(MyList.profile_id==profileId, MyList.tv_id==showId).first()

    if media:
        return jsonify({'errors': 'Profile user already has this show in My-List'}, 400)
    if not media and form.validate_on_submit():
        newAddition = MyList(
            tv_id = data['tv_id'],
            profile_id = data['profile_id'],
        )
        db.session.add(newAddition)
        db.session.commit()
        return jsonify(newAddition.to_dict())
    return jsonify(form.errors)


##delete from my-list
@my_list_routes.route('/<int:mediaId>/delete', methods=["DELETE"])
@login_required
def delete_my_list(mediaId):
    media = MyList.query.get(mediaId)
    if media: 
        db.session.delete(media)
        db.session.commit()
        return jsonify('Successfully deleted from My-List') 
    return {'errors': ['Media not found']}, 404
