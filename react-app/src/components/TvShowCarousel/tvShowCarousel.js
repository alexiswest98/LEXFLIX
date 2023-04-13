import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

// Import Swiper React components
import { useParams } from "react-router-dom";
import { Swiper, SwiperSlide } from "swiper/react";

import TvReviewComponent from "../tvShowReview/tvShowReview";
import { getAllTvReviewsThunk } from "../../store/tvreviews";
import { getAllMyListThunk } from "../../store/mylist";
import { Modal } from '../../context/Modal';
import TVDetail from "../TVShowModal/tvShowDetail";
import { deleteMyListThunk } from "../../store/mylist";
import {addTVMyListThunk} from "../../store/mylist";
import { movieIs } from "../../store/repeatfuncs";

// Import Swiper styles
import 'swiper/swiper.min.css';
import 'swiper/modules/pagination/pagination.min.css';
import 'swiper/modules/navigation/navigation.min.css';

// import required modules
import { Pagination, Navigation } from "swiper";
import { getAllTvShowsThunk } from "../../store/tvshows";
import { Link } from "react-router-dom";


export default function TVShowCarousel() {
  const dispatch = useDispatch();
  const tvshows = Object.values(useSelector(state => state.tvShow))
  const myList = Object.values(useSelector(state => state?.myList))
  const { profId } = useParams();
  const [currTvId, setCurrTvId] = useState();
  const [showModal, setShowModal] = useState(false);
  const [isOver, setIsOver] = useState(false)
  const [count, setCount] = useState(0);

  useEffect(() => {
    dispatch(getAllTvShowsThunk())
    dispatch(getAllTvReviewsThunk(+profId))
    dispatch(getAllMyListThunk(+profId))
  }, [dispatch, profId, count])

  //MY LIST FUNCTIONALITY
  const isInMyList = (tvId) => {
    for (let i = 0; i < myList.length; i++) {
      if (myList[i].tv_id === tvId) return true;
    }
    return false;
  }

  const findMediaId = (tvId) => {
    for (let i = 0; i < myList.length; i++) {
      if (myList[i].tv_id === tvId) return myList[i].id;
    }
  }

  // console.log(findMediaId(1))

  const deleteFromMyList = async (mediaId) => {
    await dispatch(deleteMyListThunk(mediaId))
  }

  const addToMyList = async (tvId) => {
    await dispatch(addTVMyListThunk(+profId, tvId))
    setCount(count + 1);
  }

  //CSS FUNCTIONS
  const hoverRight = (num) => {
    if (num === 1 || num === 7 || num === 13) return true;
  }

  const hoverLeft = (num) => {
    if (num === 6 || num === 12 || num === 18) return true;
  }

  if (!tvshows) return null;

  return (
    <div className="whole-carousel-outer-div">
      <h1 className="movie-carousel-title">TV Shows</h1>
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
        id={isOver && "bigger-zindex"}
        allowTouchMove={false}
      >{
        tvshows.map((show, idx) => (
            <SwiperSlide>
              <div className={`swiper-indiv-div ${hoverRight(show.id) && "hover-entire-right"} ${hoverLeft(show.id) && "hover-entire-left"}`}
                onMouseOver={() => {
                  //have to have conditional so when modal is open, it doesn't trigger the hover effect
                  if (!showModal) {
                    setIsOver(true);
                  }
                }}
                onMouseOut={() => {
                  setIsOver(false);
                }}
              >
                <img src={show.prev_img} alt='movie poster' className="swiper-img" onMouseOver={() => setCurrTvId(show.id)}></img>
                {/* {console.log("------------", currMovieId)} */}
                <div className="hidden-details-info">
                  <div className="top-half-hidden-details">
                    <Link to={`/${profId}/watchTV/${show.id}`} className="play-butt-details">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 2.69127C4 1.93067 4.81547 1.44851 5.48192 1.81506L22.4069 11.1238C23.0977 11.5037 23.0977 12.4963 22.4069 12.8762L5.48192 22.1849C4.81546 22.5515 4 22.0693 4 21.3087V2.69127Z" fill="currentColor"></path></svg>
                    </Link>
                    {isInMyList(show.id) ? (
                      <div className="add-to-my-list"
                        onClick={() => {
                          const mediaId = findMediaId(show.id)
                          deleteFromMyList(mediaId)
                        }}>
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.68239 19.7312L23.6824 5.73115L22.3178 4.26904L8.02404 17.6098L2.70718 12.293L1.29297 13.7072L7.29297 19.7072C7.67401 20.0882 8.28845 20.0988 8.68239 19.7312Z" fill="currentColor"></path></svg>
                      </div>
                    ) :
                      (
                        <div className="add-to-my-list" onClick={() => addToMyList(show.id)}>
                          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M11 2V11H2V13H11V22H13V13H22V11H13V2H11Z" fill="currentColor"></path></svg>
                        </div>
                      )}
                    <TvReviewComponent tvId={currTvId} />
                    <div className="get-details-button" onClick={() => setShowModal(true)}>
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="down-arrow-details"><path fill-rule="evenodd" clip-rule="evenodd" d="M19.293 7.29297L12.0001 14.5859L4.70718 7.29297L3.29297 8.70718L11.293 16.7072C11.4805 16.8947 11.7349 17.0001 12.0001 17.0001C12.2653 17.0001 12.5196 16.8947 12.7072 16.7072L20.7072 8.70718L19.293 7.29297Z" fill="currentColor"></path></svg>
                    </div>
                    {showModal && (
                      <Modal onClose={() => setShowModal(false)}>
                        <TVDetail setShowModal={setShowModal} tvId={currTvId} />
                      </Modal>
                    )}
                  </div>
                  <div className="bottom-half-hidden-details">
                    <div className="top-bottom-movie-details">
                      <span className="new-span">New</span>
                      <div className='movie-detail-rating'>
                        <span className="movie-rating-txt">{show.rating}</span>
                      </div>
                      <span className="movie-duration">{show.num_seasons}</span>
                    </div>
                    <div className="bott-bottom-movie-details">
                      <span className="movie-is-text">{movieIs(show.tv_is)}</span>
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
