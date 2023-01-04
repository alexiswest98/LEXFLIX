import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getAllMoviesThunk } from '../../store/movies';
import './homePage.css'

export default function HomePage() {
    const dispatch = useDispatch();
    const movies = Object.values(useSelector(state => state.movies))

    useEffect(() => {
        dispatch(getAllMoviesThunk())
      }, [dispatch])

    return (
        <div>
            <h1>Movies</h1>
            {movies.map(mov => (
                <div>
                    <h2>{mov.movie_name}</h2>
                    <img src={mov.prev_img} alt='movie poster' className='movie-poster'></img>
                </div>
            ))}
        </div>
    )

}
