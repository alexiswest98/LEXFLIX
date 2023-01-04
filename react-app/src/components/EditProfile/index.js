import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useParams } from "react-router-dom";
import { useHistory } from "react-router-dom";
import { editProfileThunk, getAllProfilesThunk, deleteProfileThunk } from "../../store/profiles";
import './editProfile.css'

export default function EditProfile() {
    const dispatch = useDispatch();
    const history = useHistory();
    const { id } = useParams();
    // const profiles = Object.values(useSelector(state => state.profiles))
    const profile = useSelector(state => state.profiles[+id])
    const [username, setUsername] = useState(profile?.username || "")
    const [img, setImg] = useState(profile?.profile_img || "")
    const [validationErrors, setValidationErrors] = useState([]);
    const [hasSubmitted, setHasSubmitted] = useState(false);

    useEffect(() => {
        dispatch(getAllProfilesThunk())
        const errors = [];
        if (!username) errors.push("Username is required");
        if (username.length > 40) errors.push("Username must be less than 40 characters");
        setValidationErrors(errors);
    }, [username, img, dispatch])

    const onSubmit = () => {
        setHasSubmitted(true);

        if (validationErrors.length) return alert(`Can't Save Changes`);

        if (!validationErrors.length){
            const updatedProfile = {
                id: profile.id,
                user_id: profile.user_id,
                username
    
            }
    
            dispatch(editProfileThunk(updatedProfile))
            history.push('/profiles/manage')
        }
    }

    const deleteProfile = () => {
        dispatch(deleteProfileThunk(+id))
        history.push(`/profiles/manage`)
    }

    if (!profile) return null;

    // console.log(profile)

    return (
        <form onSubmit={onSubmit} className="outer-edit-prof">
            <div className="inner-edit-prof">
                <div className="edit-prof-div">
                    <h1 className="edit-prof-text">Edit Profile</h1>
                </div>
                <div className="outer-prof-details">
                    <div className="prof-img-div">
                        <img src={profile.profile_img} alt='profile image' className="edit-prof-img"></img>
                    </div>
                    <div className="inner-prof-dets">
                        {
                            username && username.length <= 40 &&
                            <div className="outer-input-div">
                                <input className="input-username"
                                    type="text"
                                    onChange={(e) => setUsername(e.target.value)}
                                    value={username}
                                    placeholder="Name" />
                            </div>
                        }
                        {
                            !username && 
                            <div className="outer-input-div">
                                <input className="input-username-bad"
                                    type="text"
                                    onChange={(e) => setUsername(e.target.value)}
                                    value={username}
                                    placeholder="Name" />
                                {/* <span className="no-name-red">Please enter a valid name under 40 characters</span> */}
                                {validationErrors.map((error) =>
                                    <span className="no-name-red">{error}</span>
                                )}
                            </div>
                        }
                                                {
                            username.length > 40 && 
                            <div className="outer-input-div">
                                <input className="input-username-bad"
                                    type="text"
                                    onChange={(e) => setUsername(e.target.value)}
                                    value={username}
                                    placeholder="Name" />
                                {/* <span className="no-name-red">Please enter a valid name under 40 characters</span> */}
                                {validationErrors.map((error) =>
                                    <span className="no-name-red">{error}</span>
                                )}
                            </div>
                        }
                        <div className="outer-lang-div">
                            <h2 className="lang-text-title">Language:</h2>
                            <div className='edit-language-button'>
                                <i class="fa-solid fa-globe" id="new-lang"></i>
                                English
                            </div>
                        </div>
                        <div className="outer-lang-div">
                            <h2 className="lang-text-title">Maturity Settings:</h2>
                            <button className="maturity">
                                All Maturity Ratings
                            </button>
                        </div>
                        <div className="outer-lang-div">
                            <h2 className="lang-text-title">Autoplay controls:</h2>
                            <div className="extra-edit-dets">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="svg-icon svg-icon-check-mark"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.68239 19.7312L23.6824 5.73115L22.3178 4.26904L8.02404 17.6098L2.70718 12.293L1.29297 13.7072L7.29297 19.7072C7.67401 20.0882 8.28845 20.0988 8.68239 19.7312Z" fill="currentColor"></path></svg>
                                <span>Autoplay next episode in a series on all devices.</span>
                            </div>
                            <div className="extra-edit-dets">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="svg-icon svg-icon-check-mark"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.68239 19.7312L23.6824 5.73115L22.3178 4.26904L8.02404 17.6098L2.70718 12.293L1.29297 13.7072L7.29297 19.7072C7.67401 20.0882 8.28845 20.0988 8.68239 19.7312Z" fill="currentColor"></path></svg>
                                <span>Autoplay previews while browsing on all devices.</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="edit-prof-controls">
                    <button className="done-manage-button"
                        type="submit"
                        onClick={() => onSubmit()}
                    >Save</button>
                    <button onClick={() => history.push('/profiles/manage')} className="manage-prof-button">Cancel</button>
                    <button
                        onClick={() => deleteProfile()} className="manage-prof-button">Delete Profile</button>
                </div>
            </div>
        </form>
    )
}
