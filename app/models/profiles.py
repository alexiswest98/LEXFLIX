from .db import db, environment, SCHEMA, add_prefix_for_prod
from app.models.reviews import Review

class Profile(db.Model):
    __tablename__ = 'profiles'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    username = db.Column(db.String(40), nullable=False)
    profile_img = db.Column(db.String, default='https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/K6hjPJd6cR6FpVELC5Pd6ovHRSk/AAAABUoj4FT-0Rr558WbETiintMnmH2JKw4l_p4MdMoxqVx7YXwsvLvvnGUtx3HKZN_BJFH4EHpXn5KqSCBVxLrRz0n4gk64yyeAFw.png?r=229')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    ##relationships
    profiles_to_user = db.relationship('User', back_populates='user_to_profiles', foreign_keys=[user_id])
    profiles_to_reviews = db.relationship("Review", back_populates="reviews_to_profiles",  primaryjoin="Profile.id==Review.profile_id", cascade='all,delete')

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
            'profile_img': self.profile_img,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
