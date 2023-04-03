from app.models import db, environment, SCHEMA
from app.models.tv_show_genres import TVShowGenres

# Adds a demo user, you can add other users here if you want

def seed_tv_show_genres():
    tv_genre1 = TVShowGenres(
        genre_id=12, 
        tv_id=1
    )
    tv_genre2 = TVShowGenres(
        genre_id=13, 
        tv_id=1
    )
    tv_genre3 = TVShowGenres(
        genre_id=14, 
        tv_id=1
    )
    tv_genre4 = TVShowGenres(
        genre_id=15, 
        tv_id=2
    )
    tv_genre5 = TVShowGenres(
        genre_id=16, 
        tv_id=2
    )
    tv_genre6 = TVShowGenres(
        genre_id=17, 
        tv_id=2
    )
    tv_genre7 = TVShowGenres(
        genre_id=20, 
        tv_id=3
    )
    tv_genre8 = TVShowGenres(
        genre_id=18, 
        tv_id=3
    )
    tv_genre9 = TVShowGenres(
        genre_id=19, 
        tv_id=3
    )
    tv_genre10 = TVShowGenres(
        genre_id=21, 
        tv_id=4
    )
    tv_genre11 = TVShowGenres(
        genre_id=20, 
        tv_id=4
    )
    tv_genre12 = TVShowGenres(
        genre_id=17, 
        tv_id=4
    )
    tv_genre13 = TVShowGenres(
        genre_id=17, 
        tv_id=5
    )

    tv_genre14 = TVShowGenres(
        genre_id=16, 
        tv_id=5
    )
    tv_genre15 = TVShowGenres(
        genre_id=22, 
        tv_id=5
    )
    tv_genre16 = TVShowGenres(
        genre_id=23, 
        tv_id=6
    )
    tv_genre17 = TVShowGenres(
        genre_id=15, 
        tv_id=6
    )
    tv_genre18 = TVShowGenres(
        genre_id=24, 
        tv_id=6
    )
    tv_genre19 = TVShowGenres(
        genre_id=15, 
        tv_id=7
    )
    tv_genre20 = TVShowGenres(
        genre_id=19, 
        tv_id=7
    )
    tv_genre21 = TVShowGenres(
        genre_id=17, 
        tv_id=7
    )
    tv_genre22 = TVShowGenres(
        genre_id=24, 
        tv_id=8
    )
    tv_genre23 = TVShowGenres(
        genre_id=16, 
        tv_id=8
    )
    tv_genre24 = TVShowGenres(
        genre_id=20, 
        tv_id=8
    )
    tv_genre25 = TVShowGenres(
        genre_id=21, 
        tv_id=9
    )
    tv_genre26 = TVShowGenres(
        genre_id=22, 
        tv_id=9
    )
    tv_genre27 = TVShowGenres(
        genre_id=14, 
        tv_id=9
    )
    tv_genre28 = TVShowGenres(
        genre_id=18, 
        tv_id=10
    )
    tv_genre29 = TVShowGenres(
        genre_id=15, 
        tv_id=10
    )
    tv_genre30 = TVShowGenres(
        genre_id=16, 
        tv_id=10
    )
    tv_genre31 = TVShowGenres(
        genre_id=22, 
        tv_id=11
    )
    tv_genre32 = TVShowGenres(
        genre_id=4, 
        tv_id=11
    )
    tv_genre33 = TVShowGenres(
        genre_id=16, 
        tv_id=11
    )
    tv_genre34 = TVShowGenres(
        genre_id=18, 
        tv_id=12
    )
    tv_genre35 = TVShowGenres(
        genre_id=19, 
        tv_id=12
    )
    tv_genre36 = TVShowGenres(
        genre_id=20, 
        tv_id=12
    )

    db.session.add(tv_genre1)
    db.session.add(tv_genre2)
    db.session.add(tv_genre3)
    db.session.add(tv_genre4)
    db.session.add(tv_genre5)
    db.session.add(tv_genre6)
    db.session.add(tv_genre7)
    db.session.add(tv_genre8)
    db.session.add(tv_genre9)
    db.session.add(tv_genre10)
    db.session.add(tv_genre11)
    db.session.add(tv_genre12)
    db.session.add(tv_genre13)
    db.session.add(tv_genre14)
    db.session.add(tv_genre15)
    db.session.add(tv_genre16)
    db.session.add(tv_genre17)
    db.session.add(tv_genre18)
    db.session.add(tv_genre19)
    db.session.add(tv_genre20)
    db.session.add(tv_genre21)
    db.session.add(tv_genre22)
    db.session.add(tv_genre23)
    db.session.add(tv_genre24)
    db.session.add(tv_genre25)
    db.session.add(tv_genre26)
    db.session.add(tv_genre27)
    db.session.add(tv_genre28)
    db.session.add(tv_genre29)
    db.session.add(tv_genre30)
    db.session.add(tv_genre31)
    db.session.add(tv_genre32)
    db.session.add(tv_genre33)
    db.session.add(tv_genre34)
    db.session.add(tv_genre35)
    db.session.add(tv_genre36)
    db.session.commit()

def undo_tv_show_genres():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tv_show_genres RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM tv_show_genres")
        
    db.session.commit()
