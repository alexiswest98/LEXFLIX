import React from 'react';
import './splashPage.css'
import splashPageBackground from '../../images/splashPageBackground.jpg'

export default function SplashPage() {

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
                        <span>need to finish :)</span>
                    </div>
                </div>
            </div>
        </div>
    )
}
