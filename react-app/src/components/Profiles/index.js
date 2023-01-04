import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllProfilesThunk } from "../../store/profiles";
import './profiles.css'

export default function GetProfiles() {
    const dispatch = useDispatch();
    const profiles = Object.values(useSelector(state => state.profiles))

    useEffect(() => {
        dispatch(getAllProfilesThunk())
    }, [dispatch])

    if (!profiles ) return null;

    return (
        <div className="outer-prof-div">
            <h1 className="select-prof-text">Who's Watching?</h1>
            <div className="profiles-box">
            {!profiles.includes(404) && profiles.map(prof => (
                <NavLink to={`/browse/${prof.id}`} className="outer-indiv-profile">
                    <div className="outer-prof-img">
                    <img src={prof.profile_img} alt='profile image' className="profile-img"></img>
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
            <NavLink to='/profiles/manage' className="manage-prof-button">Manage Profiles</NavLink>
        </div>
    )
}
