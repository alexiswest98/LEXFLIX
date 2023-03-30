from .db import db, environment, SCHEMA, add_prefix_for_prod

class TVShow(db.Model):
    __tablename__ = 'tv_shows'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    tv_name = db.Column(db.String, nullable=False)
    creators = db.Column(db.String(500), nullable=False)
    cast = db.Column(db.String, nullable=False)
    tv_is = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(40), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    prev_img = db.Column(db.String, nullable=False)
    detail_img = db.Column(db.String, nullable=False)
    trailer_src = db.Column(db.String, nullable=False)
    num_seasons = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    ##relationships
    tv_to_reviews = db.relationship("TVReview", back_populates="reviews_to_tv", primaryjoin="TVShow.id==TVReview.tv_id", cascade='all,delete')
    tv_to_tv_genre = db.relationship("TVShowGenres", primaryjoin="TVShow.id==TVShowGenres.tv_id", back_populates='tv_show', cascade='all,delete')
    tv_to_my_list = db.relationship("MyList", primaryjoin="TVShow.id==MyList.tv_id", back_populates='my_list_to_tv', cascade='all,delete')
    tv_to_tv_episodes = db.relationship("TVShowEpisodes", primaryjoin="TVShow.id==TVShowEpisodes.tv_id", back_populates='tv_show_episode_to_tv', cascade='all,delete')

    def to_dict(self):
        return {
            "id": self.id,
            "tv_name": self.tv_name,
            "creators": self.director,
            "cast": self.cast,
            "tv_is": self.tv_is,
            "rating": self.rating,
            "year": self.year,
            "description": self.description,
            "prev_img": self.prev_img,
            "detail_img": self.detail_img,
            "trailer_src": self.trailer_src,
            "num_seasons": self.num_seasons,
            "created_at": self.created_at,
            'genres': [genre.genre.genre_name for genre in self.tv_to_tv_genre]
        }
