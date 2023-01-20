import React, {useEffect} from 'react';
import { useHistory } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import splashPageBackground from '../../images/splashPageBackground.jpg'
import linkedin from "../../images/linkedin.png"
import github from "../../images/github.png"
import { logout } from '../../store/session';
import './splashPage.css'

export default function SplashPage() {
    const dispatch = useDispatch();
    const history = useHistory();
    //in order to get local storage value(profileIdd)

    function getTimedLocalStorage(key) {
        const data = JSON.parse(localStorage.getItem(key));
        if (data && data.expiration > new Date().getTime()) {
          return data.value;
        } else {
          localStorage.removeItem(key);
          return null;
        }
      }

      console.log(getTimedLocalStorage("currProfileId"))


    useEffect(async () => {
        const myData = getTimedLocalStorage("currProfileId");
        if (myData !== null) {
            history.push(`/browse/${+myData}`)
        } else {
          await dispatch(logout());
        }
    }, [])

    return (
        <div className='whole-outer-splash-page'>
            <div className='whole-outer-splash-body'
                style={{
                    backgroundSize: "cover",
                    backgroundImage: `url("${splashPageBackground}")`,
                    backgroundPosition: 'center center'
                }}>
                <div className='splash-page-title'>
                    <div className='splash-page-title-text'>
                        <h1>Unlimited movies, TV shows, and more.</h1>
                        <span>Watch anywhere. Cancel anytime.</span>
                    </div>
                </div>
            </div>
            <div className='lex-details'>
                <h1 className='footer-lex-text'>Created and Styled by Alexis West · </h1>
                <a target="_blank" href='https://www.linkedin.com/in/alexis-west-596a6b203/' className='footer-link-div'>
                    <img id="linkedin" src={linkedin} alt="li"></img>
                </a>
                <a target="_blank" href='https://github.com/alexiswest98' className='footer-link-div'>
                    <img id="github-icon" src={github} alt="gh"></img>
                </a>
            </div>
        </div>
    )
}
