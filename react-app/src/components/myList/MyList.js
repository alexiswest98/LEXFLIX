import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, Link, useHistory } from "react-router-dom";
import { getAllMyListThunk } from "../../store/mylist";
import { movieIs } from "../../store/repeatfuncs";
import MovieDetail from "../MovieDetailModal/MovieModal";
import TVDetail from "../TVShowModal/tvShowDetail";
import { Modal } from '../../context/Modal';
import MovieReviewComponent from "../MovieReview/MovieReview";
import TvReviewComponent from "../tvShowReview/tvShowReview";
import { getAllMoviesThunk } from "../../store/movies";
import { getAllTvShowsThunk } from "../../store/tvshows";
import { deleteMyListThunk } from "../../store/mylist";
import { getAllReviewsThunk } from "../../store/reviews";
import { getAllTvReviewsThunk } from "../../store/tvreviews";
import './myList.css';

export default function MyList() {
    const dispatch = useDispatch();
    const history = useHistory();
    const { profId } = useParams();
    const media = Object.values(useSelector(state => state.myList))
    const [isOver, setIsOver] = useState(false)
    const [selectedIndex, setSelectedIndex] = useState(null)
    const [showModal, setShowModal] = useState(false);
    const [mediaId, setMediaId] = useState(0);
    //testing re render after delete
    const [count, setCount] = useState(0);
    const [allmedia, setMedia] = useState([]);

    // console.log("SELECTED INDEX", selectedIndex)

    useEffect(() => {
        dispatch(getAllMoviesThunk())
        dispatch(getAllTvShowsThunk())
        dispatch(getAllMyListThunk(+profId))
        dispatch(getAllReviewsThunk(+profId))
        dispatch(getAllTvReviewsThunk(+profId))

        const fetchMedia = async () => {
            setMedia(media)
        }
        fetchMedia()
    }, [dispatch, profId, count]);


    const needsRightHover = (idx) => {
        if (idx === 4 || idx === 9 || idx === 14 || idx === 19 || idx === 24) return true;

    }

    const needsLeftHover = (idx) => {
        if (idx === 0 || idx === 5 || idx === 10 || idx === 15 || idx === 20) return true;
    }

    //need some way to differentiate between tv and movies 
    const isMovie = (mediaId) => {
        const curr = media.find(media => media.id === mediaId)
        if (curr.movie_id) return true;
        if(curr.tv_id) return false;
        return false;
    }

    // console.log("!!!!!!!!", isMovie(10))

    const deleteFromMyList = async (mediaId) => {
        await dispatch(deleteMyListThunk(mediaId))
        setCount(count + 1);
    }


    if (!media || media.includes(404)) return (
        <div className="my-list-container">
            <div className="my-list-title-container">
                <h1 className="my-list-title">My List</h1>
            </div>
            <div className="no-mylist-container">
                <h2 className="no-mylist-media">You haven't added any titles to your list yet.</h2>
            </div>
        </div>
    )


    return (
        <div className="my-list-container">
            <div className="my-list-title-container">
                <h1 className="my-list-title">My List</h1>
            </div>
            <div className="media-container">
                {media.map((med, idx) => (
                    isMovie(med.id) ? (
                        //movie component first
                        <div className="indiv-media-card">
                            <div className={`${!isOver || selectedIndex !== idx
                                ? "my-list-media"
                                : "hover-effect"} ${isOver && selectedIndex === idx && needsLeftHover(idx) && "left-hover-mylist"}`}
                                id={isOver && selectedIndex === idx && needsRightHover(idx) && "right-hover-mylist"}
                                key={med.id}
                                onMouseOver={() => {
                                    //have to have conditional so when modal is open, it doesn't trigger the hover effect
                                    if (!showModal) {
                                        setIsOver(true);
                                        setSelectedIndex(idx);
                                    }
                                }}
                                onMouseOut={() => {
                                    setIsOver(false);
                                    setSelectedIndex(null);
                                }}
                            >
                                <img className="my-list-media-image" src={med.detail_img} alt="media-image" />
                                <div className="hidden-details-info">
                                    <div className="top-half-hidden-details">
                                        <Link to={`/${profId}/watch/${med.movie_id}`} className="play-butt-details my-list-grow">
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 2.69127C4 1.93067 4.81547 1.44851 5.48192 1.81506L22.4069 11.1238C23.0977 11.5037 23.0977 12.4963 22.4069 12.8762L5.48192 22.1849C4.81546 22.5515 4 22.0693 4 21.3087V2.69127Z" fill="currentColor"></path></svg>
                                        </Link>
                                        <div className="add-to-my-list my-list-grow"
                                            onClick={() => deleteFromMyList(med.id)}>
                                            {/* <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M11 2V11H2V13H11V22H13V13H22V11H13V2H11Z" fill="currentColor"></path></svg> */}
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="Hawkins-Icon Hawkins-Icon-Standard"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.68239 19.7312L23.6824 5.73115L22.3178 4.26904L8.02404 17.6098L2.70718 12.293L1.29297 13.7072L7.29297 19.7072C7.67401 20.0882 8.28845 20.0988 8.68239 19.7312Z" fill="currentColor"></path></svg>
                                        </div>
                                        <MovieReviewComponent movieId={med.movie_id} />
                                        <div className="get-details-button-list" onClick={() => {
                                            setShowModal(true)
                                            setMediaId(med.movie_id)
                                            // setIsOver(false);
                                            // setSelectedIndex(null);
                                        }}>
                                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="down-arrow-details"><path fill-rule="evenodd" clip-rule="evenodd" d="M19.293 7.29297L12.0001 14.5859L4.70718 7.29297L3.29297 8.70718L11.293 16.7072C11.4805 16.8947 11.7349 17.0001 12.0001 17.0001C12.2653 17.0001 12.5196 16.8947 12.7072 16.7072L20.7072 8.70718L19.293 7.29297Z" fill="currentColor"></path></svg>
                                        </div>
                                        {showModal && (
                                            <Modal onClose={() => setShowModal(false)}>
                                                <MovieDetail setShowModal={setShowModal} movieId={mediaId} />
                                            </Modal>
                                        )}

                                    </div>
                                    <div className="bottom-half-hidden-details">
                                        <div className="top-bottom-movie-details">
                                            <span className="new-span-list">New</span>
                                            <div className={`movie-detail-rating ${med.movie_rating == "R" || med.movie_rating == "G" || med.movie_rating == "PG" ? "smaller-rating" : ""}`}>
                                                <span className="movie-rating-txt-list">{med.movie_rating}</span>
                                            </div>
                                            <span className="movie-duration-list">{med.movie_duration}</span>
                                        </div>
                                        <div className="bott-bottom-movie-details">
                                            <span className="movie-is-text-list">{med.movie_is}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>) :
                        //tv show render looks different goes here
                        (
                            <div className="indiv-media-card">
                                <div className={`${!isOver || selectedIndex !== idx
                                    ? "my-list-media"
                                    : "hover-effect"} ${isOver && selectedIndex === idx && needsLeftHover(idx) && "left-hover-mylist"}`}
                                    id={isOver && selectedIndex === idx && needsRightHover(idx) && "right-hover-mylist"}
                                    key={med.id}
                                    onMouseOver={() => {
                                        //have to have conditional so when modal is open, it doesn't trigger the hover effect
                                        if (!showModal) {
                                            setIsOver(true);
                                            setSelectedIndex(idx);
                                        }
                                    }}
                                    onMouseOut={() => {
                                        setIsOver(false);
                                        setSelectedIndex(null);
                                    }}
                                >
                                    <img className="my-list-media-image" src={med.detail_img} alt="media-image" />
                                    <div className="hidden-details-info">
                                        <div className="top-half-hidden-details">
                                            <Link to={`/${profId}/watchTV/${med.tv_id}`} className="play-butt-details my-list-grow">
                                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 2.69127C4 1.93067 4.81547 1.44851 5.48192 1.81506L22.4069 11.1238C23.0977 11.5037 23.0977 12.4963 22.4069 12.8762L5.48192 22.1849C4.81546 22.5515 4 22.0693 4 21.3087V2.69127Z" fill="currentColor"></path></svg>
                                            </Link>
                                            <div className="add-to-my-list my-list-grow"
                                                onClick={() => deleteFromMyList(med.id)}>
                                                {/* <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M11 2V11H2V13H11V22H13V13H22V11H13V2H11Z" fill="currentColor"></path></svg> */}
                                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="Hawkins-Icon Hawkins-Icon-Standard"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.68239 19.7312L23.6824 5.73115L22.3178 4.26904L8.02404 17.6098L2.70718 12.293L1.29297 13.7072L7.29297 19.7072C7.67401 20.0882 8.28845 20.0988 8.68239 19.7312Z" fill="currentColor"></path></svg>
                                            </div>
                                            <TvReviewComponent tvId={med.tv_id} />
                                            <div className="get-details-button-list" onClick={() => {
                                                setShowModal(true)
                                                setMediaId(med.tv_id)
                                                // setIsOver(false);
                                                // setSelectedIndex(null);
                                            }}>
                                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="down-arrow-details"><path fill-rule="evenodd" clip-rule="evenodd" d="M19.293 7.29297L12.0001 14.5859L4.70718 7.29297L3.29297 8.70718L11.293 16.7072C11.4805 16.8947 11.7349 17.0001 12.0001 17.0001C12.2653 17.0001 12.5196 16.8947 12.7072 16.7072L20.7072 8.70718L19.293 7.29297Z" fill="currentColor"></path></svg>
                                            </div>
                                            {showModal && (
                                                <Modal onClose={() => setShowModal(false)}>
                                                    <TVDetail setShowModal={setShowModal} tvId={mediaId} />
                                                </Modal>
                                            )}

                                        </div>
                                        <div className="bottom-half-hidden-details">
                                            <div className="top-bottom-movie-details">
                                                <span className="new-span-list">New</span>
                                                <div className="movie-detail-rating">
                                                    <span className="movie-rating-txt-list">{med.tv_rating}</span>
                                                </div>
                                                <span className="movie-duration-list">{med.num_seasons}</span>
                                            </div>
                                            <div className="bott-bottom-movie-details">
                                                <span className="movie-is-text-list">{med.tv_is}</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>)
                ))}
            </div>
        </div>
    );
}

//relative parent 
//absolute 
//absolute
//id={isOver && selectedIndex === idx && needsRightHover(idx) && "right-hover-mylist"}
