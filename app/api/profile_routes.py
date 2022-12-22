from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.profiles import Profile
from app.forms.profile_form import CreateProfileForm

profile_routes = Blueprint('profiles', __name__)

## get all profiles of current user
@profile_routes.route('/:current_id/all')
@login_required
def get_user_profiles(current_id):
    profiles = Profile.query.filter(current_user.id == current_id).all()
    profileobj = [prof.to_dict() for prof in profiles]
    return jsonify(profileobj)

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

##delete a profile 
@profile_routes.route('/:profile_id/delete', methods=["DELETE"])
@login_required
def delete_profile(profile_id):
    profile = Profile.query.get(profile_id)
    if profile:
        db.session.delete(profile)
        db.session.commit()
        return jsonify('Successfully deleted task')
    return jsonify('This task does not exist')

##edit profile
