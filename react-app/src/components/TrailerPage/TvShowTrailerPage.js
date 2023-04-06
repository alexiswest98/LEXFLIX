import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link } from 'react-router-dom';
import { getAllTvShowsThunk } from '../../store/movies';
import "./trailerPage.css"

export default function TVTrailerPage() {
    const dispatch = useDispatch();
    const { profId, tvId } = useParams();
    const tvShow = useSelector(state => state.tvShow[+tvId])
    // console.log(profId)

    useEffect(() => {
        dispatch(getAllTvShowsThunk())
    }, [dispatch])

    if (!tvShow) return null;

    return (
        <div className='outer-trailer-page'>
            <Link to={`/browse/${profId}/TV`} className="return-button-div">
            <svg width="55" height="55" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="return-arrow"><path fill-rule="evenodd" clip-rule="evenodd" d="M24 11.0001L3.41421 11.0001L8.70711 5.70718L7.29289 4.29297L0.292892 11.293C0.105356 11.4805 0 11.7349 0 12.0001C0 12.2653 0.105356 12.5196 0.292892 12.7072L7.29289 19.7072L8.70711 18.293L3.41421 13.0001H24V11.0001Z" fill="currentColor"></path></svg>
            </Link>
            <div className='trailer-video-div'>
            <iframe src={tvShow.trailer_src} allowFullScreen webkitAllowFullScreen title="YouTube video player" frameborder="0" className='trailer-frame'></iframe>
            </div>  
        </div>
    )
}
