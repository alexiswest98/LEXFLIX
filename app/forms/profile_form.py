from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired
from app.models.profiles import Profile

class CreateProfileForm(FlaskForm):
    user_id = IntegerField('profile_id', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
