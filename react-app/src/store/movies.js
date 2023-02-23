const GETALLMOVIES = 'movies/getAllMovies'
const GETONEMOVIE = 'movies/getOneMovie'

/* ___________ Action Creators   ___________ */
export const getAllMoviesAction = (movies) => {
    return {
        type: GETALLMOVIES,
        movies
    }
}

export const getOneMovieAction = (movie) => {
    return {
        type: GETONEMOVIE,
        movie
    }
}


/* ___________ T H U N K S   ___________ */
export const getAllMoviesThunk = () => async (dispatch) => {
    const response = await fetch('/api/movies/all');
    if (response.ok) {
        const movies = await response.json()
        dispatch(getAllMoviesAction(movies))
        return movies
    }
}

export const getOneMovieThunk = (movie_id) => async (dispatch) => {
    const response = await fetch(`/api/movies/${movie_id}`);
    if (response.ok) {
        const movie = await response.json()
        dispatch(getOneMovieAction(movie))
        return movie
    }
}


/* ___________ Tasks Reducer   ___________ */
export default function movieReducer(state={}, action) {
    let newState = {};

    switch (action.type){
        case GETALLMOVIES:
            action.movies.forEach(mov => newState[mov.id] = mov)
            return newState;
        case GETONEMOVIE:
            newState = {...state}
            newState[action.movie.id] = {... newState[action.movie.id], ...action.movie.id}
            return newState;
        default:
             return state
    }
}
