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
        ep_description="Awakening after traveling light years off course, a ship's crew struggles to discover just how far they've come.",
        ep_duration="17m",
        ep_poster="https://occ-0-2794-448.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABQPwILqyIGBhsZSIvrl2q4iS4U_KGyqLJNy8Fg74nNHCph7UFZkQikSvW5-qDxEqk-f4RrhS7nYUzLYoAe2x6ftv7RXmcv7lxy2ojYnPQ6POCOtTAxZQg9IE.jpg"
    )
    tv_episode13 = TVShowEpisodes(
        tv_id=2,
        ep_number=3,
        ep_name="ICE AGE",
        ep_description="A young couple moves into an apartment and finds a lost civilization inside their antique freezer.",
        ep_duration="11m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABU_j2W8MOx3EvUkdM-5ULyUI9xSgbfnHXsn_IJ9B5uAS7LbBZEgkLcN45AjXLwTKbbyUodd-35Jz4_crZuY0YojcmUve0RzkreZSS11XnnlSwHlibHYG9e5E.jpg"
    )
    tv_episode14 = TVShowEpisodes(
        tv_id=2,
        ep_number=4,
        ep_name="SONNIE'S EDGE",
        ep_description="In the underground world of 'Beastie' fights, Sonnie is unbeatable -- as long as she keeps her edge.",
        ep_duration="17m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABbNLkwiIKzD0FQQ3v3_NPWrGSzQMAim5mpQhoE2fxNVim2WuXkcG_HdWMou05U2fuG_ev-pxUAVn_qATYKGSw6iWHT6zEqNx56mDogFeMAlK5mZ_vEANVSkQ.jpg"
    )
    tv_episode15 = TVShowEpisodes(
        tv_id=2,
        ep_number=5,
        ep_name="WHEN THE YOGURT TOOK OVER",
        ep_description="After scientists accidentally breed super-intelligent yogurt, it soon hungers for world domination.",
        ep_duration="6m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABcKK6Pl63HRtYaehxY6MAYjFNlg56I8F7uDiWNOP_jqorRlYwlXXGHv1UoVjL_JpEcHAMwUAMGDVZxAQy3-x28s25VIABt9gCfm4iJ2JTo0bvz6Xiprl2l4e.jpg"
    )
    tv_episode16 = TVShowEpisodes(
        tv_id=2,
        ep_number=6,
        ep_name="THE SECRET WAR",
        ep_description="Elite units of the Red Army fight an unholy evil deep in the ancient forests of Siberia.",
        ep_duration="16m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABV0CBLwsmipM5AmAgMQmwsh41TzbKKW6Hq8F-RkoRqMUENXMdZIXmUWmzeXW_NtXmQwXiJAx8fcwWD_hTSiU-rnYCA2ItSjnr-d5icPP0uUHMel7d97YB-Zs.jpg"
    )
    tv_episode17 = TVShowEpisodes(
        tv_id=2,
        ep_number=7,
        ep_name="SUCKER OF SOULS",
        ep_description="Unleashed by an archaeological dig, a bloodthirsty demon battles a team of mercenaries armed with... cats?",
        ep_duration="13m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABem2SKcPOLXka8cBGDH_OTPi_Ivag8DMz7q3u4gcIN8d-wcf7YZSJZfNIWddObdmePrffoFjjnZR4DUIT9np_1jYfiQOXdC6oLRQdutBPA2mdjhe2zFi3zlC.jpg"
    )
    tv_episode18 = TVShowEpisodes(
        tv_id=2,
        ep_number=8,
        ep_name="THE WITNESS",
        ep_description="After seeing a brutal murder, a woman flees from the killer through the streets of a surreal city.",
        ep_duration="12m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABc6OJeTHtempiYQqEOlicrHYgexwbCwMrNDgoOayuK69jixXq_QlvE4_5xfG2VfpJJgK8mZZ8G6cDMCQbP5SeNamb0a79M6TvPnIsZA1fI3NBttfdGGh_REj.jpg"
    )
    tv_episode19 = TVShowEpisodes(
        tv_id=2,
        ep_number=9,
        ep_name="SUITS",
        ep_description="A community of farmers use their homemade mechs to defend their families from an alien invasion.",
        ep_duration="17m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABUhvOYUCzlm2B6OIOpgh8ZGy6fWJQcRpoBd0xq5oEg2_zs5BN_VY3irg-OBAfu57W5TPFEl7Gz2305aHP-f7Yr-9rNonx2Xgsn4KlBYtbs20M9qOK9GzADTM.jpg"
    )
    tv_episode20 = TVShowEpisodes(
        tv_id=2,
        ep_number=10,
        ep_name="GOOD HUNTING",
        ep_description="The son of a spirit hunter forges a bond with a shape-shifting huli jing.",
        ep_duration="17m",
        ep_poster="https://occ-0-2794-448.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABXUqo2ngtxXaK61Qxbot3QM7ewOfuRR3h5hcXCvQNngqh98cXgYf6Xu7BxIYv2P7r_yOnLC1xyoKTIxsIRTdHm1MI1m7QtuKwksVqXx9-HJnxfcjE9bh0uwW.jpg"
    )
    tv_episode21 = TVShowEpisodes(
        tv_id=2,
        ep_number=11,
        ep_name="THE DUMP",
        ep_description="Ugly Dave calls the garbage dump home, and he's not about to let some city slicker take it away from him.",
        ep_duration="11m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABa5rdvuwZpnlwbqWCkPFhl1rzrlkQCHOEQpFJkLGKol6T7Cq7FXiUk2sblzsVbK92pZ-CstMu9cas0jBt37L7Yv6w9DR5G6xMxxvC7ufvm_6fVayQ_7F84W5.jpg"
    )
    tv_episode22 = TVShowEpisodes(
        tv_id=2,
        ep_number=12,
        ep_name="SHAPE SHIFTERS",
        ep_description="Deep in Afghanistan, two Marines with supernatural powers face a threat from one of their own kind.",
        ep_duration="16m",
        ep_poster="https://www.whats-on-netflix.com/wp-content/uploads/2019/03/Shape-Shifters-Love-Death-and-Robots-Ending-Explained.jpg"
    )
    tv_episode23 = TVShowEpisodes(
        tv_id=2,
        ep_number=13,
        ep_name="FISH NIGHT",
        ep_description="After their car breaks down in the desert, two salesmen take a dreamlike voyage to the dawn of time.",
        ep_duration="10m",
        ep_poster="https://www.whats-on-netflix.com/wp-content/uploads/2019/03/Fish-Night-Love-Death-and-Robots-Ending-Explained.jpg"
    )
    tv_episode24 = TVShowEpisodes(
        tv_id=2,
        ep_number=14,
        ep_name="HELPING HAND",
        ep_description="Stranded in orbit, an astronaut must choose between life and limb before her oxygen runs out.",
        ep_duration="10m",
        ep_poster="https://static.wikia.nocookie.net/lovedeathrobots/images/d/d6/Helping_Hand.jpg"
    )
    tv_episode25 = TVShowEpisodes(
        tv_id=2,
        ep_number=15,
        ep_name="ALTERNATE HISTORIES",
        ep_description="Want to see Hitler die in a variety of comically fantastic ways? Now you can. Welcome to Multiversity!",
        ep_duration="8m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABYXCENgzzHVNNAtX9DOiMc9Q9v1rtQWILXKUQp_Lcz6Qk_l2S_-zHwyL77vcjVTxwwxwdj0bISPlEs4BwwLjlePmYJn6sMtYsw8FICX3Mva5Pfxkas6KVChu.jpg"
    )
    tv_episode26 = TVShowEpisodes(
        tv_id=2,
        ep_number=16,
        ep_name="LUCKY 13",
        ep_description="After the drop-ship Lucky 13 lost two crews, no pilot would fly her... but rookies don't get a choice.",
        ep_duration="15m",
        ep_poster="https://occ-0-2794-448.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABa4gLmFCd-TWnLmoy88jxzy70X0w2JJB-TdVpT0x9dUxL-rTPm1ePb1w6-1AYssDtW37Hpz4DeOmP0phiVzC0528BCeRWwZmxMRYygOAvl-2Abgc-oaw3SHa.jpg"
    )
    tv_episode27 = TVShowEpisodes(
        tv_id=2,
        ep_number=17,
        ep_name="BLINDSPOT",
        ep_description="A gang of cyborg thieves stage a high-speed heist of a heavily armored convoy.",
        ep_duration="9m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABYa1FZWn8THj_ir0c4YzLbkSbkauQQFWzb2BolQGCpNzr9FRflYq1CQbt7qdkqoxDBRHhwq4mFO8OTuFkAE2VaUgnruwikAohzHXBQkQJVOv7UtlubX9CKZT.jpg"
    )
    tv_episode28 = TVShowEpisodes(
        tv_id=2,
        ep_number=18,
        ep_name="ZIMA BLUE",
        ep_description="The renowned artist Zima recounts his mysterious past and rise to fame before unveiling his final work.",
        ep_duration="10m",
        ep_poster="https://occ-0-1380-778.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABeLEOOT8iZazEgIAsU0XzWE5qfUM0-hpS5dENxX4xWr1gJ5yMEEPcUlVhD1QMZa1Hf5SHclFjuIj1_webFchG2DAi5vbHGN2VUA0nWGbms753vqROyKTn4T5.jpg"
    )
    ##Sex Education
    tv_episode29 = TVShowEpisodes(
        tv_id=3,
        ep_number=1,
        ep_name="Episode 1",
        ep_description="Despite the ministrations of sex therapist mom Jean and encouragement from pal Eric, Otis worries that he can't get it on. He's not the only one.",
        ep_duration="52m",
        ep_poster="https://occ-0-3647-987.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABb97iEQt3Z2trkOr4UukvzmsG1BxtgJZW3rOKjLmpgpr1faFn7CkcVxOAu4AFuaW-5PE-d0137mJxllqqcHAydkoNDvoZSKWb4si9N9TXatn17SZCqQ_gZLq.jpg"
    )
    tv_episode30 = TVShowEpisodes(
        tv_id=3,
        ep_number=2,
        ep_name="Episode 2",
        ep_description="Egged on by Maeve -- and finding that dispensing sex tips is tougher than he thought -- Otis tries offering free advice at a classmate's house party.",
        ep_duration="50m",
        ep_poster="https://www.comingsoon.net/wp-content/uploads/sites/3/2019/01/sex-education-s1e2-1.jpg"
    )
    tv_episode31 = TVShowEpisodes(
        tv_id=3,
        ep_number=3,
        ep_name="Episode 3",
        ep_description="Otis' clinic achieves liftoff, as does his attraction to Maeve, who unexpectedly asks him for help. Eric swings off on his own and fields a come-on.",
        ep_duration="50m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BMTQwZjZhYzYtODExNi00ZTc1LTljNTUtMzQ5NGFjM2NjNDc0XkEyXkFqcGdeQXVyNjYyNDMwOQ@@._V1_.jpg"
    )
    tv_episode32 = TVShowEpisodes(
        tv_id=3,
        ep_number=4,
        ep_name="Episode 4",
        ep_description="Eric realizes Otis has fallen for Maeve. But the young sex therapist finds himself torn when hot guy Jackson seeks help with his secret crush.",
        ep_duration="47m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BYTZjMWJiYzMtY2IyNi00OGQzLWI2MzYtZGY1OTQxYTliNGZlXkEyXkFqcGdeQXVyNjYyNDMwOQ@@._V1_.jpg"
    )
    tv_episode33 = TVShowEpisodes(
        tv_id=3,
        ep_number=5,
        ep_name="Episode 5",
        ep_description="An explicit pic puts a mean girl on the spot. Maeve wants to track down the shaming culprit, forcing Otis to make a tough choice on an important day.",
        ep_duration="47m",
        ep_poster="https://static.wikia.nocookie.net/sex-education-netflix/images/d/d6/Episode_5.jpg"
    )
    tv_episode34 = TVShowEpisodes(
        tv_id=3,
        ep_number=6,
        ep_name="Episode 6",
        ep_description="Eric's trauma isolates him, and Maeve's essay wins a prize. Otis tries to hook up with Lily, but his deep-seated issues get in the way.",
        ep_duration="49m",
        ep_poster="https://static.wikia.nocookie.net/sex-education-netflix/images/e/e7/Episode_6.jpg"
    )
    tv_episode35 = TVShowEpisodes(
        tv_id=3,
        ep_number=7,
        ep_name="Episode 7",
        ep_description="The big dance brings out the best, and the drama, in Moordale's student body. Otis finds a date, Maeve gets her dress, and Eric returns with style.",
        ep_duration="51m",
        ep_poster="https://static.wikia.nocookie.net/sex-education-netflix/images/0/0f/Episode_7.jpg"
    )
    tv_episode36 = TVShowEpisodes(
        tv_id=3,
        ep_number=8,
        ep_name="Episode 8",
        ep_description="Otis feels violated by Jean's new book, and Maeve takes the fall for her brother. Eric serves detention with an old foe, while Lily's body betrays her.",
        ep_duration="53m",
        ep_poster="https://static.wikia.nocookie.net/sex-education-netflix/images/5/5a/Episode_8.jpg"
    )
    ##Haunting of Hill House
    tv_episode37 = TVShowEpisodes(
        tv_id=4,
        ep_number=1,
        ep_name="Steven Seed a Ghost",
        ep_description="While investigating a ghost story for his latest novel, a skeptical Steven receives a call from his sister that triggers a chain of fateful events.",
        ep_duration="60m",
        ep_poster="https://occ-0-993-784.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABTwhr1FZCYAQGa1NN8EFbj8JMgxMbZzBVGPDLqqieJrVPEMylyc-xlABYQqxKtGa4UI6jpIkMk9o3MmUExfUjy_d9z2d6gF_0yXm70o2QYLx4z5FC1gUc-Ux.jpg"
    )
    tv_episode38 = TVShowEpisodes(
        tv_id=4,
        ep_number=2,
        ep_name="Open Casket",
        ep_description="A devastating family tragedy stirs memories of traumatic losses, reminding Shirley of her first brush with death -- and awakening long-dormant fears.",
        ep_duration="51m",
        ep_poster="https://occ-0-993-784.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABa0ZG3Qa0dJ4J12d5Od5mn4Mo2y2qiEdNlLqeyZhxYIZaIuL4-HchhaAxIGKAZWaeR61J5IpurZYInq0etlDVl7OHZkJ0TWHqkVFaicgpWwXXZ3BUrNcm1g3.jpg"
    )
    tv_episode39 = TVShowEpisodes(
        tv_id=4,
        ep_number=3,
        ep_name="Touch",
        ep_description="Keenly perceptive Theo sees shades of herself in a troubled young patient, a girl who's haunted by the menacing grin of 'Mr. Smiley.'",
        ep_duration="53m",
        ep_poster="https://www.thesun.co.uk/wp-content/uploads/2018/09/vlcsnap-2018-09-20-09h57m04s221.png"
    )
    tv_episode40 = TVShowEpisodes(
        tv_id=4,
        ep_number=4,
        ep_name="The Twin Thing",
        ep_description="Still wrestling with addiction -- and an unshakable fright -- a frantic Luke tries to save a friend while sensing his twin sister is in danger.",
        ep_duration="53m",
        ep_poster="https://occ-0-993-784.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABfIn1m9bfkN-hDhR48Hkr4G9piDBhbdDbYYTsUYKuQyLpmwcwKDjs4PUmjPv4QFbSgfOTjFRcQufFgHr9E5yjSU4nLVOrTfR_SdQE0M40XRv8IXeuV73QJ7X.jpg"
    )
    tv_episode41 = TVShowEpisodes(
        tv_id=4,
        ep_number=5,
        ep_name="The Bent-Neck Lady",
        ep_description="A dark specter with an unsettling silhouette has haunted Nell since she was a girl. Now 'the Bent-Neck Lady' is back -- and she's calling Nell home.",
        ep_duration="70m",
        ep_poster="https://occ-0-993-784.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABc5kAClaYiMLJvE9WJvmtHyTxQIXZ3JcIXRr7zNOu7BTCic0OcMw4cR047itcFxQDi_JV3gPSXs0MZqhqoA9R74ZhrHHLLuUwXLkQLjn3lqROZcwvjWrU2mO.jpg"
    )
    tv_episode42 = TVShowEpisodes(
        tv_id=4,
        ep_number=6,
        ep_name="Two Storms",
        ep_description="It's a reunion for all the wrong reasons when Hugh flies in for the funeral, coming face to face with his estranged children on a dark, stormy night.",
        ep_duration="57m",
        ep_poster="https://www.indiewire.com/wp-content/uploads/2018/10/Haunting-of-Hill-House-Long-Take.jpg"
    )
    tv_episode43 = TVShowEpisodes(
        tv_id=4,
        ep_number=7,
        ep_name="Eulogy",
        ep_description="As the Crains gather to say their final goodbyes, a flashback reveals Mr. Dudley's connection to the house -- and exposes a secret in the walls.",
        ep_duration="60",
        ep_poster="https://occ-0-993-784.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABfrm8DZDqWRZoTEUTBCxqwcuXIf_4EMpKzAyosaMyzr0MAuCiCfOGui3NzS5QnsB0LhCjIweTCcFBSxwTDe1ghl7-x83GBFSzAMEBifEz-kw1Bl8oU_7kbPf.jpg"
    )
    tv_episode44 = TVShowEpisodes(
        tv_id=4,
        ep_number=8,
        ep_name="Witness Marks",
        ep_description="A familiar terror revisits Shirley and Theo on Halloween night as Hugh and Steve go looking for Luke, who disappeared on a deadly errand.",
        ep_duration="43",
        ep_poster="https://static.wikia.nocookie.net/the-haunting-of-hill-house3356/images/3/3e/S1E8.jpg"
    )
    tv_episode45 = TVShowEpisodes(
        tv_id=4,
        ep_number=9,
        ep_name="Screaming Meemies",
        ep_description="While struggling to discern dreams from reality, Olivia fears for her children's safety, a motherly instinct Mrs. Dudley urges her to embrace.",
        ep_duration="57",
        ep_poster="https://m.media-amazon.com/images/M/MV5BZTI4YzE1NDctOGM0YS00YTMzLThmNDMtMzdmMWRlNzU3NDA1XkEyXkFqcGdeQXVyODExNTExMTM@._V1_.jpg"
    )
    tv_episode46 = TVShowEpisodes(
        tv_id=4,
        ep_number=10,
        ep_name="Silence Lay Steadily",
        ep_description="The Red Room's contents are finally revealed as the Crains return to the house to confront old ghosts, unspeakable secrets and an insatiable evil.",
        ep_duration="71",
        ep_poster="https://static.wikia.nocookie.net/the-haunting-of-hill-house3356/images/5/56/B.jpg"
    )
    ##Hannibal
    tv_episode47 = TVShowEpisodes(
        tv_id=5,
        ep_number=1,
        ep_name="Apéritif",
        ep_description="The head of the FBI Behavioral Science unit, Jack Crawford, calls on profiler Will Graham to assist them catch a serial killer. The killer has now kidnapped eight women, all similar in appearance and always on a Friday.",
        ep_duration="42",
        ep_poster="https://m.media-amazon.com/images/M/MV5BMjM0ODAxMDc0MF5BMl5BanBnXkFtZTcwNzQxOTMzOQ@@._V1_.jpg"
    )
    tv_episode48 = TVShowEpisodes(
        tv_id=5,
        ep_number=2,
        ep_name="Amuse-Bouche",
        ep_description="Will and Jack hunt a killer who is burying his victims alive, so they will become fertilizer for his garden of fungus. While the tabloid journalist Freddie sets targets in on Will.",
        ep_duration="42",
        ep_poster="https://m.media-amazon.com/images/M/MV5BOTk4NTc5Njg2OF5BMl5BanBnXkFtZTcwNjUxOTMzOQ@@._V1_.jpg"
    )
    tv_episode49 = TVShowEpisodes(
        tv_id=5,
        ep_number=3,
        ep_name="Potage",
        ep_description="Determined to give Abigail closure, Will and Hannibal take Abigail back to the scene of her father's crimes. But things take a turn for the worse when the copycat killer strikes again.",
        ep_duration="42",
        ep_poster="https://static.wikia.nocookie.net/hannibal/images/8/83/Potage1.png"
    )
    tv_episode50 = TVShowEpisodes(
        tv_id=5,
        ep_number=4,
        ep_name="Oeuf",
        ep_description="A series of family murders takes place, and Will determines they were conducted by each of the families' missing children, who were abducted and brainwashed into killing their old families for their 'new family.'",
        ep_duration="42",
        ep_poster="https://fathersonholygore.files.wordpress.com/2015/08/img_0124.png"
    )
    tv_episode51 = TVShowEpisodes(
        tv_id=5,
        ep_number=5,
        ep_name="Coquilles",
        ep_description="A murdered couple is found in a motel room, posed in praying positions with the flesh of their backs opened and strung to the ceiling to give them the appearance of wings.",
        ep_duration="42",
        ep_poster="https://static1.srcdn.com/wordpress/wp-content/uploads/2020/02/hannibal-season-1-episode-5-coquilles.jpg"
    )
    tv_episode52 = TVShowEpisodes(
        tv_id=5,
        ep_number=6,
        ep_name="Entrée",
        ep_description="A nurse at the Baltimore State Hospital for the Criminally Insane is brutally murdered by a patient, Dr. Abel Gideon, in a manner reminiscent of the 'Chesapeake Ripper', who hasn't committed a murder in two years, as long as Gideon has been incarcerated.",
        ep_duration="42",
        ep_poster="https://m.media-amazon.com/images/M/MV5BOWM4ODBiZWEtZmY4Mi00NGZjLTk2NjUtM2IyMzM0MGVmODRhXkEyXkFqcGdeQXVyMDgyNjA5MA@@._V1_.jpg"
    )
    tv_episode53 = TVShowEpisodes(
        tv_id=5,
        ep_number=7,
        ep_name="Sorbet",
        ep_description="The BAU is called in when a man is found in a hotel room bathtub with his kidney removed and Graham must determine whether this is the act of an organ harvester or if the Chesapeake Ripper has claimed his first victim in two years.",
        ep_duration="42",
        ep_poster="https://m.media-amazon.com/images/M/MV5BOTM4MTA2ZGQtMzMyMi00NGQ4LWE4NTEtOWVmOTZhOTlmNzQ3XkEyXkFqcGdeQXVyNzQ1NjgzOTA@._V1_.jpg"
    )
    tv_episode54 = TVShowEpisodes(
        tv_id=5,
        ep_number=8,
        ep_name="Fromage",
        ep_description="Lecter's patient Franklin Froideveaux worries that his friend Tobias may be a psychopath, but Franklin's growing obsession with Lecter is what concerns the latter more.",
        ep_duration="42",
        ep_poster="https://fathersonholygore.files.wordpress.com/2015/08/img_0347.png"
    )
    tv_episode55 = TVShowEpisodes(
        tv_id=5,
        ep_number=9,
        ep_name="Trou Normand",
        ep_description="A totem pole of human bodies ranging from freshly killed to decades old are found on a beach and while Graham is investigating the crime scene, he suddenly finds himself in Lecter's office, three and a half hours away, with no memory of how he got there.",
        ep_duration="42",
        ep_poster="https://fathersonholygore.files.wordpress.com/2015/08/img_0360.png"
    )
    tv_episode56 = TVShowEpisodes(
        tv_id=5,
        ep_number=10,
        ep_name="Buffet Froid",
        ep_description="Beth LeBeau is found murdered, having drowned in her own blood as a result of her face being cut into a Glasgow smile. Graham's mental state continues to sharply decline.",
        ep_duration="42",
        ep_poster="https://static1.srcdn.com/wordpress/wp-content/uploads/2020/03/hannibal-season-1-episode-10-face-blindness.jpg"
    )
    tv_episode57 = TVShowEpisodes(
        tv_id=5,
        ep_number=11,
        ep_name="Rôti",
        ep_description="Dr. Abel Gideon escapes from custody and begins targeting the psychiatrists who attempted to treat him, displaying their bodies with a Colombian necktie. Meanwhile, Graham's undiagnosed Encephalitis drives his temperature up, causing hallucinations.",
        ep_duration="42",
        ep_poster="https://collider.com/wp-content/uploads/hannibal-roti-hugh-dancy.jpg"
    )
    tv_episode58 = TVShowEpisodes(
        tv_id=5,
        ep_number=12,
        ep_name="Relevés",
        ep_description="Graham deduces that several recent murders were all the work of a copycat patterning after recent serial murders, and that Georgia was killed because she may have remembered the face of whoever had killed Dr. Sutcliffe.",
        ep_duration="42",
        ep_poster="https://fathersonholygore.files.wordpress.com/2015/08/img_0587.png"
    )
    tv_episode59 = TVShowEpisodes(
        tv_id=5,
        ep_number=13,
        ep_name="Savoureux",
        ep_description="Following his strange trip to Minnesota, Graham is taken into custody by Crawford for the probable murder of Abigail Hobbs. They find her severed ear in his kitchen sink and her blood under his fingernails.",
        ep_duration="42",
        ep_poster="https://www.pogdesign.co.uk/cat/imgs/episodes/Hannibal/Hannibal-S01E13-1d931943bad0d8cd940850b3b918c3d8-full.jpg"
    )
    ##Alice in Borderland
