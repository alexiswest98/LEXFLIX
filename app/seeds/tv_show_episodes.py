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
        ep_duration="60m",
        ep_poster="https://occ-0-993-784.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABfrm8DZDqWRZoTEUTBCxqwcuXIf_4EMpKzAyosaMyzr0MAuCiCfOGui3NzS5QnsB0LhCjIweTCcFBSxwTDe1ghl7-x83GBFSzAMEBifEz-kw1Bl8oU_7kbPf.jpg"
    )
    tv_episode44 = TVShowEpisodes(
        tv_id=4,
        ep_number=8,
        ep_name="Witness Marks",
        ep_description="A familiar terror revisits Shirley and Theo on Halloween night as Hugh and Steve go looking for Luke, who disappeared on a deadly errand.",
        ep_duration="43m",
        ep_poster="https://static.wikia.nocookie.net/the-haunting-of-hill-house3356/images/3/3e/S1E8.jpg"
    )
    tv_episode45 = TVShowEpisodes(
        tv_id=4,
        ep_number=9,
        ep_name="Screaming Meemies",
        ep_description="While struggling to discern dreams from reality, Olivia fears for her children's safety, a motherly instinct Mrs. Dudley urges her to embrace.",
        ep_duration="57m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BZTI4YzE1NDctOGM0YS00YTMzLThmNDMtMzdmMWRlNzU3NDA1XkEyXkFqcGdeQXVyODExNTExMTM@._V1_.jpg"
    )
    tv_episode46 = TVShowEpisodes(
        tv_id=4,
        ep_number=10,
        ep_name="Silence Lay Steadily",
        ep_description="The Red Room's contents are finally revealed as the Crains return to the house to confront old ghosts, unspeakable secrets and an insatiable evil.",
        ep_duration="71m",
        ep_poster="https://static.wikia.nocookie.net/the-haunting-of-hill-house3356/images/5/56/B.jpg"
    )
    ##Hannibal
    tv_episode47 = TVShowEpisodes(
        tv_id=5,
        ep_number=1,
        ep_name="Apéritif",
        ep_description="The head of the FBI Behavioral Science unit, Jack Crawford, calls on profiler Will Graham to assist them catch a serial killer. The killer has now kidnapped eight women, all similar in appearance and always on a Friday.",
        ep_duration="42m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BMjM0ODAxMDc0MF5BMl5BanBnXkFtZTcwNzQxOTMzOQ@@._V1_.jpg"
    )
    tv_episode48 = TVShowEpisodes(
        tv_id=5,
        ep_number=2,
        ep_name="Amuse-Bouche",
        ep_description="Will and Jack hunt a killer who is burying his victims alive, so they will become fertilizer for his garden of fungus. While the tabloid journalist Freddie sets targets in on Will.",
        ep_duration="42m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BOTk4NTc5Njg2OF5BMl5BanBnXkFtZTcwNjUxOTMzOQ@@._V1_.jpg"
    )
    tv_episode49 = TVShowEpisodes(
        tv_id=5,
        ep_number=3,
        ep_name="Potage",
        ep_description="Determined to give Abigail closure, Will and Hannibal take Abigail back to the scene of her father's crimes. But things take a turn for the worse when the copycat killer strikes again.",
        ep_duration="42m",
        ep_poster="https://static.wikia.nocookie.net/hannibal/images/8/83/Potage1.png"
    )
    tv_episode50 = TVShowEpisodes(
        tv_id=5,
        ep_number=4,
        ep_name="Oeuf",
        ep_description="A series of family murders takes place, and Will determines they were conducted by each of the families' missing children, who were abducted and brainwashed into killing their old families for their 'new family.'",
        ep_duration="42m",
        ep_poster="https://fathersonholygore.files.wordpress.com/2015/08/img_0124.png"
    )
    tv_episode51 = TVShowEpisodes(
        tv_id=5,
        ep_number=5,
        ep_name="Coquilles",
        ep_description="A murdered couple is found in a motel room, posed in praying positions with the flesh of their backs opened and strung to the ceiling to give them the appearance of wings.",
        ep_duration="42m",
        ep_poster="https://static1.srcdn.com/wordpress/wp-content/uploads/2020/02/hannibal-season-1-episode-5-coquilles.jpg"
    )
    tv_episode52 = TVShowEpisodes(
        tv_id=5,
        ep_number=6,
        ep_name="Entrée",
        ep_description="A nurse at the Baltimore State Hospital for the Criminally Insane is brutally murdered by a patient, Dr. Abel Gideon, in a manner reminiscent of the 'Chesapeake Ripper', who hasn't committed a murder in two years, as long as Gideon has been incarcerated.",
        ep_duration="42m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BOWM4ODBiZWEtZmY4Mi00NGZjLTk2NjUtM2IyMzM0MGVmODRhXkEyXkFqcGdeQXVyMDgyNjA5MA@@._V1_.jpg"
    )
    tv_episode53 = TVShowEpisodes(
        tv_id=5,
        ep_number=7,
        ep_name="Sorbet",
        ep_description="The BAU is called in when a man is found in a hotel room bathtub with his kidney removed and Graham must determine whether this is the act of an organ harvester or if the Chesapeake Ripper has claimed his first victim in two years.",
        ep_duration="42m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BOTM4MTA2ZGQtMzMyMi00NGQ4LWE4NTEtOWVmOTZhOTlmNzQ3XkEyXkFqcGdeQXVyNzQ1NjgzOTA@._V1_.jpg"
    )
    tv_episode54 = TVShowEpisodes(
        tv_id=5,
        ep_number=8,
        ep_name="Fromage",
        ep_description="Lecter's patient Franklin Froideveaux worries that his friend Tobias may be a psychopath, but Franklin's growing obsession with Lecter is what concerns the latter more.",
        ep_duration="42m",
        ep_poster="https://fathersonholygore.files.wordpress.com/2015/08/img_0347.png"
    )
    tv_episode55 = TVShowEpisodes(
        tv_id=5,
        ep_number=9,
        ep_name="Trou Normand",
        ep_description="A totem pole of human bodies ranging from freshly killed to decades old are found on a beach and while Graham is investigating the crime scene, he suddenly finds himself in Lecter's office, three and a half hours away, with no memory of how he got there.",
        ep_duration="42m",
        ep_poster="https://fathersonholygore.files.wordpress.com/2015/08/img_0360.png"
    )
    tv_episode56 = TVShowEpisodes(
        tv_id=5,
        ep_number=10,
        ep_name="Buffet Froid",
        ep_description="Beth LeBeau is found murdered, having drowned in her own blood as a result of her face being cut into a Glasgow smile. Graham's mental state continues to sharply decline.",
        ep_duration="42m",
        ep_poster="https://static1.srcdn.com/wordpress/wp-content/uploads/2020/03/hannibal-season-1-episode-10-face-blindness.jpg"
    )
    tv_episode57 = TVShowEpisodes(
        tv_id=5,
        ep_number=11,
        ep_name="Rôti",
        ep_description="Dr. Abel Gideon escapes from custody and begins targeting the psychiatrists who attempted to treat him, displaying their bodies with a Colombian necktie. Meanwhile, Graham's undiagnosed Encephalitis drives his temperature up, causing hallucinations.",
        ep_duration="42m",
        ep_poster="https://collider.com/wp-content/uploads/hannibal-roti-hugh-dancy.jpg"
    )
    tv_episode58 = TVShowEpisodes(
        tv_id=5,
        ep_number=12,
        ep_name="Relevés",
        ep_description="Graham deduces that several recent murders were all the work of a copycat patterning after recent serial murders, and that Georgia was killed because she may have remembered the face of whoever had killed Dr. Sutcliffe.",
        ep_duration="42m",
        ep_poster="https://fathersonholygore.files.wordpress.com/2015/08/img_0587.png"
    )
    tv_episode59 = TVShowEpisodes(
        tv_id=5,
        ep_number=13,
        ep_name="Savoureux",
        ep_description="Following his strange trip to Minnesota, Graham is taken into custody by Crawford for the probable murder of Abigail Hobbs. They find her severed ear in his kitchen sink and her blood under his fingernails.",
        ep_duration="42m",
        ep_poster="https://www.pogdesign.co.uk/cat/imgs/episodes/Hannibal/Hannibal-S01E13-1d931943bad0d8cd940850b3b918c3d8-full.jpg"
    )
    ##Alice in Borderland
    tv_episode60 = TVShowEpisodes(
        tv_id=6,
        ep_number=1,
        ep_name="Episode 1",
        ep_description="Arisu and his friends run into a public bathroom to hide from the police, but when they reemerge, the streets of Tokyo are suddenly completely empty.",
        ep_duration="49m",
        ep_poster="https://occ-0-360-3647.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABVtm-VioPBSfed8WpPC6k5nfQ_ntr0Ac6TiAfeLYRs9s2ow2gbhA3diK2SfRSdKfKt-V1I0H41ap8JLj2hpJpBS4lUY_Wa7ZNMaDAbP99dmjsr4ky-C3URcs.jpg"
    )
    tv_episode61 = TVShowEpisodes(
        tv_id=6,
        ep_number=2,
        ep_name="Episode 2",
        ep_description="Leaving an injured Chota, Arisu and Karube head out to gain more experience. They come to a sprawling apartment, where a deadly game of tag awaits.",
        ep_duration="51m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BMjljODRmN2YtYmQ1Zi00OTE4LWFkYWEtOTc0ODY4MzgzNzRiXkEyXkFqcGdeQXVyODczNDI0MTE@._V1_FMjpg_UX1000_.jpg"
    )
    tv_episode62 = TVShowEpisodes(
        tv_id=6,
        ep_number=3,
        ep_name="Episode 3",
        ep_description="With Chota and Shibuki's visas fast expiring, the four enter a vast botanical garden in Shinjuku, where they take part in a cruel game of betrayal.",
        ep_duration="43m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BMDg5ZGI3Y2YtYzNmZi00MjI4LThhMmQtNTMyYjhhZWQ2NWQ4XkEyXkFqcGdeQXVyMTIyMzk3NDU1._V1_.jpg"
    )
    tv_episode63 = TVShowEpisodes(
        tv_id=6,
        ep_number=4,
        ep_name="Episode 4",
        ep_description="Arisu is overwhelmed with guilt and ready to give up, but Usagi urges him to keep going. Next up is a game of endurance in an underground highway.",
        ep_duration="47m",
        ep_poster="https://occ-0-360-3647.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABdSmxq-UqbXz6AgtN22Vm8xb42z331Uq6Yr0fy1qnGUKgY_X-h_JCZPSOG3mrpa6ZR0-zfgouFdNbq37UZFFMWRTi1F-WSksfmpkb7DZVRleB9rnxvcCoo3N.jpg"
    )
    tv_episode64 = TVShowEpisodes(
        tv_id=6,
        ep_number=5,
        ep_name="Episode 5",
        ep_description="After Arisu and Usagi find their way to the Beach, the king of the so-called utopian haven forces them to help gather the remaining playing cards.",
        ep_duration="52m",
        ep_poster="https://m.media-amazon.com/images/M/MV5BNjY3ZDJlMWQtOTFjNC00YzUxLWFiYzgtOTY2N2Y3ZGJiZjljXkEyXkFqcGdeQXVyMTIyMzk3NDU1._V1_.jpg"
    )
    tv_episode65 = TVShowEpisodes(
        tv_id=6,
        ep_number=6,
        ep_name="Episode 6",
        ep_description="Chishiya recruits Arisu and Usagi to help him change the status quo. An unforeseen event rocks the fragile power dynamics of the Beach.",
        ep_duration="42m",
        ep_poster="https://occ-0-360-3647.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABe0SGBbVRHHdZjnfyF6G-x7yzPN0tIrXRhTkEjpSEYZggFa4PngIPy-Zbb228NWyOgkUUJ3Gq2VTG-Nr_9Dt1soSDvHUqM5EC7-_PvtkfV03JaIDVWfddCfH.jpg"
    )
    tv_episode66 = TVShowEpisodes(
        tv_id=6,
        ep_number=7,
        ep_name="Episode 7",
        ep_description="Once a safe haven, the Beach becomes the arena for the next stage, where an epic witch hunt turns everyone against each other in a hostile showdown.",
        ep_duration="49m",
        ep_poster="https://occ-0-360-3647.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABbVu2V8s7dTPZzQ5kbj3EicXBQKz00egzqKjL--H4rnfxB0EaV-4KIBfHamPW7jwHBLKoJtCymhszqM3h2AsfJsH_LnBQ8TEnpr5nyZnjCuGVOeP_M_kqyzx.jpg"
    )
    tv_episode67 = TVShowEpisodes(
        tv_id=6,
        ep_number=8,
        ep_name="Episode 8",
        ep_description="Tensions inside the resort reach a boiling point. As the game clock nears zero, those who've survived the onslaught now face an uncertain future.",
        ep_duration="53m",
        ep_poster="https://occ-0-360-3647.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABY9QKBGX3rY_z42SuJwMoYgxUhjxiCVVsq7qKxwDc-CByz8MLfPEwnUw53soElvG57JOIVmWkVPgUVHFdg7qwDDsRxVz-JUBtmjL_cJTNFBJx8-cD2tt2yVt.jpg"
    )
    ##Stranger Things
    tv_episode68 = TVShowEpisodes(
        tv_id=7,
        ep_number=1,
        ep_name="Chapter One: The Vanishing of Will Byers",
        ep_description="On his way home from a friend's house, young Will sees something terrifying. Nearby, a sinister secret lurks in the depths of a government lab.",
        ep_duration="49m",
        ep_poster="https://occ.a.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABYtfkVLxw6lawtNwtIyOhLDnTEXi2AvuyqYG3i-jZ3Y1mrRsZCJAt8mcAxiZqZHQvCS2pl4StiieJUrohIS70br7yzenTsQqVgsVKq3C5A8vuoL_GstEWeB7.jpg"
    )
    tv_episode69 = TVShowEpisodes(
        tv_id=7,
        ep_number=2,
        ep_name="Chapter Two: The Weirdo on Maple Street",
        ep_description="Lucas, Mike and Dustin try to talk to the girl they found in the woods. Hopper questions an anxious Joyce about an unsettling phone call.",
        ep_duration="56m",
        ep_poster="https://occ.a.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABQtwsxsHgdgWIND4fSpPITza0IkQHiqZDXdeVicRWtG9JhFAws01znsKfW8XeqW_2WWBmJpqpnmdN9b7uOy3ePJ2P0Rb30PJsTNGWkXTV0aFZDawHX8kIN3Z.jpg"
    )
    tv_episode70 = TVShowEpisodes(
        tv_id=7,
        ep_number=3,
        ep_name="Chapter Three: Holly, Jolly",
        ep_description="An increasingly concerned Nancy looks for Barb and finds out what Jonathan's been up to. Joyce is convinced Will is trying to talk to her.",
        ep_duration="52m",
        ep_poster="https://occ.a.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABfvDB1xGZuh-SkB7WccIvvvpGTvyOaoYqtePmpAV3pfCbB01RJbg2srq_yIL9UXu-tvyPH9oHIPbiXRfUsL8P7d7LLHxwZeSGpen3Bwyw7gCzFO0XYaBPOku.jpg"
    )
    tv_episode71 = TVShowEpisodes(
        tv_id=7,
        ep_number=4,
        ep_name="Chapter Four: The Body",
        ep_description="Refusing to believe Will is dead, Joyce tries to connect with her son. The boys give Eleven a makeover. Nancy and Jonathan form an unlikely alliance.",
        ep_duration="51m",
        ep_poster="https://pyxis.nymag.com/v1/imgs/abb/25b/9ef00d096fcf6a3606e9be30489b88f425-12-stanger-things-7.2x.rsocial.w600.jpg"
    )
    tv_episode72 = TVShowEpisodes(
        tv_id=7,
        ep_number=5,
        ep_name="Chapter Five: The Flea and the Acrobat",
        ep_description="Hopper breaks into the lab while Nancy and Jonathan confront the force that took Will. The boys ask Mr. Clarke how to travel to another dimension.",
        ep_duration="53m",
        ep_poster="https://occ.a.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABQ4GYyP7zd6_FkLaO3FRYw0Zxvi71gu1R3Jg7HNIpg9uUYIvL_UxeUKWTWJPqYjdsd5RL_fmg_tJKKs6rlzsyalFS7XlIcaHm8rskzSkWaQZDCbjWhAg92TP.jpg"
    )
    tv_episode73 = TVShowEpisodes(
        tv_id=7,
        ep_number=6,
        ep_name="Chapter Six: The Monster",
        ep_description="A frantic Jonathan looks for Nancy in the darkness, but Steve's looking for her, too. Hopper and Joyce uncover the truth about the lab's experiments.",
        ep_duration="47m",
        ep_poster="https://static.wikia.nocookie.net/strangerthings8338/images/3/39/The_Monster_-_Nancy_hides.png"
    )
    tv_episode74 = TVShowEpisodes(
        tv_id=7,
        ep_number=7,
        ep_name="Chapter Seven: The Bathtub",
        ep_description="Eleven struggles to reach Will, while Lucas warns that 'the bad men are coming.' Nancy and Jonathan show the police what Jonathan caught on camera.",
        ep_duration="42m",
        ep_poster="https://static.wikia.nocookie.net/strangerthings8338/images/a/a4/The_Bathtub_Official_Image.jpg"
    )
    tv_episode75 = TVShowEpisodes(
        tv_id=7,
        ep_number=8,
        ep_name="Chapter Eight: The Upside Down",
        ep_description="Dr. Brenner holds Hopper and Joyce for questioning while the boys wait with Eleven in the gym. Back at Will's, Nancy and Jonathan prepare for battle.",
        ep_duration="55m",
        ep_poster="https://static.wikia.nocookie.net/strangerthings8338/images/b/b6/The_Upside_Down_S01-E08_SS_001.png"
    )
    ##squid game
    tv_episode76 = TVShowEpisodes(
        tv_id=8,
        ep_number=1,
        ep_name="Red Light, Green Light",
        ep_description="Hoping to win easy money, a broke and desperate Gi-hun agrees to take part in an enigmatic game. Not long into the first round, unforeseen horrors unfold.",
        ep_duration="60m",
        ep_poster="https://occ-0-300-325.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABcgVURx2aVqBO-ahF6pNsqh6XLdN2zWXsjt7bPe0ndT4lLfoTynn8eOSHT4o5ERPRNaTuI9sEhEmjlkmS_enUWuYT54etS_Z2c9axK2q_rwm5ubHY9x5TwTG.jpg"
    )
    tv_episode77 = TVShowEpisodes(
        tv_id=8,
        ep_number=2,
        ep_name="Hell",
        ep_description="Split on whether to continue or quit, the group holds a vote. But their realities in the outside world may prove to be just as unforgiving as the game.",
        ep_duration="63m",
        ep_poster="https://occ-0-300-325.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABdkTxh49-uTZ6CQMb5ly-nTgu3d9vk9Ij9q2xjseCAjgo1d4SKUWwVXZD_RB9UH2ltggxNm0YylvOCjXNtSSorfBp9KJaTuz-a-cLkg6WWc93obVJzN33G9b.jpg"
    )
    tv_episode78 = TVShowEpisodes(
        tv_id=8,
        ep_number=3,
        ep_name="The Man with the Umbrella",
        ep_description="A few players enter the next round — which promises equal doses of sweet and deadly — with hidden advantages. Meanwhile, Jun-ho sneaks his way inside.",
        ep_duration="55m",
        ep_poster="https://occ-0-300-325.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABbARELvP6isNm5sHcvW4fgQyaff64BK9DcyIVRNotr8sm01spljhJBew99EMuYev1E58_2vbSa3xfxKCxrh3EdUupRyCUcwwXIUGVaqL__WvlMWR2hDqbG9N.jpg"
    )
    tv_episode79 = TVShowEpisodes(
        tv_id=8,
        ep_number=4,
        ep_name="Stick to the Team",
        ep_description="As alliances form among the players, no one is safe in the dorm after lights-out. The third game challenges Gi-hun's team to think strategically.",
        ep_duration="56m",
        ep_poster="https://occ-0-300-325.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABfULc6d4fbnWvJ3kp8idjBKtpmLkQG26rHgkPoZn7-YnjblZ94GTR-tL9a7A9cOKh90kjTmC58U_QABJpNj5irSClb1iQAQEKVqh9evgb9NUfgYshfAj0T3m.jpg"
    )
    tv_episode80 = TVShowEpisodes(
        tv_id=8,
        ep_number=5,
        ep_name="A Fair World",
        ep_description="Gi-hun and his team take turns keeping guard through the night. The masked men encounter trouble with their co-conspirators.",
        ep_duration="52m",
        ep_poster="https://occ-0-300-325.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABayNMtg7c4dQ8I1vSbye_mXDsE8er_YuwdkmVnQ2WLcGPRSLyd9_ZyL8o9EEJT_1R2gZXc6kz_HkkHp4O4442H3Pfnqi8vHJPISMWcXgPfyh9PB8MQptrg6g.jpg"
    )
    tv_episode81 = TVShowEpisodes(
        tv_id=8,
        ep_number=6,
        ep_name="Gganbu",
        ep_description="Players pair off for the fourth game. Gi-hun grapples with a moral dilemma, Sang-woo chooses self-preservation and Sae-byeok shares her untold story.",
        ep_duration="62m",
        ep_poster="https://occ-0-300-325.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABYeAqA0G2uvoQS8qN2q-FS4pV3qFLEoKhtIU9ppSsPSqswtxaWcmt89kyA8-yteGYzicIkp0c3FrCV_oR4zurvcx3D-7Q8c204XLhUnqbj6xectZY8uTS0Yo.jpg"
    )
    tv_episode82 = TVShowEpisodes(
        tv_id=8,
        ep_number=7,
        ep_name="VIPS",
        ep_description="The Masked Leader welcomes VIP guests to the facility for a front-row viewing of the show. In the fifth game, some players crack under pressure.",
        ep_duration="58m",
        ep_poster="https://occ-0-300-325.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABYFD63meHAceg_zjRpkx1u86sr9FEGPJNWBQloq5Ywbex4JU1dfwtyi7SWrpftaYZr3JxLtGdSuxfXRA6XnJYvP1u1WUS9fQjsX2uV-_iRmJeTSl0QQt7P84.jpg"
    )
    tv_episode83 = TVShowEpisodes(
        tv_id=8,
        ep_number=8,
        ep_name="Front Man",
        ep_description="Ahead of the last round, distrust and disgust run deep among the finalists. Jun-ho makes a getaway, determined to expose the game's dirty secrets.",
        ep_duration="33m",
        ep_poster="https://occ-0-300-325.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABRtEUf0r5ZlEO9TBKpla-ViSRU4flRZsFDpb_UZlZTyodClVp636EfLg0ZF1he4IDTY4e8LbvyWGakt9Kz3e-0GrMaaLyfm9U0TJKt5Vi6LVjAmgwOyfm3l4.jpg"
    )
    tv_episode84 = TVShowEpisodes(
        tv_id=8,
        ep_number=9,
        ep_name="One Lucky Day",
        ep_description="The final round presents another cruel test — but this time, how it ends depends on just one player. The game's creator steps out of the shadows.",
        ep_duration="56m",
        ep_poster="https://occ-0-300-325.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABYuDBORiZZ6UTJ-SNSjZObcUQ5zAv3bp2ii2id7yAODy90wk4Tjp4ah-rAESVX0N-0zk0uofP4jB8W8BXPLfDujwvLhNC2CDiBWtNX5ynvWQjy7h_8cha8Gt.jpg"
    )
    ##wednesday
    tv_episode85 = TVShowEpisodes(
        tv_id=9,
        ep_number=1,
        ep_name="Wednesday's Child Is Full of Woe",
        ep_description="When a deliciously wicked prank gets Wednesday expelled, her parents ship her off to Nevermore Academy, the boarding school where they fell in love.",
        ep_duration="59m",
        ep_poster="https://occ-0-993-2433.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABcI5SSc8tsgcpT-6RUHuB0n7iuZ_d9DBIJORfPL-AOimOsg5G56qnJHTY39TlAGDewFM7IqVcFGflR4u8X4kZoWXXJKpdFtZfwuL9qcuV7vnZ8ArEWVdnurT.jpg"
    )
    tv_episode86 = TVShowEpisodes(
        tv_id=9,
        ep_number=2,
        ep_name="Woe is the Loneliest Number",
        ep_description="The sheriff questions Wednesday about the night's strange happenings. Later, Wednesday faces off against a fierce rival in the cutthroat Poe Cup race.",
        ep_duration="48m",
        ep_poster="https://occ-0-993-2433.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABRimuBP1gFARJ2texmP9BRCpNBHS6BPxywXYxqxfgXWrDZzrdd2al5Ic5HSVQjIPZz067PBk-8WODwDeNzkgtyDw7AubISms2gkY1Oja5_R5yY6oWV6x1EO7.jpg"
    )
    tv_episode87 = TVShowEpisodes(
        tv_id=9,
        ep_number=3,
        ep_name="Friend or Woe",
        ep_description="Wednesday stumbles on a secret society. During Outreach Day, Nevermore's outcasts mingle with Jericho's normies in Pilgrim World. Fudge, anyone?",
        ep_duration="48m",
        ep_poster="https://occ-0-993-2433.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABbPdO8OO3wIb08psCFqR9zfKRfFKOHjCgwDjfjsJe51EIa29w6PwpCo1CX7OH3azauUMoBCtJyKseGEXF9fiEXCJQCIvPmSodYKGVWVlPNz3qx_yxKW5dvLS.jpg"
    )
    tv_episode88 = TVShowEpisodes(
        tv_id=9,
        ep_number=4,
        ep_name="Woe What a Night",
        ep_description="Wednesday asks Xavier to the Rave'N dance, sparking Tyler's jealousy — but Thing's got something up his sleeve. Meanwhile, Eugene stakes out the cave.",
        ep_duration="49m",
        ep_poster="https://occ-0-993-2433.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABcSTk3X_aULK7m9O2ibOxQxd2nMQdAlNKIcL1tzFSbqXH_09IF9XORxeHTrRuDyBotqhuiCRgK8DsAkb08zJhCE_EiaKRNXNxS_Sr4fmyrbL2ihrPE3ZZNWM.jpg"
    )
    tv_episode89 = TVShowEpisodes(
        tv_id=9,
        ep_number=5,
        ep_name="You Reap What You Woe",
        ep_description="During Parents Weekend, Wednesday digs into her family's past — and accidentally gets her dad arrested. Enid feels the pressure to 'wolf out.'",
        ep_duration="52m",
        ep_poster="https://occ-0-993-2433.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABTkygdlRrjkCgCuY9_Awri731V4z-T2E8K8F1WkE4nf_Q7ZQE9qw5K5pKdBvSZsUmCklV9BA22DaRqVc_8dWgxya7MGDST5IbEPPPOeNqYrXEJvUmGAtaGpO.jpg"
    )
    tv_episode90 = TVShowEpisodes(
        tv_id=9,
        ep_number=6,
        ep_name="Quid Pro Woe",
        ep_description="Wednesday's friends throw her a surprise birthday party. They mean well... but she'd much rather mark the miserable occasion by solving the murders.",
        ep_duration="50m",
        ep_poster="https://occ-0-395-420.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABftwPVi5K-gtO5KPplQFMGUlIX-xBA82-m75iuZ-FuuELSKzWn7L2PFrhl8RFEHuM-GQlIiUYcsXAehRsR3GI7nkPuw3bxXtGg4hfJoGM_TBjBp7zjKvUjka.jpg"
    )
    tv_episode91 = TVShowEpisodes(
        tv_id=9,
        ep_number=7,
        ep_name="If You Don't Woe Me by Now",
        ep_description="Kooky Uncle Fester pays a visit and shares his theory about the monster. Wednesday begrudgingly agrees to a date with Tyler at Crackstone's crypt.",
        ep_duration="47m",
        ep_poster="https://occ-0-993-2433.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABQODYcdhitU30HQhDLH69j3CB9Q-krxJpDRBr6jErexSG2pFi7cGKGzohRacO4qKvYRG0fi6VxcZymmRJ9zhx0ZeUlwudCI9CHInNovbBsd7RZU2YIJIW6yT.jpg"
    )
    tv_episode92 = TVShowEpisodes(
        tv_id=9,
        ep_number=8,
        ep_name="A Murder of Woes",
        ep_description="Wednesday lands in trouble with Principal Weems, but that's just the start of her problems. To fight an ancient evil, she'll need all her friends' help.",
        ep_duration="52m",
        ep_poster="https://occ-0-993-2433.1.nflxso.net/dnm/api/v6/9pS1daC2n6UGc3dUogvWIPMR_OU/AAAABQ3m240NGklfP7iLk_Nos3X_3zq9-VcJ_P9NMGwnCybY7bldlYOD8ohUWxi1nDKDU2K8PuYzgEfYaU84cBFmJ4oifYfTyaU3EW66NtxiwqTf51OcRSyhis_2.jpg"
    )

    
