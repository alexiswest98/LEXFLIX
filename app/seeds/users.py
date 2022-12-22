from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', plan="Premium")
    robert = User(
        username='robdowneyjr', email='robertdowney@gmail.com', password='password', plan="Premium")
    kevin = User(
        username='shortking', email='kevinhart@gmail.com', password='password', plan="Premium")
    elizabeth = User(
        username='lizolsen', email='elizabetholsen@gmail.com', password='password', plan="Premium")
    ana = User(
        username='anatayjoy', email='anataylorjoy@gmail.com', password='password', plan="Premium")
    jake = User(
        username='jakegyll', email='jakegyllenhaal@gmail.com', password='password', plan="Premium")

    db.session.add(demo)
    db.session.add(robert)
    db.session.add(kevin)
    db.session.add(elizabeth)
    db.session.add(ana)
    db.session.add(jake)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        
    db.session.commit()
