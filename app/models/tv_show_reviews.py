from .db import db, environment, SCHEMA, add_prefix_for_prod

class TVReview(db.Model):
    __tablename__ = 'tv_show_reviews'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    tv_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("tv_shows.id")), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("profiles.id")), nullable=False)
    rating = db.Column(db.String, nullable=False)

    ##relationships
    reviews_to_tv = db.relationship('TVShow', back_populates="tv_to_reviews", foreign_keys=[tv_id])
    tv_reviews_to_profiles = db.relationship('Profile', back_populates="profiles_to_tv_reviews", foreign_keys=[profile_id])

    def to_dict(self):
        return {
            'id': self.id,
            'tv_id': self.tv_id,
            'profile_id': self.profile_id,
            'rating': self.rating
        }
