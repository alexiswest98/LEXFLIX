from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models.tv_show_reviews import TVReview

class CreateTVReviewForm(FlaskForm):
    tv_id = IntegerField('tv_id', validators=[DataRequired()])
    profile_id = IntegerField('profile_id', validators=[DataRequired()])
    rating = SelectField(u'Rating', choices=[('Thumbs Down'), ('Thumbs Neutral'), ('Thumbs Up')], validators=[DataRequired()])
