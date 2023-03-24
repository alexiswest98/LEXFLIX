from .db import db, environment, SCHEMA, add_prefix_for_prod

class TVShowEpisodes(db.Model):
    __tablename__ = 'tv_show_episodes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    tv_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('movies.id')), nullable=False)
    ep_number = db.Column(db.Integer, nullable=False)
    ep_name = db.Column(db.String, nullable=False)
    ep_description = db.Column(db.String, nullable=False)
    ep_duration = db.Column(db.Integer, nullable=False)
    ep_poster = db.Column(db.String, nullable=False)

    #relationships
    tv_show = db.relationship("TVShow", back_populates="tv_to_tv_episodes", foreign_keys=[tv_id])

    def to_dict(self):
        return {
            'tv_id': self.tv_id,
            'episode_number': self.episode_number,
            'episode_name': self.episode_name,
            'episode_description': self.episode_description,
            'episode_release_date': self.episode_release_date,
            'episode_runtime': self.episode_runtime,
            'episode_poster': self.episode_poster,
            'episode_trailer': self.episode_trailer
        }
