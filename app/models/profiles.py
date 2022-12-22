from .db import db, environment, SCHEMA, add_prefix_for_prod
from app.models.reviews import reviews


class Profile(db.Model):
    __tablename__ = 'profiles'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(40), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    ##relationships
    profiles_to_user = db.relationship('User', back_populates='user_to_profiles')

    review = db.relationship(
        "Profile",
        secondary=reviews,
        primaryjoin=(reviews.c.profile_id == id),
        backref=db.backref("profile", lazy="dynamic"),
        lazy="dynamic"
        )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
