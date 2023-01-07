import React, {useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
// Import Swiper React components
import { Swiper, SwiperSlide } from "swiper/react";

// Import Swiper styles
import 'swiper/swiper.min.css';
import 'swiper/modules/pagination/pagination.min.css';
import 'swiper/modules/navigation/navigation.min.css';

import './styles.css';

// import required modules
import { Pagination, Navigation } from "swiper";
import { getAllMoviesThunk } from '../../store/movies';


export default function HomePageCarousel() {
    const dispatch = useDispatch();
    const movies = Object.values(useSelector(state => state.movies))
    const moviesCarousel = movies.slice(0, 18)

    useEffect(() => {
        dispatch(getAllMoviesThunk())
    }, [dispatch])

    if (!movies) return null;

    return (
        <div className="whole-carousel-outer-div">
        <h1 className="movie-carousel-title">Movies</h1>
          <Swiper
            slidesPerView={6}
            spaceBetween={10}
            slidesPerGroup={6}
            loop={true}
            loopFillGroupWithBlank={true}
            pagination={{
              clickable: true,
              type: 'bullets'
            }}
            navigation={true}
            modules={[Pagination, Navigation]}
            className="mySwiper"
          >{
            moviesCarousel.map(movie => (
                <SwiperSlide>
                    <img src={movie.prev_img} alt='movie poster'></img>
                </SwiperSlide>
            ))
          }
          </Swiper>
        </div>
      );
}
