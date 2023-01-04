import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useParams } from "react-router-dom";
import { useHistory } from "react-router-dom";
import { createProfileThunk, getAllProfilesThunk } from "../../store/profiles";
import "./addProfile.css"

export default function AddProfile() {
    const dispatch = useDispatch();
    const history = useHistory();
    const [username, setUsername] = useState("")
    const [validationErrors, setValidationErrors] = useState([]);
    const sessionUser = useSelector(state => state.session.user);
    const [hasSubmitted, setHasSubmitted] = useState(false);

    useEffect(() => {
        const errors = [];
        if (!username) errors.push("Please enter a name");
        if (username.length > 40) errors.push("Username must be less than 40 characters");
        setValidationErrors(errors);
    }, [username])

    const onSubmit = async (e) => {
        e.preventDefault();
        setHasSubmitted(true);
        if (validationErrors.length) return alert(`Can't Add Profile`);

        const newProfile = {
            user_id: sessionUser.id,
            username
        }

        await dispatch(createProfileThunk(newProfile))
        // await dispatch(getAllProfilesThunk())
        history.push("/profiles/manage")
    }


    return (
        <form onSubmit={onSubmit} className="outer-whole-add-profile">
            <div className="inner-whole-add-prof">
                <h1 className="add-prof-title">Add Profile</h1>
                <h2 className="add-dets-span">Add a profile for another person watching Netflix.</h2>
                <div className="outer-add-prof">
                    <img src="https://occ-0-1339-1340.1.nflxso.net/dnm/api/v6/K6hjPJd6cR6FpVELC5Pd6ovHRSk/AAAABUoj4FT-0Rr558WbETiintMnmH2JKw4l_p4MdMoxqVx7YXwsvLvvnGUtx3HKZN_BJFH4EHpXn5KqSCBVxLrRz0n4gk64yyeAFw.png?r=229" alt="profile image" className="prof-add-img"></img>
                    {
                        !hasSubmitted &&
                        <div className="outer-input-div-add">
                            <input className="input-username-add"
                                type="text"
                                onChange={(e) => setUsername(e.target.value)}
                                value={username}
                                placeholder="Name" />
                        </div>
                    }{
                        hasSubmitted && validationErrors &&
                        <div className="outer-input-div-add">
                            <input className="input-username-add-bad"
                                type="text"
                                onChange={(e) => setUsername(e.target.value)}
                                value={username}
                                placeholder="Name" />
                            {validationErrors.map((error) => 
                            <span className="no-name-red">{error}</span>
                            )}
                        </div>
                    }
                </div>
                <div className="edit-prof-controls" id="add-prof">
                    <button className="done-manage-button"
                        type="submit"
                    // onClick={() => onSubmit()}
                    >Continue</button>
                    <button onClick={() => history.push('/profiles/manage')} className="manage-prof-button">Cancel</button>
                </div>
            </div>
        </form>
    )
}
