from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models.my_list import MyList

# def validate(self):
    #     if not self.movie_id.data and not self.tv_show_id.data:
    #         raise ValidationError('Either movie ID or TV show ID must be present.')

class CreateMyListForm(FlaskForm):
    movie_id = IntegerField('movie_id')
    profile_id = IntegerField('profile_id', validators=[DataRequired()])
