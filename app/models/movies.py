from .db import db, environment, SCHEMA, add_prefix_for_prod

class Movie(db.Model):
    __tablename__ = 'movies'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String, nullable=False)
    director = db.Column(db.String(255), nullable=False)
    cast = db.Column(db.String, nullable=False)
    writer = db.Column(db.String(500), nullable=False)
    # genre1 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')), nullable=False)
    # genre2 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')))
    # genre3 = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')))
    movie_is = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(40), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    prev_img = db.Column(db.String, nullable=False)
    detail_img = db.Column(db.String, nullable=False)
    trailer_src = db.Column(db.String, nullable=False)
    netflix_original = db.Column(db.Boolean)
    lex_top = db.Column(db.Boolean)
    top_10 = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


    ##relationships
    # primaryjoin="Movie.id==Review.movie_id"
    movie_to_reviews = db.relationship("Review", back_populates="reviews_to_movie", primaryjoin="Movie.id==Review.movie_id", cascade='all,delete')
    movie_to_movie_genre = db.relationship("MovieGenres", primaryjoin="Movie.id==MovieGenres.movie_id", back_populates='movie', cascade='all,delete')


    def to_dict(self):
        return {
            "id": self.id,
            "movie_name": self.movie_name,
            "director": self.director,
            "cast": self.cast,
            "writer": self.writer,
            "movie_is": self.movie_is,
            "rating": self.rating,
            "year": self.year,
            "duration": self.duration,
            "description": self.description,
            "prev_img": self.prev_img,
            "detail_img": self.detail_img,
            "trailer_src": self.trailer_src,
            "netflix_original": self.netflix_original,
            "lex_top": self.lex_top,
            "top_10": self.top_10,
            "created_at": self.created_at
        }
