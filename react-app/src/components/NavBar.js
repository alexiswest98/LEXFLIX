import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import LogoutButton from './auth/LogoutButton';
import lexflixLogo from '../images/lexflixLogo.png';
import { getAllProfilesThunk } from '../store/profiles';
import './NavBar.css'

const NavBar = () => {
  const { profId } = useParams()
  const sessionUser = useSelector(state => state.session.user);
  const profile = useSelector(state => state.profiles[+profId]);
  const path = window.location.pathname;
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllProfilesThunk())
  }, [dispatch, path])

  return (<>
    {
      !sessionUser && path !== '/login' &&
      <div className='outer-nav-bar'>
        <div className='inner-nav-prof'>
          <Link to='/' exact={true} className='outer-logo'>
            <img src={lexflixLogo} alt='logo' className='logo' />
          </Link>
        </div>
        <div className='action-outer-div'>
          <button className='language-button'>
            <i class="fa-solid fa-globe"></i>
            English
          </button>
          <button className='sign-in-button'>
            <Link to='/login' exact='true' className='sign-in'>
              Sign In
            </Link>
          </button>
        </div>
      </div>
    }
    {
      sessionUser &&
      <div className='outer-nav-bar'>
        <div className='inner-nav-prof'>
          <Link to='/' exact={true} className='outer-logo'>
            <img src={lexflixLogo} alt='logo' className='logo' />
          </Link>
          <Link to='/' exact={true} className='nav-home-link'>
            <span>Home</span>
          </Link>
          <Link to={`/browse/TV`} exact='true' className='nav-home-link'>
            <span>TV Shows</span>
          </Link>
          <Link to={`/browse/movies`} exact='true' className='nav-home-link'>
            <span>Movies</span>
          </Link>
          <Link to={`/browse/my-list`} exact='true' className='nav-home-link'>
            <span>My List</span>
          </Link>
        </div>
        <div className='action-outer-div-prof'>
          <div className='inner-div-prof-nav'>
            <img src={profile?.profile_img} alt='profile image' className='nav-bar-prof'></img>
            <i class="fa-solid fa-caret-down"></i>
          </div>
          <LogoutButton />
        </div>
      </div>
    }
  </>
  );
}

export default NavBar;

// style for nav bar when on manage profiles or edit 
// background-image: linear-gradient(180deg,rgba(0,0,0,.7) 10%,transparent);
