import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { getAllTvShowsThunk } from '../../store/tvshows';
import { getAllTvReviewsThunk } from '../../store/tvreviews';
// import HomePageCarousel from '../HomePageCarousels/HomePageCarousels';
import TVShowCarousel from '../TVShowCarousel/TVShowCarousel';
import { Modal } from '../../context/Modal';
import TVDetail from '../TVShowModal/tvShowDetail';
// import MovieDetail from "../MovieDetailModal/MovieModal";
import avatar from './avatar.jpg';
import './index.css'

export default function ComingSoon() {
    const dispatch = useDispatch();
    const tvshows = Object.values(useSelector(state => state.tvShow))
    const headerShow = Object.values(useSelector(state => state.tvShow))[0]
    const [showModal, setShowModal] = useState(false);
    const { profId } = useParams();

    useEffect(() => {
        dispatch(getAllTvShowsThunk())
        dispatch(getAllTvReviewsThunk(+profId))
    }, [dispatch, profId])

    if (!tvshows || !headerShow) return null;

    return (
        <div className='whole-outer-home-page'>
            <div className='whole-outer-movie-body'
                style={{
                    backgroundSize: "cover",
                    backgroundImage: `url('${avatar}')`,
                    backgroundPosition: 'center center'
                }}>
            </div>
            <div className='banner-buttons'>
                <NavLink to={`/${profId}/watchTV/${headerShow.id}`} exact='true'>
                    <button className='play-header-button'>
                        <i class="fa-sharp fa-solid fa-play"></i>
                        Play
                    </button>
                </NavLink>
                <div className='more-info-details-button' onClick={() => setShowModal(true)}>
                    <svg width="26" height="26" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3C7.02944 3 3 7.02944 3 12C3 16.9706 7.02944 21 12 21C16.9706 21 21 16.9706 21 12C21 7.02944 16.9706 3 12 3ZM1 12C1 5.92487 5.92487 1 12 1C18.0751 1 23 5.92487 23 12C23 18.0751 18.0751 23 12 23C5.92487 23 1 18.0751 1 12ZM13 10V18H11V10H13ZM12 8.5C12.8284 8.5 13.5 7.82843 13.5 7C13.5 6.17157 12.8284 5.5 12 5.5C11.1716 5.5 10.5 6.17157 10.5 7C10.5 7.82843 11.1716 8.5 12 8.5Z" fill="currentColor"></path></svg>
                    <span className='details-button-header'>More Info</span>
                </div>
                {/* !!!!!! */}
                {showModal && (
                      <Modal onClose={() => setShowModal(false)}>
                        <TVDetail setShowModal={setShowModal} tvId={headerShow.id}/>
                      </Modal>
                )}
            </div>
            <div className='fade-bottom'></div>
            <TVShowCarousel/>
            <h1 className='more-movies-holder'></h1>
        </div>
    )
}
