from app.models import db, environment, SCHEMA
from app.models.tv_show_episodes import TVShowEpisodes

def seed_tv_episodes():
    ##avatar
    tv_episode1 = TVShowEpisodes(
        tv_id=1,
        ep_number=1,
        ep_name="The Awakening",
        ep_description="Katara and Sokka make a startling discovery while fishing: a boy frozen in an iceberg, perfectly preserved and -- amazingly -- alive.",
        ep_duration="23m",
        ep_poster="https://pictures.betaseries.com/banners/episodes/2187/5afd9cf3682bb98c2d7ea6d145f6162b.jpg"
    )
    tv_episode2 = TVShowEpisodes(
        tv_id=1,
        ep_number=2,
        ep_name="The Avatar Returns",
        ep_description="Aang must learn how to control his powers and face off against Zuko, who has been sent to capture him.",
        ep_duration="23m",
        ep_poster="https://occ-0-784-1007.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABVzCEdYDyCcokRCTqZ4_R-z4RFgAyyHsNkISO_KENe07-EOahV5BGvDFgzeGb_BtKtAWf2ZzxwjT9klcT58gZvi50GZJgDgwr_dqQ6JE3NIQUQ7gEbku9l--.jpg"
    )
    tv_episode3 = TVShowEpisodes(
        tv_id=1,
        ep_number=3,
        ep_name="The Southern Air Temple",
        ep_description="Aang discovers that the Fire Nation has destroyed his people's temple and everyone he knew.",
        ep_duration="24m",
        ep_poster="https://occ-0-784-1007.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABY-he8kWysvx7aEvIM7CcKWfkbbaF_qVZYA1J7UoEv9phDs3T0gbL-tCc9YEeJ42i9ZMoPHI39iIVy0D4NV4W2SznG2Xfnpwo3zjKOPpJdcgcS7gz9aC8HpS.jpg"
    )
    tv_episode4 = TVShowEpisodes(
        tv_id=1,
        ep_number=4,
        ep_name="The Warriors of Kyoshi",
        ep_description="Aang and his friends visit a group of female warriors, but their visit is cut short when they are captured by the Fire Nation.",
        ep_duration="23m",
        ep_poster="https://occ-0-784-1007.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABRhyRSMwNheEt3ABjDT5vnUAtjPTrJncQrKbLpH_gWSXLauM6ZwrPVHzS25A6IrurWOM-5Vo5RVyxhnWuJ1GIt21H4zYlyp_E7cz-YDh_T1b71fE6YJY1Dhw.jpg"
    )
    tv_episode5 = TVShowEpisodes(
        tv_id=1,
        ep_number=5,
        ep_name="The King of Omashu",
        ep_description="Aang and his friends visit the city of Omashu, where they must face off against the eccentric King Bumi.",
        ep_duration="24m",
        ep_poster="https://occ-0-784-1007.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABUURj0MUHhtyK84wShyChyZdQn8ktDRSrl6W_ewy13IwZfb0lxcFuuHvcNd1pvNUcWql71l76TNgv6NoNytVVu49ZBWLqvwu5kWAuxf1r7EqGd-rpq9nYEAu.jpg"
    )
    tv_episode6 = TVShowEpisodes(
        tv_id=1,
        ep_number=6,
        ep_name="Imprisoned",
        ep_description="Aang and his friends help a group of Earth Kingdom prisoners escape from a Fire Nation prison.",
        ep_duration="24m",
        ep_poster="https://occ-0-784-1007.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABdbSm-5Mtu-G78NvCH5uuFVsO93TfdEIaffcIE3g-XcyU_TjFV4FluZDeKbFUPnjB_NLS72mSqpsehO3gTYd8T6ERnp-WRHQaSqjeeb3gQHaZiKBF0JvDIHF.jpg"
    )
    tv_episode7 = TVShowEpisodes(
        tv_id=1,
        ep_number=7,
        ep_name="The Spirit World: Winter Solstice, Part 1",
        ep_description="Aang travels to the Spirit World to find the Avatar Spirit and seek advice from the previous Avatar.",
        ep_duration="24m",
        ep_poster="https://occ-0-784-1007.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABeuqsoM8EKHrEhw-Mm5S13MHMxb1T4VsDHN23gUfkdbZgIQU3s_n69p5LUEw04V0rKf8dEgFpslrJxfLVAYZtURA2TYNDnMawTKRwMbY4KhdckaGSnzT0UxX.jpg"
    )
    tv_episode8 = TVShowEpisodes(
        tv_id=1,
        ep_number=8,
        ep_name="Avatar Roku: Winter Solstice, Part 2",
        ep_description="Aang must help Avatar Roku stop the Fire Nation from taking over the world on the day of the winter solstice.",
        ep_duration="23m",
        ep_poster="https://occ-0-784-1007.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABeRKQsqvWQrB3QPUffKpTyZTueuAGGBaOfWlW6Jn_Gf_dPqS0O947oTOU3wJhmx3Sh1uGMT0mNXB2KyKqMWb3YlwwOCAgyI3LspoeyChIkTlBAY49rVzZaaO.jpg"
    )
    tv_episode9 = TVShowEpisodes(
        tv_id=1,
        ep_number=9,
        ep_name="The Waterbending Scroll",
        ep_description="Aang, Katara, and Sokka find themselves in possession of a valuable Waterbending scroll, which they refuse to sell to pirates.",
        ep_duration="24m",
        ep_poster="https://occ-0-784-1007.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABePU_neCP7_4Ju4kXGb5NqYQlMZNcPkCQjQvGuKB4RLbs_IgB8TfkNQKk1ZYdUtzCYdogW9etHu427tecQBdN2Kdypkwd3qi5TBfIlR7gT0DNHZt9CM_pRMQ.jpg"
    )
    tv_episode10 = TVShowEpisodes(
        tv_id=1,
        ep_number=10,
        ep_name="Jet",
        ep_description="The gang meets Jet, a charismatic and mysterious freedom fighter who leads a band of rebels against the Fire Nation.",
        ep_duration="24m",
        ep_poster="https://occ-0-784-1007.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABdYazuV_SzqeGlWbZNRalrUmBhdDBgAkAdvhAb4j_RxM9D3bJmCxgRx49Ij4ni0kK3qRDaCQ06FtKPyqI4VNPlRRNjZNVG_WDwNYPn2E7adZlpEdYKoyHbX8.jpg"
    )
    ##Love, Death & Robots
    tv_episode11 = TVShowEpisodes(
        tv_id=2,
        ep_number=1,
        ep_name="THREE ROBOTS",
        ep_description="Long after the fall of humanity, three robots embark on a sightseeing tour of a post-apocalyptic city.",
        ep_duration="11m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABbmfWue6FiAfvqYStsj5MvwZxyfz4MjPEfSglAsZZgYFgAPqzpgQJoaWtSkvDi51Q93KMTmbUNTRGboONNvQeV7oZVo-C_Z49V01Idj9GiKXhJTAcFvvQOGZ.jpg"
    )
    tv_episode12 = TVShowEpisodes(
        tv_id=2,
        ep_number=2,
        ep_name="BEYOND THE AQUILA DRIFT",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode13 = TVShowEpisodes(
        tv_id=2,
        ep_number=3,
        ep_name="ICE AGE",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode14 = TVShowEpisodes(
        tv_id=2,
        ep_number=4,
        ep_name="SONNIE'S EDGE",
        ep_description="In the underground world of 'Beastie' fights, Sonnie is unbeatable -- as long as she keeps her edge.",
        ep_duration="17m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABRVrTnTjZOkiTV-7n9nLy1WVtihbikc14ZV7bbq8zSluE7xvBJ5Q5Y00AS5h5dswBojFuswR6Np_Jah0-W0cW_7ViW1slHsp6KVCZq3gZf-5WFRpGZv_qrcEiQ.jpg"
    )
    tv_episode15 = TVShowEpisodes(
        tv_id=2,
        ep_number=5,
        ep_name="WHEN THE YOGURT TOOK OVER",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode16 = TVShowEpisodes(
        tv_id=2
        ep_number=6,
        ep_name="THE SECRET WAR",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode17 = TVShowEpisodes(
        tv_id=2
        ep_number=7,
        ep_name="SUCKER OF SOULS",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode18 = TVShowEpisodes(
        tv_id=2
        ep_number=8,
        ep_name="THE WITNESS",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode19 = TVShowEpisodes(
        tv_id=2,
        ep_number=9,
        ep_name="SUITS",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode20 = TVShowEpisodes(
        tv_id=2,
        ep_number=10,
        ep_name="GOOD HUNTING",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode21 = TVShowEpisodes(
        tv_id=2,
        ep_number=11,
        ep_name="THE DUMP",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode22 = TVShowEpisodes(
        tv_id=2,
        ep_number=12,
        ep_name="SHAPE SHIFTERS",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode23 = TVShowEpisodes(
        tv_id=2,
        ep_number=13,
        ep_name="FISH NIGHT",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode24 = TVShowEpisodes(
        tv_id=2,
        ep_number=14,
        ep_name="HELPING HAND",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode25 = TVShowEpisodes(
        tv_id=2,
        ep_number=15,
        ep_name="ALTERNATE HISTORIES",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode26 = TVShowEpisodes(
        tv_id=2,
        ep_number=16,
        ep_name="LUCKY 13",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode27 = TVShowEpisodes(
        tv_id=2,
        ep_number=17,
        ep_name="BLINDSPOT",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode28 = TVShowEpisodes(
        tv_id=2,
        ep_number=18,
        ep_name="ZIMA BLUE",
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
        tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
    tv_episode1 = TVShowEpisodes(
        tv_id=
        ep_number=
        ep_name=
        ep_description=
        ep_duration=
        ep_poster=
    )
