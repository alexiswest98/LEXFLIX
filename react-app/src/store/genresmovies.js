const GETMOVIESGENRES = 'movies/getGenreMovies'

/* ___________ Action Creators   ___________ */
export const getMoviesGenresAction = (movies) => {
    return {
        type: GETMOVIESGENRES,
        movies
    }
}

/* ___________ T H U N K S   ___________ */
export const getMoviesGenresThunk = (movie_id) => async (dispatch) => {
    const response = await fetch(`/api/genre/movie/${movie_id}`)
    if (response.ok) {
        const genres = await response.json()
        dispatch(getMoviesGenresAction(genres))
        return genres;
    }
}

/* ___________ Tasks Reducer   ___________ */
export default function moviesGenresReducer(state={}, action) {
    let newState = {};
    switch(action.type){
        case GETMOVIESGENRES:
            newState = {...state}
            action.genres.forEach(genre => newState[genre.id] = genre)
            return newState;
        default:
             return state
    }
}
