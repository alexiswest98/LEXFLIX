import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getAllMoviesThunk } from "../../store/movies";
import "./movieReview.css"
import td from "../../images/td.png"
import dtu from "../../images/dtu.png"
import td2 from "../../images/td2.png"
import dtu2 from "../../images/dtu2.png"
import textbubb from "../../images/textbubb.png"
import { addReviewThunk } from "../../store/reviews";
import { getAllReviewsThunk } from "../../store/reviews";
import { deleteReviewThunk } from "../../store/reviews";
import { getReviewThunk } from "../../store/reviews";

export default function MovieReviewComponent({ movieId }) {
    const dispatch = useDispatch();
    // const movies = Object.values(useSelector(state => state.movies))
    const allReviews = Object.values(useSelector(state => state.reviews))
    const review = allReviews.filter(rev => rev.movie_id == movieId)[0]
    const { profId } = useParams();
    const [thumbsDowDel, setThumbsDownDel] = useState()
    const [thumbsNeutralDel, setThumbsNeutralDel] = useState()
    const [thumbsUpDel, setThumbsUpDel] = useState()
    // console.log("************", review)

    const isReviewThumbsDown = (movie_id) => {
        if (review.rating === "Thumbs Down") {
            // setThumbsDown(true)
            return true;
        }
        else return false
    }

    const isReviewThumbsNeutral = (movie_id) => {
        if (review.rating === "Thumbs Neutral") {
            // setThumbsNeutral(true)
            return true
        }
        else return false
    }

    const isReviewThumbsUp = (movie_id) => {
        if (review.rating === "Thumbs Up") {
            return true
        }
        else return false
    }

    useEffect(() => {
        //   dispatch(getAllMoviesThunk())
        //   dispatch(getAllReviewsThunk(profId))
        dispatch(getReviewThunk(profId, movieId))
    }, [dispatch, profId, movieId])


    const deleteReview = () => {
        if(review) {
            dispatch(deleteReviewThunk(review.id))
        }
    }

    if (!review) return null;

    return (
        <div className='rate-movie-button'>
            <div className={`thumbs-down-div ${isReviewThumbsDown(movieId) && "extra-styling"}`}>
                {!isReviewThumbsDown(movieId) && <img src={td} className="thumbs-down"></img>}
                {isReviewThumbsDown(movieId) && <img src={td2} className="thumbs-down"></img>}
            </div>
            <div className={`thumbs-up-holder ${isReviewThumbsNeutral(movieId) && "extra-styling"}`}>
                {!isReviewThumbsNeutral(movieId) && <svg width="15" height="15" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="thumbs-up"><path fill-rule="evenodd" clip-rule="evenodd" d="M10.696 8.7732C10.8947 8.45534 11 8.08804 11 7.7132V4H11.8377C12.7152 4 13.4285 4.55292 13.6073 5.31126C13.8233 6.22758 14 7.22716 14 8C14 8.58478 13.8976 9.1919 13.7536 9.75039L13.4315 11H14.7219H17.5C18.3284 11 19 11.6716 19 12.5C19 12.5929 18.9917 12.6831 18.976 12.7699L18.8955 13.2149L19.1764 13.5692C19.3794 13.8252 19.5 14.1471 19.5 14.5C19.5 14.8529 19.3794 15.1748 19.1764 15.4308L18.8955 15.7851L18.976 16.2301C18.9917 16.317 19 16.4071 19 16.5C19 16.9901 18.766 17.4253 18.3994 17.7006L18 18.0006L18 18.5001C17.9999 19.3285 17.3284 20 16.5 20H14H13H12.6228C11.6554 20 10.6944 19.844 9.77673 19.5382L8.28366 19.0405C7.22457 18.6874 6.11617 18.5051 5 18.5001V13.7543L7.03558 13.1727C7.74927 12.9688 8.36203 12.5076 8.75542 11.8781L10.696 8.7732ZM10.5 2C9.67157 2 9 2.67157 9 3.5V7.7132L7.05942 10.8181C6.92829 11.0279 6.72404 11.1817 6.48614 11.2497L4.45056 11.8313C3.59195 12.0766 3 12.8613 3 13.7543V18.5468C3 19.6255 3.87447 20.5 4.95319 20.5C5.87021 20.5 6.78124 20.6478 7.65121 20.9378L9.14427 21.4355C10.2659 21.8094 11.4405 22 12.6228 22H13H14H16.5C18.2692 22 19.7319 20.6873 19.967 18.9827C20.6039 18.3496 21 17.4709 21 16.5C21 16.4369 20.9983 16.3742 20.995 16.3118C21.3153 15.783 21.5 15.1622 21.5 14.5C21.5 13.8378 21.3153 13.217 20.995 12.6883C20.9983 12.6258 21 12.5631 21 12.5C21 10.567 19.433 9 17.5 9H15.9338C15.9752 8.6755 16 8.33974 16 8C16 6.98865 15.7788 5.80611 15.5539 4.85235C15.1401 3.09702 13.5428 2 11.8377 2H10.5Z" fill="currentColor"></path></svg>}
                {isReviewThumbsNeutral(movieId) && <svg width="15" height="15" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg" className="thumbs-up"><path fill-rule="evenodd" clip-rule="evenodd" d="M10.696 8.7732C10.8947 8.45534 11 8.08804 11 7.7132V4H11.8377C12.7152 4 13.4285 4.55292 13.6073 5.31126C13.8233 6.22758 14 7.22716 14 8C14 8.58478 13.8976 9.1919 13.7536 9.75039L13.4315 11H14.7219H17.5C18.3284 11 19 11.6716 19 12.5C19 12.5929 18.9917 12.6831 18.976 12.7699L18.8955 13.2149L19.1764 13.5692C19.3794 13.8252 19.5 14.1471 19.5 14.5C19.5 14.8529 19.3794 15.1748 19.1764 15.4308L18.8955 15.7851L18.976 16.2301C18.9917 16.317 19 16.4071 19 16.5C19 16.9901 18.766 17.4253 18.3994 17.7006L18 18.0006L18 18.5001C17.9999 19.3285 17.3284 20 16.5 20H14H13H12.6228C11.6554 20 10.6944 19.844 9.77673 19.5382L8.28366 19.0405C7.22457 18.6874 6.11617 18.5051 5 18.5001V13.7543L7.03558 13.1727C7.74927 12.9688 8.36203 12.5076 8.75542 11.8781L10.696 8.7732ZM10.5 2C9.67157 2 9 2.67157 9 3.5V7.7132L7.05942 10.8181C6.92829 11.0279 6.72404 11.1817 6.48614 11.2497L4.45056 11.8313C3.59195 12.0766 3 12.8613 3 13.7543V18.5468C3 19.6255 3.87447 20.5 4.95319 20.5C5.87021 20.5 6.78124 20.6478 7.65121 20.9378L9.14427 21.4355C10.2659 21.8094 11.4405 22 12.6228 22H13H14H16.5C18.2692 22 19.7319 20.6873 19.967 18.9827C20.6039 18.3496 21 17.4709 21 16.5C21 16.4369 20.9983 16.3742 20.995 16.3118C21.3153 15.783 21.5 15.1622 21.5 14.5C21.5 13.8378 21.3153 13.217 20.995 12.6883C20.9983 12.6258 21 12.5631 21 12.5C21 10.567 19.433 9 17.5 9H15.9338C15.9752 8.6755 16 8.33974 16 8C16 6.98865 15.7788 5.80611 15.5539 4.85235C15.1401 3.09702 13.5428 2 11.8377 2H10.5Z" fill="currentColor"></path></svg>}
            </div>
            {/* <div className="explanation-review">
                <img src={textbubb} className="textbubb"></img>
            </div> */}
            <div className={`double-thumbs-up-div ${isReviewThumbsUp(movieId) && "extra-styling"}`} onClick={() => deleteReview()}>
                {!isReviewThumbsUp(movieId) && <img src={dtu} className="thumbs-down"></img>}
                {isReviewThumbsUp(movieId) && <img src={dtu2} className="thumbs-down"></img>}
            </div>
        </div>
    )
}
