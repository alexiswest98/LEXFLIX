from app.models import db, environment, SCHEMA
from app.models.profiles import Profile


# Adds a demo user, you can add other users here if you want
def seed_profiles():
    prof1 = Profile(
        user_id= 1, username='Profile1')
    prof2 = Profile(
        user_id= 1, username='Profile2')
    prof3 = Profile(
        user_id= 1, username='Profile3')
    prof11 = Profile(
        user_id= 2, username='Profile1')
    prof12 = Profile(
        user_id= 2, username='Profile2')
    prof13 = Profile(
        user_id= 2, username='Profile3')

    db.session.add(prof1)
    db.session.add(prof2)
    db.session.add(prof3)
    db.session.add(prof11)
    db.session.add(prof12)
    db.session.add(prof13)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_profiles():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.profiles RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM profiles")
        
    db.session.commit()
