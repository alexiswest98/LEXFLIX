from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("movies.id")), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("profiles.id")), nullable=False)
    rating = db.Column(db.String, nullable=False)

    ##relationships
    reviews_to_movie = db.relationship('Movie', back_populates="movie_to_reviews", primaryjoin="Review.movie_id==Movie.id")
    reviews_to_profiles = db.relationship('Profile', back_populates="profiles_to_reviews",  primaryjoin="Review.profile_id==Profile.id")

    def to_dict(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'profile_id': self.profile_id,
            'rating': self.rating
        }
