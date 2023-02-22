from app.models import db, environment, SCHEMA
from app.models.my_list import MyList


# Adds a demo user, you can add other users here if you want
def seed_my_list():
    MyList1 = MyList(
        movie_id=1, profile_id=1)
    MyList2 = MyList(
        movie_id=2, profile_id=1)
    MyList3 = MyList(
        movie_id=3, profile_id=1)
    MyList4 = MyList(
        movie_id=4, profile_id=1)
    MyList5 = MyList(
        movie_id=5, profile_id=1)
    MyList6 = MyList(
        movie_id=6, profile_id=1)
    MyList7 = MyList(
        movie_id=7, profile_id=1)
    MyList8 = MyList(
        movie_id=8, profile_id=1)
    MyList9 = MyList(
        movie_id=9, profile_id=1)

    db.session.add(MyList1)
    db.session.add(MyList2)
    db.session.add(MyList3)
    db.session.add(MyList4)
    db.session.add(MyList5)
    db.session.add(MyList6)
    db.session.add(MyList7)
    db.session.add(MyList8)
    db.session.add(MyList9)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_my_list():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.my_list RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM my_list")
        
    db.session.commit()
