//FULL CRUD

/* ----- TYPES ------ */
const GETALLPROFILES = 'profiles/getAllProfiles'
const CREATEPROFILE = 'profiles/createProfile'
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
        type: CREATEPROFILE,
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
        dispatch(createProfileAction(newprofile))
        return newprofile
    }
}

export const editProfileThunk = (profile) => async dispatch => {
    const response = await fetch(`/api/profiles/${profile.id}/edit`, {
        method: 'PUT',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(profile)
    })

    if (response.ok) {
        const newprofile = await response.json()
        dispatch(editProfileAction(newprofile))
        return newprofile
    }
}

export const deleteProfileThunk = (profileId) => async (dispatch) => {
    const response = await fetch(`/api/profiles/${profileId}/delete`, { method: 'DELETE' });

    if (response.ok) {
        const deletedProf = await response.json()
      dispatch(deleteProfileAction(profileId))
      return deletedProf
    }
  }

/* ------ REDUCER ------ */
const profileReducer = (state = {}, action) => {
    let newState = {};
    switch (action.type) {
        case GETALLPROFILES:
            // newState = { ...state }
            // console.log('************', action.profiles)
            action.profiles.forEach(prof => {
                newState[prof.id] = prof
            });
            return newState;
        case CREATEPROFILE:
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
