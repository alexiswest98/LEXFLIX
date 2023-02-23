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
        genre_id=8
    )

    mov_genre7=MovieGenres(
        movie_id=3,
        genre_id=5
    )

    mov_genre8=MovieGenres(
        movie_id=3,
        genre_id=1
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
        genre_id=5
    )

    mov_genre13=MovieGenres(
        movie_id=5,
        genre_id=8
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
        genre_id=8
    )

    mov_genre18=MovieGenres(
        movie_id=7,
        genre_id=5
    )

    mov_genre19=MovieGenres(
        movie_id=8,
        genre_id=8
    )

    mov_genre20=MovieGenres(
        movie_id=8,
        genre_id=9
    )

    mov_genre21=MovieGenres(
        movie_id=8,
        genre_id=3
    )

    mov_genre22=MovieGenres(
        movie_id=9,
        genre_id=10
    )

    mov_genre23=MovieGenres(
        movie_id=9,
        genre_id=6
    )

    mov_genre24=MovieGenres(
        movie_id=9,
        genre_id=5
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
        genre_id=9
    )

    mov_genre28=MovieGenres(
        movie_id=11,
        genre_id=5
    )

    mov_genre29=MovieGenres(
        movie_id=11,
        genre_id=3
    )

    mov_genre30=MovieGenres(
        movie_id=11,
        genre_id=10
    )

    mov_genre31=MovieGenres(
        movie_id=12,
        genre_id=5
    )

    mov_genre32=MovieGenres(
        movie_id=12,
        genre_id=10
    )

    mov_genre33=MovieGenres(
        movie_id=13,
        genre_id=9
    )

    mov_genre34=MovieGenres(
        movie_id=13,
        genre_id=3
    )

    mov_genre35=MovieGenres(
        movie_id=14,
        genre_id=9
    )

    mov_genre36=MovieGenres(
        movie_id=14,
        genre_id=5
    )

    mov_genre37=MovieGenres(
        movie_id=14,
        genre_id=6
    )

    mov_genre38=MovieGenres(
        movie_id=15,
        genre_id=3
    )

    mov_genre39=MovieGenres(
        movie_id=15,
        genre_id=11
    )

    mov_genre39=MovieGenres(
        movie_id=16,
        genre_id=5
    )

    mov_genre39=MovieGenres(
        movie_id=16,
        genre_id=2
    )

    mov_genre39=MovieGenres(
        movie_id=16,
        genre_id=9
    )

    mov_genre40=MovieGenres(
        movie_id=17,
        genre_id=5
    )

    mov_genre41=MovieGenres(
        movie_id=17,
        genre_id=9
    )

    mov_genre42=MovieGenres(
        movie_id=18,
        genre_id=5
    )

    mov_genre43=MovieGenres(
        movie_id=18,
        genre_id=8
    )

    mov_genre44=MovieGenres(
        movie_id=18,
        genre_id=6
    )

    mov_genre45=MovieGenres(
        movie_id=19,
        genre_id=9
    )

    mov_genre46=MovieGenres(
        movie_id=19,
        genre_id=5
    )

    mov_genre47=MovieGenres(
        movie_id=20,
        genre_id=11
    )

    mov_genre48=MovieGenres(
        movie_id=20,
        genre_id=6
    )

    mov_genre49=MovieGenres(
        movie_id=20,
        genre_id=3
    )

    mov_genre50=MovieGenres(
        movie_id=21,
        genre_id=5
    )

    mov_genre51=MovieGenres(
        movie_id=21,
        genre_id=6
    )

    mov_genre52=MovieGenres(
        movie_id=4,
        genre_id=7
    )

    mov_genre53=MovieGenres(
        movie_id=6,
        genre_id=10
    )
    mov_genre54=MovieGenres(
        movie_id=22,
        genre_id=3
    )
    mov_genre55=MovieGenres(
        movie_id=22,
        genre_id=11
    )
    mov_genre56=MovieGenres(
        movie_id=23,
        genre_id=9
    )
    mov_genre57=MovieGenres(
        movie_id=23,
        genre_id=10
    )
    mov_genre58=MovieGenres(
        movie_id=23,
        genre_id=5
    )
    mov_genre59=MovieGenres(
        movie_id=24,
        genre_id=9
    )
    mov_genre60=MovieGenres(
        movie_id=24,
        genre_id=5
    )
    mov_genre61=MovieGenres(
        movie_id=25,
        genre_id=2
    )
    mov_genre62=MovieGenres(
        movie_id=25,
        genre_id=5
    )
    mov_genre63=MovieGenres(
        movie_id=25,
        genre_id=10
    )
    mov_genre64=MovieGenres(
        movie_id=26,
        genre_id=7
    )
    mov_genre65=MovieGenres(
        movie_id=26,
        genre_id=3
    )
    mov_genre66=MovieGenres(
        movie_id=27,
        genre_id=9
    )
    mov_genre67=MovieGenres(
        movie_id=27,
        genre_id=7
    )
    mov_genre68=MovieGenres(
        movie_id=27,
        genre_id=3
    )
    mov_genre69=MovieGenres(
        movie_id=28,
        genre_id=3
    )
    mov_genre70=MovieGenres(
        movie_id=28,
        genre_id=9
    )
    mov_genre71=MovieGenres(
        movie_id=28,
        genre_id=7
    )
    mov_genre72=MovieGenres(
        movie_id=29,
        genre_id=7
    )
    mov_genre73=MovieGenres(
        movie_id=29,
        genre_id=3
    )
    mov_genre74=MovieGenres(
        movie_id=30,
        genre_id=9
    )
    mov_genre75=MovieGenres(
        movie_id=30,
        genre_id=11
    )
    mov_genre76=MovieGenres(
        movie_id=31,
        genre_id=7
    )
    mov_genre77=MovieGenres(
        movie_id=31,
        genre_id=11
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
    db.session.add(mov_genre28)
    db.session.add(mov_genre29)
    db.session.add(mov_genre30)
    db.session.add(mov_genre31)
    db.session.add(mov_genre32)
    db.session.add(mov_genre33)
    db.session.add(mov_genre34)
    db.session.add(mov_genre35)
    db.session.add(mov_genre36)
    db.session.add(mov_genre37)
    db.session.add(mov_genre38)
    db.session.add(mov_genre39)
    db.session.add(mov_genre40)
    db.session.add(mov_genre41)
    db.session.add(mov_genre42)
    db.session.add(mov_genre43)
    db.session.add(mov_genre44)
    db.session.add(mov_genre45)
    db.session.add(mov_genre46)
    db.session.add(mov_genre47)
    db.session.add(mov_genre48)
    db.session.add(mov_genre49)
    db.session.add(mov_genre50)
    db.session.add(mov_genre51)
    db.session.add(mov_genre52)
    db.session.add(mov_genre53)
    db.session.add(mov_genre54)
    db.session.add(mov_genre55)
    db.session.add(mov_genre56)
    db.session.add(mov_genre57)
    db.session.add(mov_genre58)
    db.session.add(mov_genre59)
    db.session.add(mov_genre60)
    db.session.add(mov_genre61)
    db.session.add(mov_genre62)
    db.session.add(mov_genre63)
    db.session.add(mov_genre64)
    db.session.add(mov_genre65)
    db.session.add(mov_genre66)
    db.session.add(mov_genre67)
    db.session.add(mov_genre68)
    db.session.add(mov_genre69)
    db.session.add(mov_genre70)
    db.session.add(mov_genre71)
    db.session.add(mov_genre72)
    db.session.add(mov_genre73)
    db.session.add(mov_genre74)
    db.session.add(mov_genre75)
    db.session.add(mov_genre76)
    db.session.add(mov_genre77)

    db.session.commit()

def undo_movie_genres():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.movie_genres RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM movie_genres")
        
    db.session.commit()
