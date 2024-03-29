import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import GetProfiles from './components/Profiles';
import ManageProfiles from './components/ManageProfiles';
import EditProfile from './components/EditProfile';
import AddProfile from './components/addProfile';
import HomePage from './components/HomePage/HomePage';
// import HomePageCarousel from './components/HomePageCarousels/HomePageCarousels';
import SplashPage from './components/MainSplashPage/SplashPage';
import TrailerPage from './components/TrailerPage/TrailerPage';
import MovieHomePage from './components/MovieHomePage/MovieHomePage';
import ComingSoon from './components/ComingSoon';
import MyList from './components/myList/MyList';
import TVTrailerPage from './components/TrailerPage/TvShowTrailerPage';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      {/* <NavBar /> */}
      <Switch>
        <Route path='/login' exact='true'>
          <NavBar />
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact='true'>
          <NavBar />
          <SignUpForm />
        </Route>
        <ProtectedRoute path='/users' exact='true' >
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute path='/profiles' exact='true' >
          <GetProfiles />
        </ProtectedRoute>
        <ProtectedRoute path='/manageProfiles/:id' exact='true' >
          <EditProfile />
        </ProtectedRoute>
        <ProtectedRoute path='/profiles/manage' exact='true' >
          <ManageProfiles />
        </ProtectedRoute>
        <ProtectedRoute path='/profiles/create' exact='true' >
          <AddProfile />
        </ProtectedRoute>
        <ProtectedRoute path='/browse/:profId/TV' exact='true' >
          <NavBar />
          <ComingSoon/>
        </ProtectedRoute>
        <ProtectedRoute path='/browse/:profId/my-list' exact='true' >
          <NavBar />
          <MyList/>
        </ProtectedRoute>
        <ProtectedRoute path='/browse/:profId/movies' exact='true' >
          <NavBar />
          <MovieHomePage/>
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact='true' >
          <NavBar />
          <User />
        </ProtectedRoute>
        <ProtectedRoute path='/browse/:profId' exact='true' >
          <NavBar />
          <HomePage />
        </ProtectedRoute>
        <ProtectedRoute path='/:profId/watch/:movieId' exact='true' >
          {/* <NavBar /> */}
          <TrailerPage/>
        </ProtectedRoute>
        <ProtectedRoute path='/:profId/watchTV/:tvId' exact='true'>
          <TVTrailerPage/>
        </ProtectedRoute>
        <Route path='/' exact='true' >
          <NavBar />
          <SplashPage/>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
