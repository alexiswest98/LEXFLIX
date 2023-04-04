//FULL CRUD

/* ----- TYPES ------ */
const GETALLTVREVIEWS = 'reviews/getAllTvReviews'
const GETTVREVIEW = 'review/getTvReview'
const ADDTVREVIEW = "review/addTvReview";
const EDITTVREVIEW = "review/editTvReview";
const DELETETVREVIEW = 'review/deleteTvReview';

/* ----- ACTIONS ------ */
const getAllTvReviewsAction = (reviews) => {
    return {
        type: GETALLTVREVIEWS,
        reviews
    }
};

const getTvReviewAction = (review) => {
    return {
        type: GETTVREVIEW,
        review
    }
};

const addTvReviewAction = (review) => {
    return {
        type: ADDTVREVIEW,
        review
    }
};

const editTvReviewAction = (review) => {
    return {
        type: EDITTVREVIEW,
        review
    }
};

const deleteTvReviewAction = (reviewId) => {
    return {
        type: DELETETVREVIEW,
        reviewId
    }
};

/* ------ THUNKS ------ */
export const getAllTvReviewsThunk = (profileId) => async dispatch => {
    const response = await fetch(`/api/tvreview/profile/${profileId}/all`);

    if(response.ok){
        const tvreviews = await response.json();
        dispatch(getAllTvReviewsAction(tvreviews))
        return tvreviews;
    }
}

export const getTvReviewThunk = (profileId, tvId) => async dispatch => {
    const response = await fetch(`/api/tvreview/${tvId}/profile/${profileId}`);

    if(response.ok){
        const tvreview = await response.json();
        dispatch(getTvReviewAction(tvreview))
        return tvreview;
    }
}

export const addTvReviewThunk = (profileId, tvId, tvreview) => async dispatch => {
    const response = await fetch(`/api/tvreview/${tvId}/profile/${profileId}`, {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(tvreview)
    })

    if(response.ok){
        const newTvReview = await response.json();
        dispatch(addTvReviewAction(newTvReview))
        return newTvReview;
    }
}

export const editTvReviewThunk = (tvId, newtvreview) => async dispatch => {
    const response = await fetch(`/api/tvreview/${tvId}/edit`, {
        method: 'PUT',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(newtvreview)
    })

    if(response.ok){
        const editTvReview = await response.json();
        dispatch(editTvReviewAction(editTvReview))
        return editTvReview
    }
}

export const deleteTvReviewThunk = (reviewId) => async dispatch => {
    const response = await fetch(`/api/tvreview/${reviewId}/delete`, {
        method: 'DELETE'
    });

    if(response.ok){
        const deletedTvReview = await response.json();
        dispatch(deleteTvReviewAction(reviewId))
        return deletedTvReview;
    }
}

/* ------ REDUCER ------ */

const tvReviewReducer = (state = {}, action) => {
    let newState = {};
    switch(action.type){
        case GETALLTVREVIEWS:
            action.reviews.forEach((review) => {
                newState[review.id] = review;
            });
            return newState;
        case GETTVREVIEW:
            newState = { ...state };
            newState[action.review.id] = { ...newState[action.review.id], ...action.review}
            return newState;
        case ADDTVREVIEW:
            newState = { ...state };
            newState[action.review.id] = action.review;
            return newState;
        case EDITTVREVIEW:
            newState = { ...state };
            newState[action.review.id] = { ...newState[action.review.id], ...action.review}
            return newState;
        case DELETETVREVIEW:
            newState = { ...state };
            delete newState[action.reviewId];
            return newState;
        default:
            return state;
    }
}
