import React from 'react';
import { Link } from 'react-router-dom';
import splashPageBackground from '../../images/splashPageBackground.jpg'
import linkedin from "../../images/linkedin.png"
import github from "../../images/github.png"
import './splashPage.css'

export default function SplashPage() {

    //check
    //if user {
    //     dispatch logout to happen every time on render
    // }
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
