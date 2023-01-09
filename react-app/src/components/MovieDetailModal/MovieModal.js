import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { useHistory, useParams } from "react-router-dom";
import MovieReviewComponent from "../MovieReview/MovieReview";
import { getMoviesGenresThunk } from "../../store/genresmovies";
import "./movieModal.css";

function MovieDetail({ setShowModal, movieId }) {
    const dispatch = useDispatch();
    const history = useHistory();
    const { profId } = useParams();
    const movie = useSelector(state => state.movies[movieId])
    const movieGenres = Object.values(useSelector(state => state.movieGenres))
    const [movGenres, setMovieGenres] = useState("")
    // const currMovie = movies[movieId]
    console.log(movieGenres)

    useEffect(() => {
        dispatch(getMoviesGenresThunk(movieId))
    }, [movieId, dispatch]);

    const movieGenreWord = () => {
        let newWords = [];
        for (let i = 0; i < movieGenres.length - 1; i++) {
            let curr = movieGenres[i]
            newWords.push(curr.genre_name, ", ");
        }
        let last = movieGenres[movieGenres.length - 1]
        newWords.push(last?.genre_name)
        let newGenres = newWords.join("")
        return newGenres;
    }

    return (
        <div className="outer-whole-movie-modal">
            <div className="top-half-movie-modal"
                style={{
                    backgroundSize: "cover",
                    backgroundImage: `url("${movie.detail_img}")`,
                    backgroundPosition: 'center center'
                }}
            >
                <div className='movie-modal-functions'>
                    <NavLink to={`/${profId}/watch/${movieId}`} exact='true'>
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
                <h1 className="movie-title-modal">{movie.movie_name}</h1>
                <div className="middle-details-modal">
                    <div className="left-side-modal-details">
                        <div className="top-mid-movie-dets">
                            <h3 className="moviemodal-yr">{movie.year}</h3>
                            <div className={`modal-rating-border ${movie.rating == "R" || movie.rating == "G" || movie.rating == "PG" ? "smaller-rating" : ""}`}>
                                {movie.rating}
                            </div>
                            <h3 className="moviemodal-duration">{movie.duration}</h3>
                        </div>
                        <div className="bottom-mid-movie-dets">
                            <h4>{movie.description}</h4>
                        </div>
                    </div>
                    <div className="right-side-modal-details">
                        <div className="indiv-modal-right-details">
                            <span className="modal-midd-right-txt" id="label-grey">Cast: </span>
                            <span className="modal-midd-right-txt"> {movie.cast}</span>
                        </div>
                        <div className="indiv-modal-right-details">
                            <span className="modal-midd-right-txt" id="label-grey">Genres: </span>
                            <span className="modal-midd-right-txt">{movieGenreWord()}</span>
                        </div>
                        <div className="indiv-modal-right-details">
                            <span className="modal-midd-right-txt" id="label-grey">This Movie is: </span>
                            <span className="modal-midd-right-txt"> {movie.movie_is}</span>
                        </div>
                    </div>
                </div>
                <div className="more-about-movie-modal">
                    <h3 className="movie-more-modal">About {movie.movie_name}</h3>
                    <div className="indiv-modal-right-details">
                        <span className="smaller-more-txt" id="label-grey">Director: </span>
                        <span className="smaller-more-txt">{movie.director}</span>
                    </div>
                    <div className="indiv-modal-right-details">
                        <span className="smaller-more-txt" id="label-grey">Writer: </span>
                        <span className="smaller-more-txt">{movie.writer}</span>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default MovieDetail;
