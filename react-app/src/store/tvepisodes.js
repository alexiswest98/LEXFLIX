const GETTVSHOWEPISODES = 'tvepisodes/getTvShowEpisodes';

/* ___________ Action Creators   ___________ */
export const getTvShowEpisodesAction = (episodes) => {
    return {
        type: GETTVSHOWEPISODES,
        episodes
    }
}

/* ___________ T H U N K S   ___________ */
export const getTvShowEpisodesThunk = (tvshow_id) => async (dispatch) => {
    const response = await fetch(`/api/tvep/tv/${tvshow_id}/all`);

    if(response.ok){
        const episodes = await response.json()
        dispatch(getTvShowEpisodesAction(episodes))
        return episodes
    }
}

/* ___________ Tasks Reducer   ___________ */
export default function tvShowEpisodesReducer(state={}, action) {
    let newState={};

    switch(action.type){
        case GETTVSHOWEPISODES:
            action.episodes.forEach(ep => newState[ep.id] = ep)
            return newState;
        default:
            return state
    }
}
