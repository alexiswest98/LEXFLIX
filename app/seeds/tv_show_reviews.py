from app.models import db, environment, SCHEMA
from app.models.tv_show_reviews import TVReview

def seed_tv_reviews():
    tv_review1 = TVReview(
        tv_id=1,
        profile_id=1,
        rating="Thumbs Up",
    )
    tv_review2 = TVReview(
        tv_id=2,
        profile_id=1,
        rating="Thumbs Up",
    )
    tv_review3 = TVReview(
        tv_id=3,
        profile_id=1,
        rating="Thumbs Up",
    )
    tv_review4 = TVReview(
        tv_id=4,
        profile_id=1,
        rating="Thumbs Up",
    )
    tv_review5 = TVReview(
        tv_id=5,
        profile_id=1,
        rating="Thumbs Up",
    )

    db.session.add(tv_review1)
    db.session.add(tv_review2)
    db.session.add(tv_review3)
    db.session.add(tv_review4)
    db.session.add(tv_review5)
    db.session.commit()

def undo_tv_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tv_show_reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM tv_show_reviews")
        
    db.session.commit()
