import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
// Import Swiper React components
import { useParams } from "react-router-dom";
import { Swiper, SwiperSlide } from "swiper/react";
import MovieReviewComponent from "../MovieReview/MovieReview";
import { getAllReviewsThunk } from "../../store/reviews";
import { Modal } from '../../context/Modal';
import MovieDetail from "../MovieDetailModal/MovieModal";

// Import Swiper styles
import 'swiper/swiper.min.css';
import 'swiper/modules/pagination/pagination.min.css';
import 'swiper/modules/navigation/navigation.min.css';

import './styles.css';

// import required modules
import { Pagination, Navigation } from "swiper";
import { getAllMoviesThunk } from '../../store/movies';
import { Link } from "react-router-dom";


export default function HomePageCarousel() {
  const dispatch = useDispatch();
  const movies = Object.values(useSelector(state => state.movies))
  const moviesCarousel = movies.slice(0, 18)
  const { profId } = useParams();
  const [currMovieId, setCurrMovieId] = useState();
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    dispatch(getAllMoviesThunk())
    dispatch(getAllReviewsThunk(+profId))
  }, [dispatch, profId])

  // const setMovieId = (movieId) => {
  //   setCurrMovieId(movieId);
  // };

  // useEffect(() => {
  //   if (!currMovieId) return;

  //   //event listener for drop down menu
  //   document.addEventListener('mouseover', setMovieId);
  //   //clean up
  //   // return () => document.removeEventListener("click", closeMenu);
  // }, [showMenu])

  const movieIs = (string) => {
    const words = string.split(',');
    let newWords = [];
    for (let i = 0; i < words.length - 1; i++) {
      newWords.push(words[i], " · ");
    }
    newWords.push(words[words.length - 1])
    return newWords.join("")
  };

  const hoverRight = (num) => {
    if (num == 1 || num == 7 || num == 13) return true;
  }

  const hoverLeft = (num) => {
    if (num == 6 || num == 12 || num == 18) return true;
  }

  if (!movies) return null;

  return (
    <div className="whole-carousel-outer-div">
      <h1 className="movie-carousel-title">Movies</h1>
      <Swiper
        slidesPerView={6}
        spaceBetween={7}
        slidesPerGroup={6}
        loop={true}
        loopFillGroupWithBlank={true}
        pagination={{
          clickable: true
        }}
        navigation={true}
        modules={[Pagination, Navigation]}
        className="mySwiper"
        allowTouchMove={false}
      >{
          moviesCarousel.map(movie => (
            <SwiperSlide>
              <div className={`swiper-indiv-div ${hoverRight(movie.id) && "hover-entire-right"} ${hoverLeft(movie.id) && "hover-entire-left"}`}>
                <img src={movie.prev_img} alt='movie poster' className="swiper-img" onMouseOver={() => setCurrMovieId(movie.id)}></img>
                {/* {console.log("------------", currMovieId)} */}
                <div className="hidden-details-info">
                  <div className="top-half-hidden-details">
                    <Link to={`/${profId}/watch/${movie.id}`} className="play-butt-details">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 2.69127C4 1.93067 4.81547 1.44851 5.48192 1.81506L22.4069 11.1238C23.0977 11.5037 23.0977 12.4963 22.4069 12.8762L5.48192 22.1849C4.81546 22.5515 4 22.0693 4 21.3087V2.69127Z" fill="currentColor"></path></svg>
                    </Link>
                    <div className="add-to-my-list">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M11 2V11H2V13H11V22H13V13H22V11H13V2H11Z" fill="currentColor"></path></svg>
                    </div>
                    <MovieReviewComponent movieId={currMovieId}/>
                    <div className="get-details-button" onClick={() => setShowModal(true)}>
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="down-arrow-details"><path fill-rule="evenodd" clip-rule="evenodd" d="M19.293 7.29297L12.0001 14.5859L4.70718 7.29297L3.29297 8.70718L11.293 16.7072C11.4805 16.8947 11.7349 17.0001 12.0001 17.0001C12.2653 17.0001 12.5196 16.8947 12.7072 16.7072L20.7072 8.70718L19.293 7.29297Z" fill="currentColor"></path></svg>
                    </div>
                    {showModal && (
                      <Modal onClose={() => setShowModal(false)}>
                        <MovieDetail setShowModal={setShowModal} movieId={currMovieId}/>
                      </Modal>
                    )}
                  </div>
                  <div className="bottom-half-hidden-details">
                    <div className="top-bottom-movie-details">
                      <span className="new-span">New</span>
                      <div className={`movie-detail-rating 
                      ${movie.rating == "R"|| movie.rating == "G" || movie.rating == "PG" ? "smaller-rating": ""}`}>
                        <span className="movie-rating-txt">{movie.rating}</span>
                      </div>
                      <span className="movie-duration">{movie.duration}</span>
                    </div>
                    <div className="bott-bottom-movie-details">
                      <span className="movie-is-text">{movieIs(movie.movie_is)}</span>
                    </div>
                  </div>
                </div>
              </div>
            </SwiperSlide>
          ))
        }
      </Swiper>
    </div>
  );
}
