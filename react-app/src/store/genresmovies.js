const GETGENREMOVIES = 'movies/getGenreMovies'

/* ___________ Action Creators   ___________ */
export const getGenreMoviesAction = (movies) => {
    return {
        type: GETGENREMOVIES,
        movies
    }
}

/* ___________ T H U N K S   ___________ */
export const getGenreMoviesThunk = (genre_id) => async (dispatch) => {
    const response = await fetch(`/api/movies/${genre_id}/all`)
}

/* ___________ Tasks Reducer   ___________ */
