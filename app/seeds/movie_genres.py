from app.models import db, environment, SCHEMA
from app.models.movie_genres import MovieGenres


def seed_movie_genres():
    mov_genre1=MovieGenres(
        movie_id=1,
        genre_id=1
    )

    mov_genre2=MovieGenres(
        movie_id=1,
        genre_id=2
    )

    mov_genre3=MovieGenres(
        movie_id=1,
        genre_id=3
    )

    mov_genre4=MovieGenres(
        movie_id=2,
        genre_id=4
    )

    mov_genre5=MovieGenres(
        movie_id=2,
        genre_id=5
    )

    mov_genre6=MovieGenres(
        movie_id=3,
        genre_id=9
    )

    mov_genre7=MovieGenres(
        movie_id=3,
        genre_id=5
    )

    mov_genre8=MovieGenres(
        movie_id=3,
        genre_id=7
    )

    mov_genre9=MovieGenres(
        movie_id=4,
        genre_id=3
    )

    mov_genre10=MovieGenres(
        movie_id=4,
        genre_id=6
    )

    mov_genre11=MovieGenres(
        movie_id=5,
        genre_id=2
    )

    mov_genre12=MovieGenres(
        movie_id=5,
        genre_id=4
    )

    mov_genre13=MovieGenres(
        movie_id=5,
        genre_id=7
    )

    mov_genre14=MovieGenres(
        movie_id=6,
        genre_id=2
    )

    mov_genre15=MovieGenres(
        movie_id=6,
        genre_id=8
    )

    mov_genre16=MovieGenres(
        movie_id=7,
        genre_id=2
    )

    mov_genre17=MovieGenres(
        movie_id=7,
        genre_id=7
    )

    mov_genre18=MovieGenres(
        movie_id=7,
        genre_id=5
    )

    mov_genre19=MovieGenres(
        movie_id=8,
        genre_id=7
    )

    mov_genre20=MovieGenres(
        movie_id=8,
        genre_id=8
    )

    mov_genre21=MovieGenres(
        movie_id=8,
        genre_id=3
    )

    mov_genre22=MovieGenres(
        movie_id=9,
        genre_id=9
    )

    mov_genre23=MovieGenres(
        movie_id=9,
        genre_id=7
    )

    mov_genre24=MovieGenres(
        movie_id=9,
        genre_id=4
    )

    mov_genre25=MovieGenres(
        movie_id=10,
        genre_id=5
    )

    mov_genre26=MovieGenres(
        movie_id=10,
        genre_id=2
    )

    mov_genre27=MovieGenres(
        movie_id=10,
        genre_id=4
    )

    db.session.add(mov_genre1)
    db.session.add(mov_genre2)
    db.session.add(mov_genre3)
    db.session.add(mov_genre4)
    db.session.add(mov_genre5)
    db.session.add(mov_genre6)
    db.session.add(mov_genre7)
    db.session.add(mov_genre8)
    db.session.add(mov_genre9)
    db.session.add(mov_genre10)
    db.session.add(mov_genre11)
    db.session.add(mov_genre12)
    db.session.add(mov_genre13)
    db.session.add(mov_genre14)
    db.session.add(mov_genre15)
    db.session.add(mov_genre16)
    db.session.add(mov_genre17)
    db.session.add(mov_genre18)
    db.session.add(mov_genre19)
    db.session.add(mov_genre20)
    db.session.add(mov_genre21)
    db.session.add(mov_genre22)
    db.session.add(mov_genre23)
    db.session.add(mov_genre24)
    db.session.add(mov_genre25)
    db.session.add(mov_genre26)
    db.session.add(mov_genre27)
    db.session.commit()

def undo_movie_genres():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM movie_genres")
        
    db.session.commit()
