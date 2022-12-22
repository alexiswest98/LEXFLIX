from .db import db, environment, SCHEMA, add_prefix_for_prod
from app.models.reviews import Review

class Profile(db.Model):
    __tablename__ = 'profiles'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    username = db.Column(db.String(40), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    ##relationships
    profiles_to_user = db.relationship('User', back_populates='user_to_profiles', primaryjoin="Profile.user_id==User.id")
    profiles_to_reviews = db.relationship("Review", back_populates="reviews_to_profiles",  primaryjoin="Profile.id==Review.profile_id")

    # reviews = db.relationship(
    #     "Profile",
    #     secondary=follows,
    #     primaryjoin=(follows.c.follower_id == id),
    #     backref=db.backref("following", lazy="dynamic"),
    #     lazy="dynamic"
    #     )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'username': self.username,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
