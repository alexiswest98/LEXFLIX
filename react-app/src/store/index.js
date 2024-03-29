import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import movieReducer from './movies';
import profileReducer from './profiles';
import reviewsReducer from './reviews';
import moviesGenresReducer from './genresmovies';
import myListReducer from './mylist';
import tvshowReducer from './tvshows';
import tvReviewReducer from './tvreviews';
import tvShowEpisodesReducer from './tvepisodes';

const rootReducer = combineReducers({
  session,
  movies: movieReducer,
  profiles: profileReducer,
  reviews: reviewsReducer,
  movieGenres: moviesGenresReducer,
  myList: myListReducer,
  tvShow: tvshowReducer,
  tvReview: tvReviewReducer,
  tvShowEpisodes: tvShowEpisodesReducer
});

let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
