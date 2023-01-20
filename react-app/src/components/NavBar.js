import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { NavLink } from 'react-router-dom';
import { useHistory } from 'react-router-dom';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import LogoutButton from './auth/LogoutButton';
import lexflixLogo from '../images/lexflixLogo.png';
import { getAllProfilesThunk } from '../store/profiles';
// import { logout } from '../store/session';
import './NavBar.css'

const NavBar = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { profId } = useParams();
  const sessionUser = useSelector(state => state.session.user);
  const userProfiles = Object.values(useSelector(state => state.profiles))
  const profile = useSelector(state => state.profiles[+profId]);
  const path = window.location.pathname;
  const [show, handleShow] = useState(false);
  const [showMenu, setShowMenu] = useState(false);

  //helper function for nav bar 
  const transitionNavBar = () => {
    if (window.scrollY > 100) {
      handleShow(true)
    } else handleShow(false)
  }

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = () => {
      setShowMenu(false);
    };
    //event listener for drop down menu
    document.addEventListener('click', closeMenu);
    //clean up
    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu])

  function setTimedLocalStorage(key, value, minutes) {
    var expiration = new Date().getTime() + minutes * 60 * 1000;
    localStorage.setItem(key, JSON.stringify({ value: value, expiration: expiration }));
  }

  useEffect(() => {

    if(sessionUser){
      dispatch(getAllProfilesThunk())
    }

    //event listener for nav bar background transition
    window.addEventListener("scroll", transitionNavBar)

    //trying local storage again 
    window.addEventListener("beforeunload", function (e) {
      if(profId){
          setTimedLocalStorage('currProfileId', `${profId}`, 60)
      }
    });

    //clean up
    return () => window.removeEventListener("scroll", transitionNavBar)

  }, [dispatch, path, profId])

  return (<div className='whole-outer-nav-full'>
    {
      !sessionUser && path == '/login' && 
      <div className='outer-nav-bar' id='darker-background-nav'>
      <div className='inner-nav-prof'>
        <Link to='/' exact='true' className='outer-logo'>
          <img src={lexflixLogo} alt='logo' className='logo' />
        </Link>
      </div>
      <div className='action-outer-div'>
      </div>
    </div>
    }
    {
      !sessionUser && path !== '/login' &&
      <div className='outer-nav-bar' id='darker-background-nav'>
        <div className='inner-nav-prof'>
          <Link to='/' exact='true' className='outer-logo'>
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
      <div className={`outer-nav-bar ${show && 'fixed'}`}>
        <div className='inner-nav-prof'>
          <Link to={`/browse/${profId}`} exact="true" className='outer-logo'>
            <img src={lexflixLogo} alt='logo' className='logo' />
          </Link>
          <Link to={`/browse/${profId}`} exact="true" className='nav-home-link'>
            <span>Home</span>
          </Link>
          <Link to={`/browse/${profId}/TV`} exact='true' className='nav-home-link'>
            <span>TV Shows</span>
          </Link>
          <Link to={`/browse/${profId}/movies`} exact='true' className='nav-home-link'>
            <span>Movies</span>
          </Link>
          <Link to={`/browse/${profId}/my-list`} exact='true' className='nav-home-link'>
            <span>My List</span>
          </Link>
        </div>
        <div className='action-outer-div-prof'>
          <div className={`inner-div-prof-nav ${showMenu && 'carrot-transform'}`} onClick={openMenu}>
            <img src={profile?.profile_img} alt='profile image' className='nav-bar-prof'></img>
            <i class="fa-solid fa-caret-down"></i>
          </div>
          {showMenu && (
            <div className='whole-outer-drop-down'>
              <div className='up-arrow-drop-down-div'>
                <i class="fa-solid fa-caret-up"></i>
              </div>
              <div className={`drop-down-menu ${userProfiles.length == 3 && "smaller-nav"} ${userProfiles.length < 3 && "smallest-nav"}`}>
                {userProfiles.map(prof => (
                  <Link to={`/browse/${prof.id}`} exact="true" className={`outer-drop-down-div ${userProfiles.length == 3 && "smaller-nav-prof"}  ${userProfiles.length < 3 && "smallest-nav-prof"}`}>
                    <img src={prof.profile_img} alt='profile image' className='drop-down-prof-image'></img>
                    <h4 className='drop-down-menu-text'>{prof.username.length < 20 ? prof.username : prof.username.slice(0, 10) + '..'}</h4>
                  </Link>
                ))}
                <Link to='/profiles/manage' className={`drop-down-manage-prof-div ${userProfiles.length == 3 && "smaller-nav-manage"}  ${userProfiles.length < 3 && "smallest-nav-manage"}`}>
                  <div className='left-side-drop-svg'>
                    <svg width="38" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" id='drop-down-edit' class="svg-icon svg-icon-edit"><path fill-rule="evenodd" clip-rule="evenodd" d="M22.2071 7.79285L15.2071 0.792847L13.7929 2.20706L20.7929 9.20706L22.2071 7.79285ZM13.2071 3.79285C12.8166 3.40232 12.1834 3.40232 11.7929 3.79285L2.29289 13.2928C2.10536 13.4804 2 13.7347 2 14V20C2 20.5522 2.44772 21 3 21H9C9.26522 21 9.51957 20.8946 9.70711 20.7071L19.2071 11.2071C19.5976 10.8165 19.5976 10.1834 19.2071 9.79285L13.2071 3.79285ZM17.0858 10.5L8.58579 19H4V14.4142L12.5 5.91417L17.0858 10.5Z" fill="currentColor"></path></svg>
                  </div>
                  <div className='right-half-drop-manage'>
                    <h4 className="drop-manage-prof-button">Manage Profiles</h4>
                  </div>
                </Link>
                <div className={`log-out-div ${userProfiles.length == 3 && "smaller-nav-logout"} ${userProfiles.length < 3 && "smallest-nav-logout"}`}>
                  <LogoutButton />
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    }
  </div>
  );
}

export default NavBar;

// style for nav bar when on manage profiles or edit 
// background-image: linear-gradient(180deg,rgba(0,0,0,.7) 10%,transparent);
