from app.models import db, environment, SCHEMA
from app.models.tv_shows import TVShow

# Adds a demo user, you can add other users here if you want
def seed_tv():
    tv1 = TVShow(
        tv_name="Avatar",
        creators="Michael Dante DiMartino, Bryan Konietzko",
        cast="Zach Tyler, Mae Whitman, Jack De Sena, Dee Bradley Baker, Dante Basco, Jessie Flower, Mako Iwamatsu",
        # genre1=Kids TV 12,
        # genre2=TV Cartoons 13,
        # genre3=Fantasy TV Shows 14,
        tv_is="Exciting",
        rating="TV-Y7",
        year=2005,
        description="In a war-torn world of elemental magic, a young boy reawakens to undertake a dangerous mystic quest to fulfill his destiny as the Avatar, and bring peace to the world.",
        prev_img="https://wwwimage-us.pplusstatic.com/base/files/seo/atla_social_1200x627.jpg",
        detail_img ="https://www.slashfilm.com/img/gallery/nickelodeons-first-avatar-the-last-airbender-animated-movie-will-bring-the-gaang-back-together/l-intro-1658550631.jpg",
        trailer_src= "https://www.youtube.com/embed/ooVvH2IYz0w",
        num_seasons= "3 Seasons"
    )
    tv2 = TVShow(
        tv_name="Love, Death & Robots",
        creators="Tim Miller, David Fincher, Jennifer Miller, Josh Donen",
        cast="Joe Manganiello, Rosario Dawson, Seth Green, Michael B. Jordan",
        # genre1=Sci Fi TV 15,
        # genre2=TV Thrillers 16,
        # genre3=TV Horror 17,
        tv_is="Mind-Bending",
        rating="TV-MA",
        year=2019,
        description="Terrifying creatures, wicked surprises and dark comedy converge in this NSFW anthology of animated stories presented by Tim Miller and David Fincher.",
        prev_img="https://ntvb.tmsimg.com/assets/p16594930_b_h8_ac.jpg",
        detail_img ="https://m.media-amazon.com/images/M/MV5BNTMwMDUxOWYtMDEzZi00MTBmLWI1YzItOTVhMTYwNjM0MmIxXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg",
        trailer_src= "https://www.youtube.com/embed/wUFwunMKa4E",
        num_seasons= "3 Volumes"
    )
    tv3 = TVShow(
        tv_name="Sex Education",
        creators="Laurie Nunn",
        cast="Asa Butterfield, Gillian Anderson, Ncuti Gatwa",
        # genre1=British 18,
        # genre2=Teen TV Shows 19,
        # genre3=TV Dramas 20,
        tv_is="Raunchy, Irreverent, Heartfelt",
        rating="TV-MA",
        year=2019,
        description="A teenage boy with a sex therapist mother teams up with a high school classmate to set up an underground sex therapy clinic at school.",
        prev_img="https://criticcircle.com/wp-content/uploads/2021/09/Sex-Education-1.jpg",
        detail_img ="https://assets.teenvogue.com/photos/5e15e202e29ccb0008c312dc/16:9/w_2560%2Cc_limit/sexed-lede.jpg",
        trailer_src= "https://www.youtube.com/embed/Hd2ldTR-WpI",
        num_seasons= "3 Seasons"
    )
    tv4 = TVShow(
        tv_name="The Haunting of Hill House",
        creators="Mike Flanagan",
        cast="Michiel Huisman, Carla Gugino, Henry Thomas, Elizabeth Reaser, Kate Siegel, Victoria Pedretti, Oliver Jackson-Cohen",
        # genre1=TV Mysteries 21,
        # genre2=TV Dramas 20,
        # genre3=TV Horror 17,
        tv_is="Ominous, Chilling, Scary",
        rating="TV-MA",
        year=2018,
        description="Flashing between past and present, a fractured family confronts haunting memories of their old home and the terrifying events that drove them from it.",
        prev_img="https://flxt.tmsimg.com/assets/p15880871_b_h10_ab.jpg",
        detail_img ="https://variety.com/wp-content/uploads/2018/12/Haunting-of-Hill-House.jpg",
        trailer_src= "https://www.youtube.com/embed/3eqxXqJDmcY",
        num_seasons= "1 Season"
    )
    tv5 = TVShow(
        tv_name="Hannibal",
        creators="Bryan Fuller",
        cast="Hugh Dancy, Mads Mikkelsen, Caroline Dhavernas",
        # genre1=TV Horror 17,
        # genre2=Tv Thrillers 16,
        # genre3=Crime TV Show 22,
        tv_is="Mind-Bending, Gory, Dark",
        rating="TV-MA",
        year=2013,
        description="Explores the early relationship between renowned psychiatrist Hannibal Lecter and a young FBI criminal profiler who is haunted by his ability to empathize with serial killers.",
        prev_img="https://4.bp.blogspot.com/-XU6ckXIdJak/Vy_x20iWESI/AAAAAAAAAu8/7qOU81sgbXs_pUfPx_kGTUoKS71nmrSsgCLcB/s1600/LI2i3.jpg",
        detail_img ="https://bloody-disgusting.com/wp-content/uploads/2014/12/hannibal5.jpg",
        trailer_src= "https://www.youtube.com/embed/Es3B24z8fdA",
        num_seasons= "3 Seasons"
    )
    tv6 = TVShow(
        tv_name="Alice in Borderland",
        creators="Haro Aso",
        cast="Kento Yamazaki, Tao Tsuchiya, Nijirô Murakami",
        # genre1=Japanese 23,
        # genre2=Sci-Fi TV 15,
        # genre3=TV Shows Based on Manga 24,
        tv_is="Dark, Suspenseful",
        rating="TV-MA",
        year=2020,
        description="Arisu is a man without much money or luck. He is unemployed currently as well. Out of the blue a blinding light engulfs him one day in whose aftermath the city of Tokyo has lost all its inhabitants save Arisu and two friends. This is a dangerous and potentially fatal game of survival now in which they are forced to take part.",
        prev_img="https://flxt.tmsimg.com/assets/p18829068_b_h10_aa.jpg",
        detail_img ="https://cdn.mos.cms.futurecdn.net/KSDF9cn3NGgrCu6tJXkq3K.jpg",
        trailer_src= "https://www.youtube.com/embed/49_44FFKZ1M",
        num_seasons= "2 Seasons"
    )
    tv7 = TVShow(
        tv_name="Stranger Things",
        creators="The Duffer Brothers",
        cast="Millie Bobby Brown, Finn Wolfhard, Winona Ryder",
        # genre1=Sci-Fi TV 15,
        # genre2=Teen TV Shows 19,
        # genre3=TV Horror 17,
        tv_is="Ominous, Scary",
        rating="TV-14",
        year=2016,
        description="When a young boy disappears, his mother, a police chief and his friends must confront terrifying supernatural forces in order to get him back.",
        prev_img="https://cdn.wallpapersafari.com/78/47/A7PDtQ.jpg",
        detail_img ="https://occ-0-33-1009.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABXdoFBGXx_gQywX64x9I5gEetMlsMB-wM_vZC4VBpdoqOxNZQxTi-foCgZ_kGXllVTLiZeTPpHuD9UkvR9frMUdFRHKxVrAYUMuS.jpg",
        trailer_src= "https://www.youtube.com/embed/b9EkMc79ZSU",
        num_seasons= "4 Seasons"
    )
    tv8 = TVShow(
        tv_name="Squid Game",
        creators="Hwang Dong-hyuk",
        cast="Lee Jung-jae, Park Hae-soo, Hoyeon",
        # genre1=Korean 24,
        # genre2=TV Thrillers 16,
        # genre3=TV Dramas 20,
        tv_is="Suspenseful",
        rating="TV-MA",
        year=2021,
        description="Hundreds of cash-strapped players accept a strange invitation to compete in children's games. Inside, a tempting prize awaits with deadly high stakes. A survival game that has a whopping 45.6 billion-won prize at stake.",
        prev_img="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2022/04/Squid-Game-poster.jpg",
        detail_img ="https://occ-0-2186-3934.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABe1fA_q1l9tqtFkCK7xxnTUkhV3NHZDpPy7yF-YgiPUDPzGfeMlcRoKXiOfHl2UVx9oINILikJ1NaUYxpOnGKLAv_f49b5p3jyA7.jpg",
        trailer_src= "https://www.youtube.com/embed/oqxAJKy0ii4",
        num_seasons= "1 Season"
    )
    tv9 = TVShow(
        tv_name="Wednesday",
        creators="Alfred Gough, Miles Millar",
        cast="Jenna Ortega, Gwendoline Christie, Riki Lindhome, Christina Ricci",
        # genre1=TV Mysteries 21,
        # genre2=Crime TV Shows 22,
        # genre3=Fantasy TV Shows 14,
        tv_is="Deadpan",
        rating="TV-14",
        year=2022,
        description="Follows Wednesday Addams' years as a student, when she attempts to master her emerging psychic ability, thwart a killing spree, and solve the mystery that embroiled her parents.",
        prev_img="https://i.ytimg.com/vi/YGDLb7N21bY/maxresdefault.jpg",
        detail_img ="https://snworksceo.imgix.net/bdh/6c19bab8-1b40-4fc3-8f46-56c83f214069.sized-1000x1000.jpg",
        trailer_src= "https://www.youtube.com/embed/Di310WS8zLk",
        num_seasons= "1 Season"
    )
    tv10 = TVShow(
        tv_name="Black Mirror",
        creators="Charlie Brooker",
        cast="Daniel Lapaine, Hannah John-Kamen, Michaela Coel, Jessie Plemons, Cristin Milioti",
        # genre1=British 18,
        # genre2=Sci-Fi TV 15,
        # genre3=TV Thrillers 16,
        tv_is="Mind-Bending, Ominous",
        rating="TV-MA",
        year=2011,
        description="An anthology series exploring a twisted, high-tech multiverse where humanity's greatest innovations and darkest instincts collide.",
        prev_img="https://variety.com/wp-content/uploads/2017/08/black-mirror-logo.jpg",
        detail_img ="https://cdn.vox-cdn.com/thumbor/OZnNQGUKIW-4EEAD4DxcSIP05_s=/0x0:3200x1600/fit-in/1200x600/cdn.vox-cdn.com/uploads/chorus_asset/file/16317504/black_mirror_episodes.jpg",
        trailer_src= "https://www.youtube.com/embed/V0XOApF5nLU",
        num_seasons= "5 Seasons"
    )
    tv11 = TVShow(
        tv_name="Money Heist",
        creators="Álex Pina",
        cast="Úrsula Corberó, Álvaro Morte, Itziar Ituño",
        # genre1=Crime TV Shows 22,
        # genre2=Spanish 4,
        # genre3=TV Thrillers 16,
        tv_is="Suspensful, Exciting",
        rating="TV-MA",
        year=2017,
        description="An unusual group of robbers attempt to carry out the most perfect robbery in Spanish history - stealing 2.4 billion euros from the Royal Mint of Spain.",
        prev_img="https://static1.colliderimages.com/wordpress/wp-content/uploads/2021/08/money-heist-season-5.jpg",
        detail_img ="https://cdn.mos.cms.futurecdn.net/8NgbWjnZUq5zRV4orQfbJi.jpg",
        trailer_src= "https://www.youtube.com/embed/_InqQJRqGW4",
        num_seasons= "5 parts"
    )
    tv12 = TVShow(
        tv_name="The End of the F***ing World",
        creators="Charles Forsman",
        cast="Jessica Barden, Alex Lawther, Wunmi Mosaku, Stephen Wight, Gemma Whelan",
        # genre1=British 18,
        # genre2=Teen TV Shows 19,
        # genre3=TV Dramas 20,
        tv_is="Deadpan, Offbeat",
        rating="TV-MA",
        year=2017,
        description="James is 17 and is pretty sure he is a psychopath. Alyssa, also 17, is the cool and moody new girl at school. The pair make a connection and she persuades him to embark on a road trip in search of her real father.",
        prev_img="https://i.ytimg.com/vi/JoZ09nJNN28/maxresdefault.jpg",
        detail_img ="https://wallpapercave.com/wp/wp2398137.jpg",
        trailer_src= "https://www.youtube.com/embed/FruHLslczag",
        num_seasons= "2 Seasons"
    )


    db.session.add(tv1)
    db.session.add(tv2)
    db.session.add(tv3)
    db.session.add(tv4)
    db.session.add(tv5)
    db.session.add(tv6)
    db.session.add(tv7)
    db.session.add(tv8)
    db.session.add(tv9)
    db.session.add(tv10)
    db.session.add(tv11)
    db.session.add(tv12)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_tv():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tv_shows RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM tv_shows")
        
    db.session.commit()
