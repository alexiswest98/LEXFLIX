from .db import db, environment, SCHEMA, add_prefix_for_prod

class MyList(db.Model):
    __tablename__ = 'my_list'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("movies.id")))
    # tv_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("movies.id")))
    profile_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("profiles.id")), nullable=False)

    ##relationships
    my_list_to_movie = db.relationship('Movie', back_populates="movie_to_reviews", foreign_keys=[movie_id])
    my_list_to_profiles = db.relationship('Profile', back_populates="profiles_to_reviews", foreign_keys=[profile_id])

    def to_dict(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'profile_id': self.profile_id
        }
