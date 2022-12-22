from .db import db, environment, SCHEMA, add_prefix_for_prod
from app.models.reviews import reviews

class Movie(db.Model):
    __tablename__ = 'movies'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(40), nullable=False, unique=True)
    cast = db.Column(db.String(255), nullable=False)
    writer = db.Column(db.String(255), nullable=False)
    genre1 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')), nullable=False)
    genre2 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')))
    genre3 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')))
    movie_is = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.String)
    description = db.Column(db.string(1000), nullable=False, unique=True)
    prev_img = db.Column(db.String, nullable=False)
    detail_img = db.Column(db.String, nullable=False)
    trailer_src = db.Column(db.String, nullable=False)
    netflix_original = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    ##relationships
    movie_to_genres = db.relationship('Genre', foreign_keys='Movie.genre1')
    movie_to_genres = db.relationship('Genre', foreign_keys='Movie.genre2')
    movie_to_genres = db.relationship('Genre', foreign_keys='Movie.genre3')
    movie_to_reviews = db.relationship('Review', back_populates="reviews_to_movie" )

    def to_dict(self):
        return {
            "id": self.id,
            "movie_name": self.movie_name,
            "director": self.director,
            "cast": self.cast,
            "writer": self.writer,
            "genre1": self.genre1,
            "genre2": self.genre2,
            "genre3": self.genre3,
            "movie_is": self.movie_is,
            "rating": self.rating,
            "year": self.year,
            "duration": self.duration,
            "description": self.description,
            "prev_img": self.prev_img,
            "detail_img": self.detail_img,
            "trailer_src": self.trailer_src,
            "netflix_original": self.netflix_original,
            "created_at": self.created_at
        }
