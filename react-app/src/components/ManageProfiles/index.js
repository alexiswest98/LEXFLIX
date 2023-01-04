import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Link } from "react-router-dom";
import { getAllProfilesThunk } from "../../store/profiles";
import './manageProfiles.css'

export default function ManageProfiles() {
    const dispatch = useDispatch();
    const profiles = Object.values(useSelector(state => state.profiles))

    useEffect(() => {
        dispatch(getAllProfilesThunk())
    }, [dispatch])

    if (!profiles ) return null;

    return (
        <div className="outer-prof-div">
            <h1 className="select-prof-text">Manage Profiles:</h1>
            <div className="profiles-box">
                {!profiles.includes(404) && profiles.map(prof => (
                    <NavLink to={`/ManageProfiles/${prof.id}`} className="outer-indiv-manage-profile">
                        <div className="outer-prof-img">
                            <img src={prof.profile_img} alt='profile image' className="profile-img" />
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="svg-icon svg-icon-edit"><path fill-rule="evenodd" clip-rule="evenodd" d="M22.2071 7.79285L15.2071 0.792847L13.7929 2.20706L20.7929 9.20706L22.2071 7.79285ZM13.2071 3.79285C12.8166 3.40232 12.1834 3.40232 11.7929 3.79285L2.29289 13.2928C2.10536 13.4804 2 13.7347 2 14V20C2 20.5522 2.44772 21 3 21H9C9.26522 21 9.51957 20.8946 9.70711 20.7071L19.2071 11.2071C19.5976 10.8165 19.5976 10.1834 19.2071 9.79285L13.2071 3.79285ZM17.0858 10.5L8.58579 19H4V14.4142L12.5 5.91417L17.0858 10.5Z" fill="currentColor"></path></svg>
                        </div>
                        <h4 className="profile-username">{prof.username}</h4>
                    </NavLink>
                ))}
                {
                    profiles.length < 5 && (
                        <NavLink to={`/profiles/create`} className="outer-indiv-profile">
                            <div className="outer-prof-img">
                                <div className="add-prof-div">
                                    <i class="fa-sharp fa-solid fa-circle-plus"></i>
                                </div>
                            </div>
                            <h4 className="profile-username">Add Profile</h4>
                        </NavLink>
                    )
                }
            </div>
            <NavLink to='/profiles' className="done-manage-button">Done</NavLink>
        </div>
    )
}
