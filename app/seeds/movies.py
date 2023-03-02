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
        # genre1=1,
        # genre2=2,
        # genre3=3,
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
        # genre1= 4,
        # genre2= 5,
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
        # genre1= 5,
        # genre2= 1,
        # genre3= 8,
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
        # genre1= 3,
        # genre2= 6,
        # genre3=7
        movie_is= "Bittersweet, Romantic",
        rating= "R",
        year= 2019,
        duration= "1h 32m", 
        description= "On the heels of a blindsiding breakup, music journalist Jenny braces for a new beginning -- and one last adventure with her closest friends.",
        prev_img= "https://occ.a.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABSlNOgddyhfTKZIEYtWWwjpuSxhm9ebG3TJUJ5Yu_mhhtnSBvzYd1Yqp7tVVHbIMvywCORjZhm6x_rpkOFHlhuXc5Z9BC0Tako_c6_qYVHWy0leum-RrYOUot_5l9nRQESFhPw.jpg?r=7df",
        detail_img = "https://thecinemaholic.com/wp-content/uploads/2019/04/Someone-Great-Ending.jpg",
        trailer_src= "https://www.youtube.com/embed/BBd9gcrj2Wk?controls=0",
        netflix_original= True
        )

    movie5 = Movie(
        movie_name= "Spiderhead", 
        director= "Joseph Kosinski",
        cast= "Chris Hemsworth, Miles Teller, Jurnee Smollett",
        writer= "Rhett Reese, Paul Wernick",
        # genre1= 2,
        # genre2= 5,
        # genre3= 8,
        movie_is= "Offbeat",
        rating= "R",
        year= 2022,
        duration= "1h 47m", 
        description= "A prisoner in a state-of-the-art penitentiary begins to question the purpose of the emotion-controlling drugs he's testing for a pharmaceutical genius.",
        prev_img= "https://i0.wp.com/highoncinemaa.com/wp-content/uploads/2022/06/Spiderhead-Reviews-Roundup-Chris-Hemsworths-Best-Performance-Yet.jpg?fit=1604%2C870&ssl=1",
        detail_img = "https://media.wired.com/photos/62bce1c09c301780cc3296a2/master/pass/Spiderhead-Lacks-Charm-Culture-SH_JK_FP_099149_CC.jpg",
        trailer_src= "https://www.youtube.com/embed/BfsNfFoA0J0?controls=0",
        netflix_original= True
        )

    movie6 = Movie(
        movie_name= "What Happened To Monday", 
        director= "Tommy Wirkola",
        cast= "Noomi Rapace, Willem Dafoe, Glenn Close",
        writer= "Max Botkin, Kerry Williamson",
        # genre1= 2,
        # genre2= 8,
        #genre3=10
        movie_is= "Violent, Gritty",
        rating= "TV-MA" ,
        year= 2017,
        duration= "2h 3m", 
        description= "In a future with a strict one-child policy, six septuplets must avoid government detection while searching for their missing sister.",
        prev_img= "https://occ-0-58-990.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABZb1JZZT_wEWc6iWaLHqiQWwrSTmTejotmwG2TEe6Sg7wUe__pG6hNUxKSGGSvzG7VQwKVOnIRtWfn3Twzf0FdEaU2gsSBeOVEPryLOgmFQUq5XS5NYrF_ZNdjlMnsqKAXUI2Q.jpg?r=436",
        detail_img = "https://s3.amazonaws.com/static.rogerebert.com/uploads/review/primary_image/reviews/what-happened-to-monday-2017/What_Happened_to_Monday.jpg",
        trailer_src= "https://www.youtube.com/embed/hOiWSWLt-NA?controls=0",
        netflix_original= True
        )

    movie7 = Movie(
        movie_name= "Bird Box", 
        director= "Susanne Bier",
        cast= "Sandra Bullock, Trevante Rhodes, John Malkovich",
        writer= "Eric Heisserer",
        # genre1= 2,
        # genre2= 8,
        # genre3= 5,
        movie_is= "Ominous, Chilling",
        rating= "R",
        year= 2018,
        duration= "2h 4m", 
        description= "Five years after an ominous unseen presence drives most of society to suicide, a survivor and her two children make a desperate bid to reach safety.",
        prev_img= "https://occ-0-33-41.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABQ-Fi5X9KMeL6VSvn_HMJtFUzbnArBRh3mrqyNZSaDFr4LkeZcI2jxYZJ3T6O5RYaDbrtGGHQ4Wnmxamw5EkV6eibuikDMrDTy8iA7ujh_-NRk9X20dRz16Cs7SwXr2-6Ge-WA.jpg?r=ca8",
        detail_img = "https://s3-us-west-2.amazonaws.com/prd-rteditorial/wp-content/uploads/2019/01/03113538/bird-box-700x380.jpg",
        trailer_src= "https://www.youtube.com/embed/o2AsIXSh2xo?controls=0",
        netflix_original= True
        )

    movie8 = Movie(
        movie_name= "Bullet Train", 
        director= "David Leitch",
        cast= "Brad Pitt, Joey King, Aaron Taylor-Johnson",
        writer= "Zak Olkewicz",
        # genre1= 8,
        # genre2= 9,
        # genre3= 3,
        movie_is= "Offbeat",
        rating= "R",
        year= 2022,
        duration= "2h 6m", 
        description= "Five assassins board a Japanese bullet train bound for Kyoto and come to discover that their seemingly separate missions are mysteriously linked.",
        prev_img= "https://occ.a.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABVDdKjzrLi9DErgrVtSjCJIIAnj5vlTilGmIJNo3qy80pO2YMCMAOp75GGFXjkTE0eGJoa2ZaWFgF2Ue7VDAILOPJQtOsfgLzdgu.jpg?r=397",
        detail_img = "https://www.indiewire.com/wp-content/uploads/2022/08/Bullet-Train-trailer-still.jpeg",
        trailer_src= "https://www.youtube.com/embed/iUZ5H1g5CSg?controls=0"
        )

    movie9 = Movie(
        movie_name= "Shutter Island", 
        director= "Martin Scorsese",
        cast= "Leonardo DiCaprio, Mark Ruffalo, Ben Kingsley",
        writer= "Laeta Kalogridis",
        # genre1= 10,
        # genre2= 6,
        # genre3= 5,
        movie_is= "Mind-Bending, Ominous",
        rating= "R",
        year= 2010,
        duration= "2h 18m", 
        description= "A U.S. marshal's troubling visions compromise his investigation into the disappearance of a patient from a hospital for the criminally insane.",
        prev_img= "https://i0.wp.com/www.irishfilmcritic.com/wp-content/uploads/2019/11/Shutter-Island.jpg?fit=1392%2C696&ssl=1",
        detail_img = "https://www.slashfilm.com/img/gallery/shutter-island-revisited/intro-import.jpg",
        trailer_src= "https://www.youtube.com/embed/YDGldPitxic?controls=0",
        lex_top=True
        )

    movie10 = Movie(
        movie_name= "Interstellar", 
        director= "Christopher Nolan",
        cast= "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
        writer= "Jonathan Nolan, Christopher Nolan",
        # genre1= 5,
        # genre2= 2,
        # genre3= 9,
        movie_is= "Exciting, Chilling",
        rating= "PG-13",
        year= 2014,
        duration= "2h 49m", 
        description= "Earth's future has been riddled by disasters, famines, and droughts. There is only one way to ensure mankind's survival: Interstellar travel.",
        prev_img= "https://ntvb.tmsimg.com/assets/p10543523_v_h8_at.jpg?w=960&h=540",
        detail_img = "https://images8.alphacoders.com/560/560736.jpg",
        trailer_src= "https://www.youtube.com/embed/0vxOhd4qlnA?controls=0",
        lex_top=True
        )

    movie11 = Movie(
        movie_name= "Glass Onion: A Knives Out Mystery", 
        director= "Rian Johnson",
        cast= "Daniel Craig, Edward Norton, Kate Hudson",
        writer= "Rian Johnson",
        # genre1= 5,
        # genre2= 3,
        # genre3= 10,
        movie_is= "Offbeat, Witty",
        rating= "PG-13",
        year= 2022,
        duration= "2h 19m", 
        description= "World-famous detective Benoit Blanc heads to Greece to peel back the layers of a mystery surrounding a tech billionaire and his eclectic crew of friends.",
        prev_img= "https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABTc_7_sLJTeV53u7JhE96G9iXXy3IDanPm8P13mpug-VmoXa-Ff5ff6zd6mDWsU3ME262EZXiVDhQx1PygCDdLtqwUnhkPEI3vV5cwwgmbTSsYCMG7QTdfHsM9rrb9j10k9YGpvjlWzttHYJh64kl-SW_ID2-wwpq0fjUAoImlcUcTZHsdebgUeyhiZSxY4.jpg?r=005",
        detail_img = "https://occ-0-37-34.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABekeLR1_UTvm-LGCdAfnoJm8ghWkXLS8izpG3FQ9ok9fwONCMPKSy6iLZz82y9QqnSgbgBBJNw0DsROmZ3Ye3c0ERgCAp7yLMvy5.jpg?r=878",
        trailer_src= "https://www.youtube.com/embed/gj5ibYSz8C0?controls=0",
        netflix_original= True
        )

    movie12 = Movie(
        movie_name= "Velvet Buzzsaw", 
        director= "Dan Gilroy",
        cast= "Jake Gyllenhaal, Rene Russo, Zawe Ashton",
        writer= "Dan Gilroy",
        # genre1= 5,
        # genre2= 10,
        movie_is= "Cerebral",
        rating= "R",
        year= 2019,
        duration= "1h 52m", 
        description= "A feared critic, an icy gallery owner and an ambitious assistant snap up a recently deceased artist's stash of paintings -- with dire consequences.",
        prev_img= "https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABU9ztP6Jm7POyIV1q9CCL_UbNXS6RzHl4zqDUnhx0KdBCwiMGqXYja47lfPEHyyqgydKLnijmtxyEXlPNIsC1PoIVrKx7rDfnVunWpJ6aIOgoW7upfDZlUG1nny-h-4Udoxd.jpg?r=e0e",
        detail_img = "https://d2xl3i29vwgm2y.cloudfront.net/media/static/4b/c0/4bc0bacc-4c91-438c-b7b5-1b1297e949a9/1.jpg",
        trailer_src= "https://www.youtube.com/embed/XdAR-lK43YU?controls=0",
        netflix_original= True
        )

    movie13 = Movie(
        movie_name= "Spider-Man: Into the Spider-Verse", 
        director= "Bob Persichetti",
        cast= "Shameik Moore, Jake Johnson, Hailee Steinfeld",
        writer= "Phil Lord, Rodney Rothman",
        # genre1= 9,
        # genre2= 3,
        movie_is= "Exciting",
        rating= "PG",
        year= 2018,
        duration= "1h 57m", 
        description= "Teen Miles Morales becomes the Spider-Man of his universe, and must join with five spider-powered individuals from other dimensions to stop a threat for all realities.",
        prev_img= "https://hbomax-images.warnermediacdn.com/images/GYWkQzQT5VKTDwgEAAACb/tileburnedin?size=1280x720&partner=hbomaxcom&v=bb23236b5edf9b0260ae882bbbcbd679&host=art-gallery.api.hbo.com&language=en-us&w=1280",
        detail_img = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/846a9086-8a40-43e0-aa10-2fc7d6d73730/dcv16z1-7c3d92fe-c484-4580-82e8-c6220c2626f2.png/v1/fill/w_900,h_463,q_80,strp/spider_man__into_the_spider_verse___wallpaper_by_mintmovi3_dcv16z1-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDYzIiwicGF0aCI6IlwvZlwvODQ2YTkwODYtOGE0MC00M2UwLWFhMTAtMmZjN2Q2ZDczNzMwXC9kY3YxNnoxLTdjM2Q5MmZlLWM0ODQtNDU4MC04MmU4LWM2MjIwYzI2MjZmMi5wbmciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.I9RsR-vuiJdbK6LjbHtanINuGiH8fwSS_Xe8UdS96UE",
        trailer_src= "https://www.youtube.com/embed/cqGjhVJWtEg?controls=0",
        lex_top=True
        )

    movie14 = Movie(
        movie_name= "Harry Potter and the Goblet of Fire", 
        director= "Mike Newell",
        cast= "Daniel Radcliffe, Emma Watson, Rupert Grint",
        writer= "Steve Kloves, J.K. Rowling",
        # genre1= 8,
        # genre2= 5,
        # genre3= 6,
        movie_is= "Magical, Exciting",
        rating= "PG-13",
        year= 2005,
        duration= "2h 37m", 
        description= "Harry Potter finds himself competing in a hazardous tournament between rival schools of magic, but he is distracted by recurring nightmares.",
        prev_img= "https://hbomax-images.warnermediacdn.com/images/GXssOeAtVmlVGwwEAAABR/tileburnedin?size=1280x720&partner=hbomaxcom&v=57cd564a8452ab3931c9463515a0da3e&host=art-gallery.api.hbo.com&language=en-us&w=1280",
        detail_img = "https://www.pluggedin.com/wp-content/uploads/2019/12/harry-potter-and-the-goblet-of-fire.jpg",
        trailer_src= "https://www.youtube.com/embed/4xkFJgcCQRE?controls=0",
        lex_top=True
        )
    
    movie15 = Movie(
        movie_name= "Zoolander", 
        director= "Ben Stiller",
        cast= "Ben Stiller, Owen Wilson, Christine Taylor",
        writer= "Drake Sather, Ben Stiller, John Hamburg",
        # genre1= 3,
        # genre2= 11,
        movie_is= "Irreverant, Goofy",
        rating= "PG-13",
        year= 2001,
        duration= "1h 30m", 
        description= "At the end of his career, a clueless fashion model is brainwashed to kill the Prime Minister of Malaysia.",
        prev_img= "https://image.tmdb.org/t/p/w780/7vVVSkFauLKvbSxX1eYwcij074F.jpg",
        detail_img = "https://media.architecturaldigest.com/photos/56be5970f80b269a4abb014e/2:1/w_4928,h_2464,c_limit/zoolander-2-movie-set-design-004.jpg",
        trailer_src= "https://www.youtube.com/embed/YtQq0T3ExLs?controls=0",
        lex_top=True
        )
    
    movie16 = Movie(
        movie_name= "Arrival", 
        director= "Denis Villenueve",
        cast= "Amy Adams, Jeremy Renner, Forest Whitaker",
        writer= "Eric Heisserer, Ted Chiang",
        # genre1= 5,
        # genre2= 2,
        # genre3= 9,
        movie_is= "Suspenseful, Exciting",
        rating= "PG-13",
        year= 2016,
        duration= "1h 56m", 
        description= "A linguist works with the military to communicate with alien lifeforms after twelve mysterious spacecraft appear around the world.",
        prev_img= "https://occ.a.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABUHSnfcPVTUcNhlA6ZxJsQ5yQUPDqAbuUceVp0YMVl7p8zIjmYZzvjhWVWlKubF_F9CXqmkCgYOYPTGEz_JbWZql1Brbd-I8S8MP.jpg?r=1aa",
        detail_img = "https://s.studiobinder.com/wp-content/uploads/2010/03/Arrival-Video-Essay-How-to-Balance-Fear-and-Intrigue-WP.jpg",
        trailer_src= "https://www.youtube.com/embed/tFMo3UJ4B4g?controls=0",
        lex_top=True
        )
    
    movie17 = Movie(
        movie_name= "Pulp Fiction", 
        director= "Quentin Tarantino",
        cast= "John Travolta, Uma Thurman, Samuel L. Jackson",
        writer= "Quentin Tarantino, Roger Avary",
        # genre1= 5,
        # genre2= 9,
        movie_is= "Gritty, Exciting",
        rating= "R",
        year= 1994,
        duration= "2h 34m", 
        description= "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        prev_img= "https://www.sho.com/site/image-bin/images/0_0_3507086/0_0_3507086_00h_1280x640.jpg",
        detail_img = "https://www.today.it/~media/horizontal-hi/1419668529936/pulp-fiction-ballo-2.jpg",
        trailer_src= "https://www.youtube.com/embed/5ZAhzsi1ybM?controls=0",
        lex_top=True
        )
    
    movie18 = Movie(
        movie_name= "The Lovely Bones", 
        director= "Peter Jackson",
        cast= "Rachel Weisz, Mark Wahlberg, Saoirse Ronan",
        writer= "Fran Walsh, Alice Sebold",
        # genre1= 5,
        # genre2= 8,
        # genre3= 6,
        movie_is= "Suspenseful",
        rating= "PG-13",
        year= 2009,
        duration= "2h 15m", 
        description= "Centers on a young girl who has been murdered and watches over her family - and her killer - from purgatory. She must weigh her desire for vengeance against her desire for her family to heal.",
        prev_img= "https://img3.hulu.com/user/v3/artwork/a90a24ff-e8e8-4059-943e-9a1fda060186?base_image_bucket_name=image_manager&base_image=2e0ab599-f934-4b2b-83d2-8d929fccf659&region=US&format=jpeg&size=952x536",
        detail_img = "https://m.media-amazon.com/images/M/MV5BMTUwNjc2Mjg5M15BMl5BanBnXkFtZTcwMjAzNzAxMw@@._V1_.jpg",
        trailer_src= "https://www.youtube.com/embed/lTBeK-fwyQs?controls=0",
        lex_top=True
        )
    
    movie19 = Movie(
        movie_name= "The Dark Knight", 
        director= "Christopher Nolan",
        cast= "Christian Bale, Heath Ledger, Aaron Eckhart",
        writer= "Jonathan Nolan, David S. Goyer",
        # genre1= 9,
        # genre2= 5,
        movie_is= "Exciting",
        rating= "PG-13",
        year= 2008,
        duration= "2h 32m", 
        description= "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        prev_img= "https://occ-0-34-41.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABTQpo96D_Ag7ZsiDNLdWUjM73ShPJR4Xj63AKD9lYKMohCTTYD2RcWfII8TtbNuV3ntf5KIuUkyHXqLJzk-_nyGsVjU5oU2y7pzR.jpg?r=157",
        detail_img = "https://www.slashfilm.com/img/gallery/how-joker-would-have-played-a-role-in-the-dark-knight-rises/l-intro-1648651771.jpg",
        trailer_src= "https://www.youtube.com/embed/_PZpmTj1Q8Q?controls=0",
        lex_top=True
        )
    
    movie20 = Movie(
        movie_name= "The Princess and the Frog", 
        director= "Ron Clements, John Musker",
        cast= "Anika Noni Rose, Keith David, Oprah Winfrey",
        writer= "Ron Clements, John Musker, Greg Erb",
        # genre1= 11,
        # genre2= 6,
        # genre3= 3,
        movie_is= "Magical, For Children",
        rating= "G",
        year= 2009,
        duration= "1h 37m", 
        description= "A waitress, desperate to fulfill her dreams as a restaurant owner, is set on a journey to turn a frog prince back into a human being, but she has to face the same problem after she kisses him.",
        prev_img= "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/6E4425084B8F6CEDC2A4A983A71CC783BA2F694229C89E7AA9F1C204E169AC64/scale?width=1200&aspectRatio=1.78&format=jpeg",
        detail_img = "https://imagesvc.meredithcorp.io/v3/mm/image?q=60&c=sc&rect=0%2C211%2C2000%2C1211&poi=%5B1540%2C346%5D&w=2000&h=1000&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2021%2F08%2F21%2FPrincess-and-the-Frog-1.jpg",
        trailer_src= "https://www.youtube.com/embed/uQBy6jqbmlU?controls=0",
        lex_top=True
        )

    movie21 = Movie(
        movie_name= "The Grand Budapest Hotel", 
        director= "Wes Anderson",
        cast= "Ralph Fiennes, Murray Abraham, Mathieu Amalric",
        writer= "Stefan Zweig, Wes Anderson, Hugo Guinness",
        # genre1= 5,
        # genre2= 6,
        movie_is= "Beautiful, Exciting",
        rating= "R",
        year= 2014,
        duration= "1h 39m", 
        description= "A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel's glorious years under an exceptional concierge.",
        prev_img= "https://ntvb.tmsimg.com/assets/p10295153_v_h8_ad.jpg?w=1280&h=720",
        detail_img = "https://s26162.pcdn.co/wp-content/uploads/2021/11/budapest-feature.jpg",
        trailer_src= "https://www.youtube.com/embed/1Fg5iWmQjwk?controls=0"
        )
    movie21 = Movie(
        movie_name= "The Grand Budapest Hotel", 
        director= "Wes Anderson",
        cast= "Ralph Fiennes, Murray Abraham, Mathieu Amalric",
        writer= "Stefan Zweig, Wes Anderson, Hugo Guinness",
        # genre1= 5,
        # genre2= 6,
        movie_is= "Beautiful, Exciting",
        rating= "R",
        year= 2014,
        duration= "1h 39m", 
        description= "A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel's glorious years under an exceptional concierge.",
        prev_img= "https://ntvb.tmsimg.com/assets/p10295153_v_h8_ad.jpg?w=1280&h=720",
        detail_img = "https://s26162.pcdn.co/wp-content/uploads/2021/11/budapest-feature.jpg",
        trailer_src= "https://www.youtube.com/embed/1Fg5iWmQjwk?controls=0"
        )
    movie22 = Movie(
        movie_name= "Elf", 
        director= "Jon Favreau",
        cast= "Will Ferrell, James CaanBob, Newhart",
        writer= "David Berenbaum",
        # genre1= 3,
        # genre2= 11,
        movie_is= "Heart Warming, For Children",
        rating= "PG",
        year= 2003,
        duration= "1h 37m", 
        description= "Raised as an oversized elf, Buddy travels from the North Pole to New York City to meet his biological father, Walter Hobbs, who doesn't know he exists and is in desperate need of some Christmas spirit.",
        prev_img= "https://keithandthemovies.files.wordpress.com/2012/12/elf.jpg",
        detail_img = "https://hips.hearstapps.com/hmg-prod/images/will-ferrell-buddy-the-elf-1541700803.jpg",
        trailer_src= "https://www.youtube.com/embed/14o38xfHlXc?controls=0"
        )
    movie23 = Movie(
        movie_name= "Get Out", 
        director= "Jordan Peele",
        cast= "Daniel Kaluuya, Allison Williams, Bradley Whitford",
        writer= "Jordan Peele",
        # genre1= 9,
        # genre2= 10,
        #genre3= 5,
        movie_is= "Exciting, New",
        rating= "R",
        year= 2017,
        duration= "1h 44m", 
        description= "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.",
        prev_img= "http://noirehistoir.com/wp-content/uploads/2019/10/Get-Out-Feature-Image.jpg",
        detail_img = "https://thehoya.com/wp-content/uploads/2017/02/B6_GetOut_youtube.png",
        trailer_src= "https://www.youtube.com/embed/DzfpyUB60YY?controls=0"
        )
    movie24 = Movie(
        movie_name= "Léon: The Professional", 
        director= "Luc Besson",
        cast= "Jean Reno, Gary Oldman, Natalie Portman",
        writer= "Luc Besson",
        # genre1= 9,
        # genre2= 5,
        movie_is= "Intense, Gripping",
        rating= "R",
        year= 1994,
        duration= "1h 50m", 
        description= "12-year-old Mathilda is reluctantly taken in by Léon, a professional assassin, after her family is murdered. An unusual relationship forms as she becomes his protégée and learns the assassin's trade.",
        prev_img= "https://e7.pngegg.com/pngimages/285/446/png-clipart-mathilda-film-1080p-high-definition-video-720p-leon-the-professional-film-poster-weapon.png",
        detail_img = "https://assets.mubicdn.net/images/film/168/image-w856.jpg",
        trailer_src= "https://www.youtube.com/embed/jawVxq1Iyl0?controls=0"
        )
    movie25 = Movie(
        movie_name= "Donnie Darko", 
        director= "Richard Kelly",
        cast= "Jake Gyllenhaal, Jena MaloneMary, McDonnell",
        writer= "Richard Kelly",
        # genre1= 2,
        # genre2= 5,
        #genre3= 10,
        movie_is= "Enigmatic, Thought-provoking",
        rating= "R",
        year= 2001,
        duration= "1h 53m", 
        description= "After narrowly escaping a bizarre accident, a troubled teenager is plagued by visions of a man in a large rabbit suit who manipulates him to commit a series of crimes.",
        prev_img= "https://64.media.tumblr.com/b61f702092b743576933e8806c29e2c5/a3a68366972ad0d4-0a/s1280x1920/ef6f979e0c74134ee073893d28f61a4ecc417bae.pnj",
        detail_img = "https://images.mubicdn.net/images/film/159/cache-33084-1617107095/image-w1280.jpg",
        trailer_src= "https://www.youtube.com/embed/rPeGaos7DB4?controls=0"
        )
    movie26 = Movie(
        movie_name= "Hitch", 
        director= "Andy Tennant",
        cast= "Will Smith, Eva Mendes, Kevin James",
        writer= "Kevin Bisch",
        # genre1= 7,
        # genre2= 3,
        movie_is= "Romantic, Lighthearted",
        rating= "PG-13",
        year= 2005,
        duration= "1h 58m", 
        description= "A smooth-talking man falls for a hardened columnist while helping a shy accountant woo a beautiful heiress.",
        prev_img= "https://ntvb.tmsimg.com/assets/p35562_v_h8_an.jpg",
        detail_img = "https://imagesvc.meredithcorp.io/v3/mm/image?q=60&c=sc&poi=face&w=2000&h=1000&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2019%2F10%2F000029121-2000.jpg",
        trailer_src= "https://www.youtube.com/embed/dMaq_pfxs-0?controls=0"
        )
    movie27 = Movie(
        movie_name= "Scott Pilgrim vs. the World", 
        director= "Edgar Wright",
        cast= "Michael Cera, Mary Elizabeth Winstead, Kieran Culkin",
        writer= "Michael Bacall, Edgar Wright, Bryan Lee O'Malley",
        # genre1= 9,
        # genre2= 7,
        #genre3= 3,
        movie_is= "Whimsical, Irreverent",
        rating= "PG-13",
        year= 2010,
        duration= "1h 52m", 
        description= "In a magically realistic version of Toronto, a young man must defeat his new girlfriend's seven evil exes one by one in order to win her heart.",
        prev_img= "https://popculturalstudies.files.wordpress.com/2016/11/scott-pilgrim-8.jpg",
        detail_img = "https://static01.nyt.com/images/2010/08/13/arts/13scott-span/13scott-span-articleLarge.jpg",
        trailer_src= "https://www.youtube.com/embed/7wd5KEaOtm4?controls=0"
        )
    movie28 = Movie(
        movie_name= "Deadpool", 
        director= "Tim Miller",
        cast= "Ryan Reynolds, Morena Baccarin, T.J. Miller",
        writer= "Rhett Reese, Paul Wernick",
        # genre1= 3,
        # genre2= 9,
        #genre3= 7,
        movie_is= "Witty, Irreverent",
        rating= "R",
        year= 2016,
        duration= "1h 48m", 
        description= "A wisecracking mercenary gets experimented on and becomes immortal but ugly, and sets out to track down the man who ruined his looks.",
        prev_img= "https://staticg.sportskeeda.com/editor/2022/01/74d3c-16426630332228-1920.jpg",
        detail_img = "https://m.media-amazon.com/images/M/MV5BMzYyNjI0MzA3M15BMl5BanBnXkFtZTgwMDA3Nzc5NzE@._V1_.jpg",
        trailer_src= "https://www.youtube.com/embed/ONHBaC-pfsk?controls=0"
        )
    movie29 = Movie(
        movie_name= "Eternal Sunshine of the Spotless Mind", 
        director= "Michel Gondry",
        cast= "Jim Carrey, Kate Winslet, Tom Wilkinson",
        writer= "Charlie Kaufman, Michel Gondry, Pierre Bismuth",
        # genre1= 7,
        # genre2= 3,
        movie_is= "Intricate, Poignant",
        rating= "R",
        year= 2004,
        duration= "1h 48m", 
        description= "When their relationship turns sour, a couple undergoes a medical procedure to have each other erased from their memories for ever.",
        prev_img= "https://keithandthemovies.files.wordpress.com/2014/03/eternalposter.jpg",
        detail_img = "https://www.hollywoodreporter.com/wp-content/uploads/2016/10/eternal_sunshine_of_the_spotless_mind_-_kate_winslet_-_jim_carey_-_h_-_2016.jpg",
        trailer_src= "https://www.youtube.com/embed/yE-f1alkq9I?controls=0"
        )
    movie30 = Movie(
        movie_name= "Spy Kids", 
        director= "Robert Rodriguez",
        cast= "Alexa PenaVega, Daryl Sabara, Antonio Banderas",
        writer= "Robert Rodriguez",
        # genre1= 9,
        # genre2= 11,
        movie_is= "Adventurous, Whimsical",
        rating= "PG",
        year= 2001,
        duration= "1h 28m", 
        description= "Using high tech gadgets, two kids have to save their reactivated OSS top spy parents when they're taken by an evil, high tech enemy.",
        prev_img= "https://occ-0-55-41.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABVi8Vpnx85AOYD5YgbF6lDFfwZ5VspsjtAJ6bm9H8CzLOjU9Adw0V-gtjw88X2di8lAndAdssHdnV6zZ18efOA8jea6XnNCY2d_2.jpg",
        detail_img = "https://pyxis.nymag.com/v1/imgs/28a/90a/61814819a1f1b78862c093f00ea706aad5-tony-shalhoub-spy-kids-role-call-lede-.2x.rsocial.w600.jpg",
        trailer_src= "https://www.youtube.com/embed/GE5aHKJp6HI?controls=0"
        )
    movie31 = Movie(
        movie_name= "The Parent Trap", 
        director= "Nancy Meyers",
        cast= "Lindsay Lohan, Dennis Quaid, Natasha Richardson",
        writer= "Erich Kästner, David Swift, Nancy Meyers",
        # genre1= 7,
        # genre2= 11,
        movie_is= "Heartwarming, Entertaining",
        rating= "PG",
        year= 1998,
        duration= "2h 8m", 
        description= "Identical twins Annie and Hallie, separated at birth and each raised by one of their biological parents, discover each other for the first time at summer camp and make a plan to bring their wayward parents back together.",
        prev_img= "https://www.hollywoodfl.org/ImageRepository/Document?documentID=20417",
        detail_img = "https://d23.com/app/uploads/2017/02/1180w-600h_a-to-z-the-parent-trap-1998.jpg",
        trailer_src= "https://www.youtube.com/embed/PMAhVpgzmRU?controls=0"
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
    db.session.add(movie11)
    db.session.add(movie12)
    db.session.add(movie13)
    db.session.add(movie14)
    db.session.add(movie15)
    db.session.add(movie16)
    db.session.add(movie17)
    db.session.add(movie18)
    db.session.add(movie19)
    db.session.add(movie20)
    db.session.add(movie21)
    db.session.add(movie22)
    db.session.add(movie23)
    db.session.add(movie24)
    db.session.add(movie25)
    db.session.add(movie26)
    db.session.add(movie27)
    db.session.add(movie28)
    db.session.add(movie29)
    db.session.add(movie30)
    db.session.add(movie31)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_movies():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.movies RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM movies")
        
    db.session.commit()
