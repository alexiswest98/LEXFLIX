import React from 'react';
import { NavLink } from 'react-router-dom';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from './auth/LogoutButton';
import lexflixLogo from '../images/lexflixLogo.png';
import './NavBar.css'

const NavBar = () => {
  const sessionUser = useSelector(state => state.session.user);
  const path = window.location.pathname;

  return (
    <div className='outer-nav-bar'>
      <Link to='/' exact={true} className='outer-logo'>
        <img src={lexflixLogo} alt='logo' className='logo' />
      </Link>
      {
        !sessionUser && path !== '/login' &&
        <div className='action-outer-div'>
          <button className='language-button'>
            <i class="fa-solid fa-globe"></i>
            English
          </button>
          <button className='sign-in-button'>
            <Link to='/login' exact={true} className='sign-in'>
              Sign In
            </Link>
          </button>
        </div>
      }
      {
        sessionUser && path !== '/profiles' && path !== '/profiles/manage' &&
        <div className='action-outer-div'>
          <LogoutButton />
        </div>
      }
    </div>
  );
}

export default NavBar;
