const GETALLTVSHOWS = 'tvshows/getAllTvShows';
const GETONETVSHOW = 'tvshows/getOneTvShow';

/* ___________ Action Creators   ___________ */
export const getAllTvShowsAction = (tvshows) => {
    return {
        type: GETALLTVSHOWS,
        tvshows
    }
}

export const getOneTvShowAction = (tvshow) => {
    return {
        type: GETONETVSHOW,
        tvshow
    }
}

/* ___________ T H U N K S   ___________ */
export const getAllTvShowsThunk = () => async (dispatch) => {
    const response = await fetch('/api/tv/all');

    if(response.ok){
        const tvshows = await response.json()
        dispatch(getAllTvShowsAction(tvshows))
        return tvshows
    }
}

export const getOneTvShowThunk = (tvshow_id) => async (dispatch) => {
    const response = await fetch(`/api/tv/${tvshow_id}`);

    if(response.ok){
        const tvshow = await response.json()
        dispatch(getOneTvShowAction(tvshow))
        return tvshow
    }
}

/* ___________ Tasks Reducer   ___________ */
export default function tvshowReducer(state={}, action) {
    let newState={};

    switch(action.type){
        case GETALLTVSHOWS:
            action.tvshows.forEach(tv => newState[tv.id] = tv)
            return newState;
        case GETONETVSHOW:
            newState = {...state}
            newState[action.tvshow.id] = {... newState[action.tvshow.id], ...action.tvshow}
            return newState;
        default:
            return state
    }
}
