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
    genre5 = Genre(
        genre_name='Thriller')
    genre6 = Genre(
        genre_name='Dramas')
    genre7 = Genre(
        genre_name='Romance')
    genre8 = Genre(
        genre_name='Movies Based on Books')
    genre9 = Genre(
        genre_name='Action')
    genre10 = Genre(
        genre_name='Mysteries')
    genre11 = Genre(
        genre_name='Children & Family')
    genre12 = Genre(
        genre_name='Kids\' TV')
    genre13 = Genre(
        genre_name='TV Cartoons')
    genre14 = Genre(
        genre_name='Fantasy TV Shows')
    genre15 = Genre(
        genre_name='Sci Fi TV')
    genre16 = Genre(
        genre_name='TV Thrillers')
    genre17 = Genre(
        genre_name='TV Horror')
    genre18 = Genre(
        genre_name='British')
    genre19 = Genre(
        genre_name='Teen TV Shows')
    genre20 = Genre(
        genre_name='TV Dramas')
    genre21 = Genre(
        genre_name='TV Mysteries')
    genre22 = Genre(
        genre_name='Crime TV Shows')
    genre23 = Genre(
        genre_name='Japanese')
    genre24 = Genre(
        genre_name='TV Shows Based on Manga')
    genre24 = Genre(
        genre_name='Korean')



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
    db.session.add(genre11)
    db.session.add(genre12)
    db.session.add(genre13)
    db.session.add(genre14)
    db.session.add(genre15)
    db.session.add(genre16)
    db.session.add(genre17)
    db.session.add(genre18)
    db.session.add(genre19)
    db.session.add(genre20)
    db.session.add(genre21)
    db.session.add(genre22)
    db.session.add(genre23)
    db.session.add(genre24)
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
