import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Link } from "react-router-dom";
import { useHistory, useParams } from "react-router-dom";
import MovieReviewComponent from "../MovieReview/MovieReview";
import { getTvShowEpisodesThunk } from "../../store/tvepisodes";
// import { getMoviesGenresThunk } from "../../store/genresmovies";
import "./tvShowDetail.css";

function TVDetail({ setShowModal, tvId }) {
    const dispatch = useDispatch();
    const history = useHistory();
    const { profId } = useParams();
    const tvShow = useSelector(state => state.tvShow[tvId])
    const episodes = Object.values(useSelector(state => state.tvShowEpisodes))
    // const [movGenres, setMovieGenres] = useState("")

    const getGenres = (genres) => {
        let newString = [];
        for(let i = 0; i < genres.length - 1; i++) {
            newString.push(genres[i], ", ");
        }
        let lastgenre= genres[genres.length - 1];
        newString.push(lastgenre);
        return newString.join("")
    }

    useEffect(() => {
        dispatch(getTvShowEpisodesThunk(tvId))
    }, [dispatch, tvId])

    if(!tvShow || !episodes) return null;

    return (
        <div className="outer-whole-tv-modal">
            <div className="top-half-tv-modal"
                style={{
                    backgroundSize: "cover",
                    backgroundImage: `url("${tvShow.detail_img}")`,
                    backgroundPosition: 'center center'
                }}
            >
                <div className='tv-modal-functions'>
                    <NavLink to={`/${profId}/watchTV/${tvShow.id}`} exact='true'>
                        <button className='play-header-button-modal-tv'>
                            <i class="fa-sharp fa-solid fa-play"></i>
                            Play
                        </button>
                    </NavLink>
                </div>
            </div>
            <div className='fade-bottom-modal'></div>
            <div className="bottom-half-tv-modal">
                <h1 className="tv-title-modal">{tvShow.tv_name}</h1>
                <div className="middle-details-modal-tv">
                    <div className="left-side-modal-details-tv">
                        <div className="top-mid-tv-dets">
                            <h3 className="tvmodal-yr">{tvShow.year}</h3>
                            <div className='modal-rating-border-tv'>
                                {tvShow.rating}
                            </div>
                            <h3 className="tvmodal-seasons">{tvShow.num_seasons}</h3>
                        </div>
                        <div className="bottom-mid-tv-dets">
                            <h4>{tvShow.description}</h4>
                        </div>
                    </div>
                    <div className="right-side-modal-details-tv">
                        <div className="indiv-modal-right-details-tv">
                            <span className="modal-midd-right-txt-tv" id="label-grey">Cast: </span>
                            <span className="modal-midd-right-txt-tv"> {tvShow.cast}</span>
                        </div>
                        <div className="indiv-modal-right-details-tv">
                            <span className="modal-midd-right-txt-tv" id="label-grey">Genres: </span>
                            <span className="modal-midd-right-txt-tv">{getGenres(tvShow.genres)}</span>
                        </div>
                        <div className="indiv-modal-right-details-tv">
                            <span className="modal-midd-right-txt-tv" id="label-grey">This Show is: </span>
                            <span className="modal-midd-right-txt-tv"> {tvShow.tv_is}</span>
                        </div>
                    </div>
                </div>
                <div className="ep-title-container">
                    <div className="right-side-ep-title">
                        <h2 className="ep-title">Episodes</h2>
                        <h4 className="ep-title-details">Season 1: <span className="rating-border">{tvShow.rating}</span></h4>
                    </div>
                    <div className="left-side-ep-title">
                        <div className="ep-title-box">Season 1</div>
                    </div>

                </div>
                {/* !!!episodes go here */}
                <div className="full-ep-container">
                {episodes.map((episode) => (
                    <div className="indiv-ep-box">
                        <div className='ep-number'>{episode.ep_number}</div>
                        <Link to={`/${profId}/watchTV/${tvId}`} className="tvep-img-div">
                            <img src={episode.ep_poster} alt="episode poster" className="tvep-img"/>
                            <div className="play-ep-div">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="playSVG" data-name="Play"><path d="M4 2.69127C4 1.93067 4.81547 1.44851 5.48192 1.81506L22.4069 11.1238C23.0977 11.5037 23.0977 12.4963 22.4069 12.8762L5.48192 22.1849C4.81546 22.5515 4 22.0693 4 21.3087V2.69127Z" fill="currentColor"></path></svg>
                            </div>
                        </Link>
                        <div className="inner-ep-details">
                            <div className="ep-title-duration-box">
                                <h3 className="indiv-ep-name-title">{episode.ep_name}</h3>
                                <span>{episode.ep_duration}</span>
                            </div>
                            <h5 className="indiv-ep-descr">{episode.ep_description}</h5>
                        </div>               
                    </div>
                ))}
                </div>
                <div className="more-about-tv-modal">
                    <h3 className="tv-more-modal">About {tvShow.tv_name}</h3>
                    <div className="indiv-modal-right-details-tv">
                        <span className="smaller-more-txt-tv" id="label-grey">Creators: </span>
                        <span className="smaller-more-txt-tv">{tvShow.creators}</span>
                    </div>
                    <div className="indiv-modal-right-details-tv">
                        <span className="smaller-more-txt-tv" id="label-grey">Cast: </span>
                        <span className="smaller-more-txt-tv">{tvShow.cast}</span>
                    </div>
                    <div className="indiv-modal-right-details-tv">
                        <span className="smaller-more-txt-tv" id="label-grey">Genres: </span>
                        <span className="smaller-more-txt-tv">{getGenres(tvShow.genres)}</span>
                    </div>
                    <div className="indiv-modal-right-details-tv">
                        <span className="smaller-more-txt-tv" id="label-grey">This Show is: </span>
                        <span className="smaller-more-txt-tv">{tvShow.tv_is}</span>
                    </div>
                </div>
                <div className="seeding-warning">For the sake of seeding countless amounts of episodes, each show only has 1 season :)</div>
            </div>
        </div>
    )
};

export default TVDetail;
