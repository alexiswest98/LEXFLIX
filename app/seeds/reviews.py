from app.models import db, environment, SCHEMA
from app.models.reviews import Review


# Adds a demo user, you can add other users here if you want
def seed_reviews():
    review1 = Review(
        movie_id=1, profile_id=1, rating="Thumbs Up")
    review2 = Review(
        movie_id=2, profile_id=1, rating="Thumbs Up")
    review3 = Review(
        movie_id=3, profile_id=1, rating="Thumbs Up")
    review4 = Review(
        movie_id=4, profile_id=1, rating="Thumbs Up")
    review5 = Review(
        movie_id=5, profile_id=1, rating="Thumbs Up")
    review6 = Review(
        movie_id=6, profile_id=1, rating="Thumbs Up")

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM reviews")
        
    db.session.commit()
