from .db import db, environment, SCHEMA, add_prefix_for_prod


class Genre(db.Model):
    __tablename__ = 'genres'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), nullable=False, unique=True)

    ##relationships
    genres_to_movie = db.relationship('Movie', back_populates='movie_to_genres')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.genre,
        }
