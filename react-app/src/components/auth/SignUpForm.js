import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import "./auth.css";

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [plan, setPlan] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(username, email, password, plan));
      if (data) {
        setErrors(data)
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/profiles' />;
  }

  return (
    <form onSubmit={onSignUp} className='outer-whole-signup-form'>
      <h1>Let's Get You Started</h1>
      <div>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div className='whole-input-div'>
        <label>User Name</label>
        <input
          type='text'
          name='username'
          onChange={updateUsername}
          value={username}
        ></input>
      </div>
      <div className='whole-input-div'>
        <label>Email</label>
        <input
          type='text'
          name='email'
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div className='whole-input-div'>
        <label>Password</label>
        <input
          type='password'
          name='password'
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <div className='whole-input-div'>
        <label>Repeat Password</label>
        <input
          type='password'
          name='repeat_password'
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required="true"
        ></input>
      </div>
      <div className='whole-input-div'>
        <h3 className='sel-pay-title'>Select a Payment Plan</h3>
        <input
        type='radio'
        id="basic-with-ads"
        name='plan'
        value={plan}
        onClick={() => setPlan('Basic with ads')}>
        </input>
        <label htmlFor="basic-with-ads">Basic with ads</label>
        <input
        type='radio'
        id="standard"
        name='plan'
        value={plan}
        onClick={() => setPlan('Standard')}>
        </input>
        <label htmlFor="standard">Standard</label>
        <input
        type='radio'
        id="premium"
        name='plan'
        value={plan}
        onClick={() => setPlan('Premium')}>
        </input>
        <label htmlFor="premium">Premium</label>
      </div>
      <button type='submit' className='sign-up-submit'>Sign Up</button>
    </form>
  );
};

export default SignUpForm;

// type='radio'
// name='Basic with ads'
// onChange={updatePlan}
// value={plan}
// checked
