const GETMOVIEBYGENRE = 'movies/getMovieByGenre'

/* ___________ Action Creators   ___________ */
export const getMovieByGenreAction = (movies) => {
    return {
        type: GETMOVIEBYGENRE,
        movies
    }
}

/* ___________ T H U N K S   ___________ */
export const getMovieByGenreThunk = (genreId) => async (dispatch) => {
    const response = await fetch(`/api/movies/${genreId}/all`);
    if(response.ok) {
        const movies = await response.json()
        dispatch(getMovieByGenreAction(movies))
        return movies
    }
}

/* ___________ Tasks Reducer   ___________ */
export default function mediaByGenreReducer(state={}, action) {
    let newState = {};

    switch (action.type){
        case GETMOVIEBYGENRE:
            action.movies.forEach(mov => newState[mov.id] = mov)
            return newState
        default:
             return state
    }
}
