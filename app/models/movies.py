from .db import db, environment, SCHEMA, add_prefix_for_prod

class Movie(db.Model):
    __tablename__ = 'movies'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(40), nullable=False, unique=True)
    cast = db.Column(db.String(255))
    writer = db.Column(db.String(255))
    genres = db.Column(db.String, nullable=False)
    overall_rating = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    description = db.Column(db.string(1000), nullable=False, unique=True)
    movie_img = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "movie_name": self.movie_name,
            "director": self.director,
            "cast": self.cast,
            "writer": self.writer,
            "genres": self.genres,
            "overall_rating": self.overall_rating,
            "year": self.year,
            "duration": self.duration,
            "description": self.description,
            "movie_img": self.movie_img,
            "created_at": self.created_at
        }
