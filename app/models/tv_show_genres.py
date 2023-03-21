from .db import db, environment, SCHEMA, add_prefix_for_prod

class TVShowGenres(db.Model):
    __tablename__ = 'tv_show_genres'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    tv_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('movies.id')), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')), nullable=False)

    #relationships
    tv_show = db.relationship("TVShow", back_populates="tv_to_tv_genre", foreign_keys=[tv_id])
    tvgenre = db.relationship("Genre", back_populates="genres_to_tv", foreign_keys=[genre_id])

    def to_dict(self):
        return {
            'tv_id': self.movie_id,
            'genre_id': self.genre_id,
            'genre_name': self.tvgenre.genre_name,
            'movie_name': self.tv_show.tv_name
        }
