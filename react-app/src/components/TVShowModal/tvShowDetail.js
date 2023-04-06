import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { useHistory, useParams } from "react-router-dom";
import MovieReviewComponent from "../MovieReview/MovieReview";
import { getTvShowEpisodesThunk } from "../../store/tvepisodes";
// import { getMoviesGenresThunk } from "../../store/genresmovies";
// import "./movieModal.css";

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
            newString.push(genres[i].genre_name, ", ");
        }
        let lastgenre= genres[genres.length - 1];
        newString.push(lastgenre.genre_name);
        return newString.join("")
    }

    useEffect(() => {
        dispatch(getTvShowEpisodesThunk(tvId))
    }, [dispatch, tvId])

    if(!tvShow) return null;

    return (
        <div className="outer-whole-movie-modal">
            <div className="top-half-movie-modal"
                style={{
                    backgroundSize: "cover",
                    backgroundImage: `url("${tvShow.detail_img}")`,
                    backgroundPosition: 'center center'
                }}
            >
                <div className='movie-modal-functions'>
                    <NavLink to={`/${profId}/watchTV/${tvShow.id}`} exact='true'>
                        <button className='play-header-button-modal'>
                            <i class="fa-sharp fa-solid fa-play"></i>
                            Play
                        </button>
                    </NavLink>
                    {/* <div className="add-to-my-list-modal">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M11 2V11H2V13H11V22H13V13H22V11H13V2H11Z" fill="currentColor"></path></svg>
                </div> */}
                    {/* <MovieReviewComponent movieId={movieId}/> */}
                </div>
            </div>
            <div className='fade-bottom-modal'></div>
            <div className="bottom-half-movie-modal">
                <h1 className="movie-title-modal">{tvShow.tv_name}</h1>
                <div className="middle-details-modal">
                    <div className="left-side-modal-details">
                        <div className="top-mid-movie-dets">
                            <h3 className="moviemodal-yr">{tvShow.year}</h3>
                            <div className='modal-rating-border'>
                                {tvShow.rating}
                            </div>
                            <h3 className="moviemodal-duration">{tvShow.num_seasons}</h3>
                        </div>
                        <div className="bottom-mid-movie-dets">
                            <h4>{tvShow.description}</h4>
                        </div>
                    </div>
                    <div className="right-side-modal-details">
                        <div className="indiv-modal-right-details">
                            <span className="modal-midd-right-txt" id="label-grey">Cast: </span>
                            <span className="modal-midd-right-txt"> {tvShow.cast}</span>
                        </div>
                        <div className="indiv-modal-right-details">
                            <span className="modal-midd-right-txt" id="label-grey">Genres: </span>
                            <span className="modal-midd-right-txt">{getGenres(tvShow.genres)}</span>
                        </div>
                        <div className="indiv-modal-right-details">
                            <span className="modal-midd-right-txt" id="label-grey">This Movie is: </span>
                            <span className="modal-midd-right-txt"> {tvShow.tv_is}</span>
                        </div>
                    </div>
                </div>
                {/* !!!episodes go here */}
                {episodes.map((episode) => (
                    <div>
                        <img src={episode.ep_poster} alt="episode poster" />                 
                    </div>
                ))}
                <div className="more-about-movie-modal">
                    <h3 className="movie-more-modal">About {tvShow.tv_name}</h3>
                    <div className="indiv-modal-right-details">
                        <span className="smaller-more-txt" id="label-grey">Cast: </span>
                        <span className="smaller-more-txt">{tvShow.cast}</span>
                    </div>
                    <div className="indiv-modal-right-details">
                        <span className="smaller-more-txt" id="label-grey">Creators: </span>
                        <span className="smaller-more-txt">{tvShow.creators}</span>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default TVDetail;
