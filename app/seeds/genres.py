from app.models import db, environment, SCHEMA
from app.models.genres import Genre

# Adds a demo user, you can add other users here if you want
def seed_genres():
    genre1 = Genre(
        genre_name='Social Issue Dramas')
    genre2 = Genre(
        genre_name='Sci-Fi')
    genre3 = Genre(
        genre_name='Comedies')
    genre4 = Genre(
        genre_name='Spanish')
    genre4 = Genre(
        genre_name='Thriller')
    genre5 = Genre(
        genre_name='Dramas')
    genre6 = Genre(
        genre_name='Romance')
    genre7 = Genre(
        genre_name='Movies Based on Books')
    genre8 = Genre(
        genre_name='Action')
    genre9 = Genre(
        genre_name='Mysteries')
    genre10 = Genre(
        genre_name='Children & Family')


    db.session.add(genre1)
    db.session.add(genre2)
    db.session.add(genre3)
    db.session.add(genre4)
    db.session.add(genre5)
    db.session.add(genre6)
    db.session.add(genre7)
    db.session.add(genre8)
    db.session.add(genre9)
    db.session.add(genre10)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_genres():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.genres RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM genres")
        
    db.session.commit()
