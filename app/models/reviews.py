from .db import db, environment, SCHEMA, add_prefix_for_prod

reviews = db.Table(
    "reviews",
    db.Column("movie_id", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False),
    db.Column("profile_id", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False),
    db.Column("rating", db.String, nullable=False)
    )

if environment == 'production':
    reviews.schema = SCHEMA
