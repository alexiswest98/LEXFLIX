from app.models import db, environment, SCHEMA
from app.models.movies import Movie

# Adds a demo user, you can add other users here if you want

##netflix originnals
def seed_movies():
    movie1 = Movie(
        movie_name="Don't Look Up",
        director="Adam McKay",
        cast="Leonardo DiCaprio, Jennifer Lawrence,	Meryl Streep",
        writer="Adam McKay, David Sirota",
        genre1=1,
        genre2=2,
        genre3=3,
        movie_is="Offbeat, Provocative, Witty",
        rating="R",
        year=2021,
        duration="2h 18m",
        description="Two astronomers go on a media tour to warn humankind of a planet-killing comet hurtling toward Earth. The response from a distracted world: Meh.",
        prev_img="https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABciGejhlI4_RL7lOo27FZ6g0DERsFnO69RRmm_7x-zN5o42ufxLn1OKYb8qJfXQE8NUOVIEtLqQUhtWVn8SV1ValiYGJdyeFF4rcWCgBcgohEQ1noO_NgOA-yFSkm6uBmyLd.jpg?r=446",
        detail_img ="https://occ-0-988-1722.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABf2NpNhZsRSLwu3n0KhysCBpHNRlTQu86BLXuxSsleAMrjLNF6G0COGO2-s8YUywD64vHPiX5knGmTkMgF6A002TGi6eilpE329N.jpg?r=7c6",
        trailer_src= "https://www.youtube.com/embed/RbIxYm3mKzI?controls=0",
        netflix_original= True)

    movie2 = Movie(
        movie_name= "The Platform" , 
        director= "Galder Gaztelu-Urrutia",
        cast= "Ivan Massagué, Antonia San Juan, Zorion Eguileor",
        writer= "David Desola, Pedro Rivero",
        genre1= 4,
        genre2= 5,
        movie_is= "Violent, Dark",
        rating= "TV-MA" ,
        year= 2019 ,
        duration= "1h 34m", 
        description= "A slab of food descends floor by floor in a prison. The inmates above eat heartily, leaving those below starving and desperate. A rebellion is imminent.",
        prev_img= "https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABQNDChmnSqrkP0cYD7U9-C-5ZXi69mQZI6dGY61SECQoXesJdRo_LNHS35p7R_GIYpjUoo_52N4prIDfsq-Cgo2yIT76EBzu-iV0269q7Nb_2Z0ljv2BcOAnPdKy6qnMBkxC.jpg?r=fc2",
        detail_img = "https://static01.nyt.com/images/2020/03/26/arts/platform1/platform1-mobileMasterAt3x.jpg",
        trailer_src= "https://www.youtube.com/embed/RlfooqeZcdY?controls=0",
        netflix_original= True
        )

    movie3 = Movie(
        movie_name= "Luckiest Girl Alive" , 
        director= "Mike Barker" ,
        cast= "Mila Kunis, Finn Wittrock, Connie Britton" ,
        writer= "Jessica Knoll" ,
        genre1= 5,
        genre2= 7,
        movie_is= "Bittersweet, Dark",
        rating= "R",
        year= 2022,
        duration= "1h 55m" , 
        description= "A writer's perfectly crafted New York City life starts to unravel when a true-crime documentary forces her to confront her harrowing high school history." ,
        prev_img= "https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABR7IruY4nAy8ADtOzwxbyt7DrRqlLLoPfCuEaxdW9fcf_zW0vbFx6OPjf3CyptVzSxbtFvdvhAVmjdZYMq4aGeJOO4PDuSnzx7RKyqW-HHKsa4CSCD1jVasSAtWP3KL9Cyns.jpg?r=e28" ,
        detail_img = "https://www.themoviedb.org/t/p/w780/iHc14vucwUMl6WuvQa4iPfoEdy9.jpg",
        trailer_src= "https://www.youtube.com/embed/B_XUlbPW-eY?controls=0",
        netflix_original= True
        )

    movie4 = Movie(
        movie_name= "Someone Great" , 
        director= "Jennifer Kaytin Robinson",
        cast= "Gina Rodriguez, Brittany Snow, DeWanda Wise",
        writer= "Jennifer Kaytin Robinson",
        genre1= 3,
        genre2= 6,
        movie_is= "Bittersweet, Romantic",
        rating= "R",
        year= 2019,
        duration= "1h 32m", 
        description= "On the heels of a blindsiding breakup, music journalist Jenny braces for a new beginning -- and one last adventure with her closest friends.",
        prev_img= "https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6g…B6Cl8PpABtrkmBhfYqvsiCLk61u4RfqiL0joPgA.jpg?r=8e1",
        detail_img = "https://occ-0-56-1123.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABYS8Zaxee9mTX3Af5Uo2iyd9uWrZmHrqm_3V2kqg45uNf9Y2jQTsKXeB8nRZKF2LH2bVkxfbpNMApplNCn3cqqPwe2f6HaaAmzWu.jpg?r=9ce",
        trailer_src= "https://www.youtube.com/embed/BBd9gcrj2Wk?controls=0",
        netflix_original= True
        )

    movie5 = Movie(
        movie_name= "Spiderhead", 
        director= "Joseph Kosinski",
        cast= "Chris Hemsworth, Miles Teller, Jurnee Smollett",
        writer= "Rhett Reese, Paul Wernick",
        genre1= 2,
        genre2= 4,
        genre3= 7,
        movie_is= "Offbeat",
        rating= "R",
        year= 2022,
        duration= "1h 47m", 
        description= "A prisoner in a state-of-the-art penitentiary begins to question the purpose of the emotion-controlling drugs he's testing for a pharmaceutical genius.",
        prev_img= "	https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6g…pcCKlbVuljP6PK1W3jmAkIvKhkJJPC87oiq6H1j.jpg?r=ee6",
        detail_img = "https://fictionhorizon.com/wp-content/uploads/2022/06/spiderhead-1.jpg",
        trailer_src= "https://www.youtube.com/embed/BfsNfFoA0J0?controls=0",
        netflix_original= True
        )

    movie6 = Movie(
        movie_name= "What Happened To Monday", 
        director= "Tommy Wirkola",
        cast= "Noomi Rapace, Willem Dafoe, Glenn Close",
        writer= "Max Botkin, Kerry Williamson",
        genre1= 2,
        genre2= 8,
        movie_is= "Violent, Gritty",
        rating= "TV-MA" ,
        year= 2017,
        duration= "2h 3m", 
        description= "In a future with a strict one-child policy, six septuplets must avoid government detection while searching for their missing sister.",
        prev_img= "https://www.youtube.com/embed/hOiWSWLt-NA?controls=0",
        detail_img = "https://s3.amazonaws.com/static.rogerebert.com/uploads/review/primary_image/reviews/what-happened-to-monday-2017/What_Happened_to_Monday.jpg",
        trailer_src= "https://www.youtube.com/embed/hOiWSWLt-NA?controls=0",
        netflix_original= True
        )

    movie7 = Movie(
        movie_name= "Bird Box", 
        director= "Susanne Bier",
        cast= "Sandra Bullock, Trevante Rhodes, John Malkovich",
        writer= "Eric Heisserer",
        genre1= 2,
        genre2= 7,
        genre3= 5,
        movie_is= "Ominous, Chilling",
        rating= "R",
        year= 2018,
        duration= "2h 4m", 
        description= "Five years after an ominous unseen presence drives most of society to suicide, a survivor and her two children make a desperate bid to reach safety.",
        prev_img= "https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6g…kOxEBSwPPi5b-a5uPuFizHWBS2thzIAo4v_NPuv.jpg?r=ef5",
        detail_img = "https://s3-us-west-2.amazonaws.com/prd-rteditorial/wp-content/uploads/2019/01/03113538/bird-box-700x380.jpg",
        trailer_src= "https://www.youtube.com/embed/o2AsIXSh2xo?controls=0",
        netflix_original= True
        )

    movie8 = Movie(
        movie_name= "Bullet Train", 
        director= "David Leitch",
        cast= "Brad Pitt, Joey King, Aaron Taylor-Johnson",
        writer= "Zak Olkewicz",
        genre1= 7,
        genre2= 8,
        genre3= 3,
        movie_is= "Offbeat",
        rating= "R",
        year= 2022,
        duration= "2h 6m", 
        description= "Five assassins board a Japanese bullet train bound for Kyoto and come to discover that their seemingly separate missions are mysteriously linked.",
        prev_img= "https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6g…yUZWcTLTbxBihCCNzB0oKjMiEn9e6FwBg5Vga4.webp?r=83c",
        detail_img = "https://www.indiewire.com/wp-content/uploads/2022/08/Bullet-Train-trailer-still.jpeg",
        trailer_src= "https://www.youtube.com/embed/iUZ5H1g5CSg?controls=0"
        )

    movie9 = Movie(
        movie_name= "Shutter Island", 
        director= "Martin Scorsese",
        cast= "Leonardo DiCaprio, Mark Ruffalo, Ben Kingsley",
        writer= "Laeta Kalogridis",
        genre1= 9,
        genre2= 7,
        genre3= 4,
        movie_is= "Mind-Bending, Ominous",
        rating= "R",
        year= 2010,
        duration= "2h 18m", 
        description= "A U.S. marshal's troubling visions compromise his investigation into the disappearance of a patient from a hospital for the criminally insane.",
        prev_img= "https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6g…JGY8XkyAkYFGOEd2GEL37rqkKUd-ByGNvCEp2M.webp?r=0d6",
        detail_img = "https://www.slashfilm.com/img/gallery/shutter-island-revisited/intro-import.jpg",
        trailer_src= "https://www.youtube.com/embed/YDGldPitxic?controls=0",
        netflix_original= True
        )

    movie10 = Movie(
        movie_name= "Interstellar", 
        director= "Christopher Nolan",
        cast= "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
        writer= "Jonathan Nolan, Christopher Nolan",
        genre1= 5,
        genre2= 2,
        genre3= 4,
        movie_is= "Exciting, Chilling",
        rating= "PG-13",
        year= 2014,
        duration= "2h 49m", 
        description= "Earth's future has been riddled by disasters, famines, and droughts. There is only one way to ensure mankind's survival: Interstellar travel. A newly discovered wormhole in the far reaches of our solar system allows a team of astronauts to go where no man has gone before, a planet that may have the right environment to sustain human life.",
        prev_img= "https://ntvb.tmsimg.com/assets/p10543523_v_h8_at.jpg?w=960&h=540",
        detail_img = "https://images8.alphacoders.com/560/560736.jpg",
        trailer_src= "https://www.youtube.com/embed/0vxOhd4qlnA?controls=0",
        netflix_original= True
        )

    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.add(movie4)
    db.session.add(movie5)
    db.session.add(movie6)
    db.session.add(movie7)
    db.session.add(movie8)
    db.session.add(movie9)
    db.session.add(movie10)
    db.session.commit()

    


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_movies():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM movies")
        
    db.session.commit()
