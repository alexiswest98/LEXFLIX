//FULL CRUD

/* ----- TYPES ------ */
const GETALLPROFILES = 'profiles/getAllProfiles'
const CREATEPROFLE = 'profiles/createProfile'
const EDITPROFILE = 'profiles/editProfile'
const DELETEPROFILE = 'profiles/deleteProfile'

/* ----- ACTIONS ------ */
export const getAllProfilesAction = (profiles) => {
    return {
        type: GETALLPROFILES,
        profiles
    }
}

export const createProfileAction = (profile) => {
    return {
        type: CREATEPROFLE,
        profile
    }
}

export const editProfileAction = (profile) => {
    return {
        type: EDITPROFILE,
        profile
    }
}

export const deleteProfileAction = (profileId) => {
    return {
        type: DELETEPROFILE,
        profileId
    }
}

/* ------ THUNKS ------ */

export const getAllProfilesThunk = () => async dispatch => {
    const response = await fetch(`/api/profiles/all`)

    if (response.ok) {
        const profiles = await response.json()
        dispatch(getAllProfilesAction(profiles))
        return profiles
    }
}

export const createProfileThunk = (profile) => async dispatch => {
    const response = await fetch(`/api/profiles/create`, {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(profile)
    })

    if (response.ok) {
        const newprofile = await response.json()
        dispatch(getAllProfilesAction(newprofile))
        return newprofile
    }
}

export const editProfileThunk = (profile) => async dispatch => {
    const response = await fetch(`/api/profiles/all`, {
        method: 'PUT',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(profile)
    })

    if (response.ok) {
        const newprofile = await response.json()
        dispatch(getAllProfilesAction(newprofile))
        return newprofile
    }
}

export const deleteProfileThunk = (profileId) => async (dispatch) => {
    const res = await fetch(`/api/profiles/${profileId}/delete`, { method: 'DELETE' });
    if (res.ok) {
      dispatch(deleteProfileAction(profileId))
    }
  }

/* ------ REDUCER ------ */
const profileReducer = (state = {}, action) => {
    let newState = {};
    switch (action.type) {
        case GETALLPROFILES:
            newState = { ...state }
            action.profiles.forEach(prof => {
                newState[prof.id] = prof
            });
            return newState;
        case CREATEPROFLE:
            newState = { ...state }
            newState[action.profile.id] = action.profile
            return newState;
        case EDITPROFILE:
            newState={...state}
            newState[action.profile.id] = { ...newState[action.profile.id], ...action.profile };
            return newState;
        case DELETEPROFILE:
            newState = { ...state }
            delete newState[action.profileId];
            return newState;
        default:
            return state;
    }
}

export default profileReducer;
