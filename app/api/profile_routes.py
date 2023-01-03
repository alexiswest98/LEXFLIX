from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.profiles import Profile
from app.forms.profile_form import CreateProfileForm

profile_routes = Blueprint('profiles', __name__)

## get all profiles of current user
@profile_routes.route('/all', methods=["GET"])
@login_required
def get_user_profiles():
    profiles = Profile.query.filter(Profile.user_id == current_user.id).all()
    if profiles:
        profileobj = [prof.to_dict() for prof in profiles]
        return jsonify(profileobj)
    return jsonify({'errors': 'Profiles for that User not found'}, 404)

## make a profile 
@profile_routes.route('/create', methods=["POST"])
@login_required
def make_profile():
    form = CreateProfileForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    if form.validate_on_submit():
        newprof = Profile(
            user_id = data['user_id'],
            username = data['username']
            )
        db.session.add(newprof)
        db.session.commit()
        return jsonify(newprof.to_dict())
    return jsonify(form.errors)

##edit profile
@profile_routes.route('/<int:profileId>/edit', methods=["PUT"])
@login_required
def edit_profile(profileId):
    form = CreateProfileForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    prof = Profile.query.get(profileId)

    if prof and form.validate_on_submit():
        prof.user_id = data['user_id']
        prof.username = data['username']
        db.session.commit()
        return jsonify(prof.to_dict())
    if not prof:
        return {'errors': ['That profile does not exist']}, 404
    else:
        return jsonify(form.errors)

##delete a profile 
@profile_routes.route('/<int:profileId>/delete', methods=["DELETE"])
@login_required
def delete_profile(profileId):
    profile = Profile.query.get(profileId)
    if profile:
        db.session.delete(profile)
        db.session.commit()
        return jsonify('Successfully deleted profile')
    return jsonify({'errors': 'Profile not found'}, 404)
