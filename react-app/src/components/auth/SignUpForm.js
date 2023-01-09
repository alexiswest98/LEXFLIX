import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { useEffect } from 'react';
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import splashPageBackground from '../../images/splashPageBackground.jpg'
import "./auth.css";

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [plan, setPlan] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  useEffect(() => {
    let errs = []
    if (!username) errs.push('Please provide username')
    if (!email || !email.includes('@')) errs.push('Please provide a valid email')
    if (password !== repeatPassword) errs.push('Passwords do not match.')
    if (password.length > 255) errs.push('Password must be less than 255 characters.')
    if (email.length > 255) errs.push('Email must be less than 255 characters.')
    if (username.length > 40) errs.push('Username must be less than 40 characters.')
    if (username === email) errs.push('Username and email cannot be the same')
    if (!plan) errs.push('Please select a payment plan')
    setErrors(errs)
  }, [username, email, password, repeatPassword, plan]);

  const onSignUp = async (e) => {
    e.preventDefault();
    setHasSubmitted(true);

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
    <div className='whole-outer-sign-up'>
      <div className='header-sign-up-div'>
        <h1>Let's Get You Started</h1>
      </div>
      <form onSubmit={onSignUp} className='outer-whole-signup-form'>
        <div className='right-half-outer-sign-up'>
          <h2 className='sel-pay-title'>User Information</h2>
          <div className='sign-up-whole-input-div'>
            <label>User Name</label>
            <input
              type='text'
              name='username'
              onChange={updateUsername}
              value={username}
              className="sign-up-input-field"
            ></input>
          </div>
          <div className='sign-up-whole-input-div'>
            <label>Email</label>
            <input
              type='text'
              name='email'
              onChange={updateEmail}
              value={email}
              className="sign-up-input-field"
            ></input>
          </div>
          <div className='sign-up-whole-input-div'>
            <label>Password</label>
            <input
              type='password'
              name='password'
              onChange={updatePassword}
              value={password}
              className="sign-up-input-field"
            ></input>
          </div>
          <div className='sign-up-whole-input-div'>
            <label>Repeat Password</label>
            <input
              type='password'
              name='repeat_password'
              onChange={updateRepeatPassword}
              value={repeatPassword}
              required="true"
              className="sign-up-input-field"
            ></input>
          </div>
        </div>
        <div className='left-half-outer-sign-up'>
          <h3 className='sel-pay-title'>Select a Payment Plan</h3>
          <div className='outer-plan-selection'>
            <div className='outer-plan-div'>
              <div className='box-each-plan'>
                <label className='plan-box' htmlFor="basic-with-ads">Basic with ads</label>
              </div>
              <div>
                <input
                  type='radio'
                  id="basic-with-ads"
                  name='plan'
                  value={plan}
                  onClick={() => setPlan('Basic with ads')}>
                </input>
              </div>
              <span>$6.99/month</span>
            </div>
            <div className='outer-plan-div'>
              <div className='box-each-plan'>
                <label htmlFor="standard">Standard</label>
              </div>
              <div>
                <input
                  type='radio'
                  id="standard"
                  name='plan'
                  value={plan}
                  onClick={() => setPlan('Standard')}>
                </input>
              </div>
              <span>$15.49/month</span>
            </div>
            <div className='outer-plan-div'>
              <div className='box-each-plan'>
                <label htmlFor="premium">Premium</label>
              </div>
              <div>
                <input
                  type='radio'
                  id="premium"
                  name='plan'
                  value={plan}
                  onClick={() => setPlan('Premium')}>
                </input>
              </div>
              <span>$19.99/month</span>
            </div>
          </div>
          <button type='submit' className='submit-login'>Sign Up</button>
        </div>
      </form>
      <div className='errors-sign-up-div'>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
    </div>
  );
};

export default SignUpForm;

// type='radio'
// name='Basic with ads'
// onChange={updatePlan}
// value={plan}
// checked
