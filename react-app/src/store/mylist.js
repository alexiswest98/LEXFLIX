/* ----- TYPES ------ */
const GETMYLIST = 'mylist/getmylist'
const ADDMOVIEMYLIST = 'mylist/addmylist'
const DELETEMYLIST = 'mylist/deletemylist'

/* ----- ACTIONS ------ */
const getAllMyListAction = (media) => {
    return {
        type: GETMYLIST,
        media
    }
};

const addMovieMyListAction = (movie) => {
    return {
        type: ADDMOVIEMYLIST,
        movie
    }
};

//need separate add show action

const deleteAllMyListAction = (mediaId) => {
    return {
        type: DELETEMYLIST,
        mediaId
    }
};

/* ------ THUNKS ------ */

export const getAllMyListThunk = (profileId) => async dispatch => {
    const response = await fetch(`/api/mylist/profile/${profileId}/all`)

    if (response.ok) {
        const media = await response.json()
        dispatch(getAllMyListAction(media))
        return media;
    }
}

export const addMovieMyListThunk = (profileId, movieId ) => async dispatch => {
    const response = await fetch(`/api/mylist/profile/${profileId}/movie/${movieId}`, {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({
            movie_id: movieId,
            profile_id: profileId
        })
    })

    if (response.ok) {
        const movie = await response.json()
        dispatch(addMovieMyListAction(movie))
        return movie
    }
}

export const deleteMyListThunk = (mediaId) => async dispatch => {
    const response = await fetch(`/api/mylist/${mediaId}/delete`, { method: 'DELETE' })

    if (response.ok) {
        const media = await response.json()
        dispatch(deleteAllMyListAction(media))
        return media
    }
}

/* ------ REDUCER ------ */
const myListReducer = (state = {}, action) => {
    let newState = {};
    switch(action.type) {
        case GETMYLIST:
            action.media.forEach((med) => {
                newState[med.id] = med
            });
            return newState;
        case ADDMOVIEMYLIST:
            newState = {...state}
            newState[action.movie.id] = action.movie
            return newState;
        case DELETEMYLIST:
            newState = {...state}
            delete newState[action.movieId]
            return newState;
        default:
            return state;
    }
}

export default myListReducer;
