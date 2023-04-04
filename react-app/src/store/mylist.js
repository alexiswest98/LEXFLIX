/* ----- TYPES ------ */
const GETMYLIST = 'mylist/getmylist'
const ADDMOVIEMYLIST = 'mylist/addmylist'
const ADDTVMYLIST = 'mylist/addtvmylist'
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

//need separate add tv show action
const addTvMyListAction = (tv) => {
    return {
        type: ADDTVMYLIST,
        tv
    }
};

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

//tv show just added
export const addTVMyListThunk = (profileId, tvId) => async dispatch => {
    const response = await fetch(`/api/mylist/profile/${profileId}/tvshow/${tvId}`, {
        method: 'POST',
        headers: {'COntent-Type':'application/json'},
        body: JSON.stringify({
            tv_id: tvId,
            profile_id: profileId
        })
    })

    if(response.ok){
        const tv =await response.json()
        dispatch(addTvMyListAction(tv))
        return tv
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
        //may have to come back to bc movie id and tv id may be the same
        case ADDTVMYLIST:
            newState = {...state}
            newState[action.tv.id] = action.tv
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
