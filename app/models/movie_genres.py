from .db import db, environment, SCHEMA, add_prefix_for_prod

class MovieGenres(db.Model):
    __tablename__ = 'movie_genres'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('movies.id')), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')), nullable=False)

    movie = db.relationship("Movie", back_populates="movie_to_movie_genre", foreign_keys=[movie_id])
    genre = db.relationship("Genre", back_populates="genres_to_movie", foreign_keys=[genre_id])
