import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import './LoginForm.css'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
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
    <form onSubmit={onLogin} className='outer-log-in'>
      <h1>Sign In</h1>
      <div>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div className='whole-input-div'>
        <label htmlFor='email'> Email </label>
        <input
          name='email'
          type='text'
          placeholder='Email'
          value={email}
          onChange={updateEmail}
        />
      </div>
      <div className='whole-input-div'>
        <label htmlFor='password'> Password </label>
        <input
          name='password'
          type='password'
          placeholder='Password'
          value={password}
          onChange={updatePassword}
        />
        <button type='submit'>Login</button>
        <div className='outer-demo'>
          <button
            type='submit'
            onClick={() => { dispatch(login('demo@aa.io', 'password')) }}
          >Login as Demo User</button>
        </div>
        <div className='outer-demo'> 
          <h2 className='new-sign-up-title'>New To Netflix?</h2>
          <NavLink to='/sign-up' exact="true" className='sign-up-link'>
            <span className='sign-up-link'>Sign Up</span>
          </NavLink>
        </div>
      </div>
    </form>
  );
};

export default LoginForm;
