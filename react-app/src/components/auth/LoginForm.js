import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import splashPageBackground from '../../images/splashPageBackground.jpg'
import './LoginForm.css'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const [hasSubmitted, setHasSubmitted] = useState(false);

  const onLogin = async (e) => {
    e.preventDefault();
    setHasSubmitted(true)
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/profiles' />;
  }

  return (
    <div className='whole-outer-login-div' style={{
      backgroundSize: "cover",
      backgroundImage: `url("${splashPageBackground}")`,
      backgroundPosition: 'center center'
  }}>
    <div className='outer-tint'>
    <form onSubmit={onLogin} className='outer-log-in'>
      <div className='title-sign-in-div'>
        <h1 className='sign-in-text'>Sign In</h1>
      </div>
      <div className='whole-input-div'>
        <input
          name='email'
          type='text'
          placeholder=' Email'
          value={email}
          onChange={updateEmail}
          className="input-field"
        />
      </div>
      <div className='whole-input-div'>
        <input
          name='password'
          type='password'
          placeholder=' Password'
          value={password}
          onChange={updatePassword}
          className="input-field"
        />
        </div>
        <button type='submit' className='submit-login'>Login</button>
        <button
          className='submit-login'
          type='submit'
          onClick={() => { dispatch(login('demo@aa.io', 'password'))}}
          >Login as Demo User
        </button>
        <div className='outer-demo'> 
          <h2 className='new-sign-up-title'>New To Letflix?</h2>
          <NavLink to='/sign-up' exact="true" className='sign-up-link'>
            <span>Sign up now.</span>
          </NavLink>
        </div>
      <div className='sign-in-errors'>
        {hasSubmitted && errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
    </form>
    </div>
    </div>
  );
};

export default LoginForm;
