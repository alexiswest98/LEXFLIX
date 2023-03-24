from .db import db, environment, SCHEMA, add_prefix_for_prod

class TVShow(db.Model):
    __tablename__ = 'tv_shows'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    tv_name = db.Column(db.String, nullable=False)
    director = db.Column(db.String(255), nullable=False)
    cast = db.Column(db.String, nullable=False)
    writer = db.Column(db.String(500), nullable=False)
    tv_is = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(40), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    prev_img = db.Column(db.String, nullable=False)
    detail_img = db.Column(db.String, nullable=False)
    trailer_src = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


    ##relationships
    tv_to_reviews = db.relationship("TVReview", back_populates="reviews_to_tv", primaryjoin="TVShow.id==Review.movie_id", cascade='all,delete')
    tv_to_tv_genre = db.relationship("TVShowGenres", primaryjoin="TVShow.id==TVShowGenres.tv_id", back_populates='tv_show', cascade='all,delete')
    tv_to_my_list = db.relationship("MyList", primaryjoin="TVShow.id==MyList.tv_id", back_populates='my_list_to_tv', cascade='all,delete')

    def to_dict(self):
        return {
            "id": self.id,
            "tv_name": self.movie_name,
            "director": self.director,
            "cast": self.cast,
            "writer": self.writer,
            "tv_is": self.movie_is,
            "rating": self.rating,
            "year": self.year,
            "duration": self.duration,
            "description": self.description,
            "prev_img": self.prev_img,
            "detail_img": self.detail_img,
            "trailer_src": self.trailer_src,
            "created_at": self.created_at,
            # 'genres': [genre.genre.genre_name for genre in self.tv_to_tv_genre]
        }
