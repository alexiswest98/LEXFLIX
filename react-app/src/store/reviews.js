//FULL CRUD

/* ----- TYPES ------ */
const GETALLREVIEWS = 'reviews/getAllReviews'
const GETREVIEW = 'reviews/getReview'
const ADDREVIEW = "review/addReview";
const EDITREVIEW = "review/editReview";
const DELETEREVIEW = 'review/deleteReview';

/* ----- ACTIONS ------ */
const getAllReviewsAction = (reviews) => {
    return {
        type: GETALLREVIEWS,
        reviews
    }
};

const getReviewAction = (review) => {
    return {
        type: GETREVIEW,
        review
    }
};

const addReviewAction = (review) => {
    return {
        type: ADDREVIEW,
        review
    }
};

const editReviewAction = (review) => {
    return {
        type: EDITREVIEW,
        review
    }
};

const deleteReviewAction = (reviewId) => {
    return {
        type: DELETEREVIEW,
        reviewId
    }
};
 

/* ------ THUNKS ------ */
export const getAllReviewsThunk = (profileId) => async dispatch => {
    const response = await fetch(`/api/review/profile/${profileId}/all`);

    if (response.ok) {
        const reviews = await response.json();
        dispatch(getAllReviewsAction(reviews))
        return reviews;
    }
};

export const getReviewThunk = (profileId, movieId) => async dispatch => {
    const response = await fetch(`/api/review/profile/${profileId}/movie/${movieId}`);

    if (response.ok) {
        const review = await response.json();
        dispatch(getReviewAction(review))
        return review;
    }
};

export const addReviewThunk = (profileId, movieId, review) => async dispatch => {
    const response = await fetch(`/api/review/profile/${profileId}/movie/${movieId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(review)
    });

    if (response.ok) {
        const newReview = await response.json();
        await dispatch(addReviewAction(newReview));
        return newReview;
    }
};

export const editReviewThunk = (review) => async dispatch => {
    const response = await fetch(`/api/review/${review.id}/edit`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(review)
    });

    if (response.ok) {
        const newReview = await response.json();
        await dispatch(editReviewAction(newReview));
        return newReview;
    }
};

export const deleteReviewThunk = (reviewId) => async dispatch => {
    const response = await fetch(`/api/review/${reviewId}/delete`, {
        method: 'DELETE'
    });

    if (response.ok) {
        const review = await response.json();
        await dispatch(deleteReviewAction(reviewId));
        return review;
    }
};


/* ------ REDUCER ------ */
const reviewsReducer = (state = {}, action) => {
    let newState = {};
    switch (action.type) {
        case GETALLREVIEWS:
            action.reviews.forEach((review) => {
                newState[review.id] = review;
            });
            return newState;
        case GETREVIEW:
            newState = { ...state };
            newState[action.review.id] = { ...newState[action.review.id], ...action.review}
        case ADDREVIEW:
            newState = { ...state };
            newState[action.review.id] = action.review;
            return newState;
        case EDITREVIEW:
            newState = { ...state };
            newState[action.review.id] = { ...newState[action.review.id], ...action.review}
            return newState;
        case DELETEREVIEW:
            newState = { ...state };
            delete newState[action.reviewId];
            return newState;
        default:
            return state;
    }

}

export default reviewsReducer;
