from .db import db, environment, SCHEMA, add_prefix_for_prod

class MyList(db.Model):
    __tablename__ = 'my_list'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("movies.id")), unique=True)
    tv_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("tv_shows.id")), unique=True)
    profile_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("profiles.id")), nullable=False)

    ##relationships
    my_list_to_movie = db.relationship('Movie', back_populates="movie_to_my_list", foreign_keys=[movie_id])
    my_list_to_profiles = db.relationship('Profile', back_populates="profiles_to_my_list", foreign_keys=[profile_id])
    my_list_to_tv = db.relationship('TVShow', back_populates="tv_to_my_list", foreign_keys=[tv_id])

    def to_dict(self):
        if self.my_list_to_movie:
            return {
                'id': self.id,
                'movie_id': self.movie_id,
                'profile_id': self.profile_id,
                'movie_name':self.my_list_to_movie.movie_name,
                'detail_img':self.my_list_to_movie.prev_img,
                'movie_rating':self.my_list_to_movie.rating,
                'movie_duration':self.my_list_to_movie.duration,
                'movie_is':self.my_list_to_movie.movie_is
            }
        elif self.my_list_to_tv:
            return {
                'id': self.id,
                'tv_id': self.tv_id,
                'profile_id': self.profile_id,
                'tv_name':self.my_list_to_tv.tv_name,
                'detail_img':self.my_list_to_tv.prev_img,
                'tv_rating':self.my_list_to_tv.rating,
                'tv_duration':self.my_list_to_tv.duration,
                'tv_is':self.my_list_to_tv.tv_is
            }
