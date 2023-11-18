import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../components/iconify/index';
// firebase
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";

import auth from '../../../firebase/firebase';
// context 
import { useAppContext } from '../../../hooks/useContext';
// texts
import TEXTS from '../../../locales/text';

// ----------------------------------------------------------------------

export default function LoginForm() {
  const { setLogin, setUid, setToken, setDisplayName, setPhotoURL, email, setEmail } = useAppContext();
  const navigate = useNavigate();
  const providerGoogle = new GoogleAuthProvider();

  // const [showPassword, setShowPassword] = useState(false);
  // const [password, setPassword] = useState('');

  const handleClick = () => {
    // signInWithEmailAndPassword(auth, email, password)
    //   .then((userCredential) => {
    //     // Signed in 
    //     const user = userCredential.user;
    //     handleUserDataContextChange("uid", user.uid);
    //     // dashboard
    //     // navigate('/dashboard', { replace: true });
    //   })
    //   .catch((error) => {
    //     const errorCode = error.code;
    //     const errorMessage = error.message;
    //     // ..
    //   });


    signInWithPopup(auth, providerGoogle)
      .then((result) => {
        const credential = GoogleAuthProvider.credentialFromResult(result);
        const token = credential.accessToken;
        const user = result.user;


        setLogin(true);
        setUid(user.uid);
        setToken(token);
        setDisplayName(user.displayName);
        setPhotoURL(user.photoURL);
        setEmail(user.email);

        navigate('/dashboard', { replace: true });

      }).catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.email;
        const credential = GoogleAuthProvider.credentialFromError(error);
      });
  };

  return (
    <>
      <Stack direction={"column"} spacing={3}>

        {/* <Stack spacing={3}>
          <TextField
            name="email"
            label={TEXTS.LoginPage.email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <TextField
            name="password"
            label={TEXTS.LoginPage.password}
            type={showPassword ? 'text' : 'password'}
            onChange={(e) => setPassword(e.target.value)}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton onClick={() => setShowPassword(!showPassword)} edge="end">
                    <Iconify icon={showPassword ? 'eva:eye-fill' : 'eva:eye-off-fill'} />
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
        </Stack> */}
        <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={handleClick}>
          登錄
        </LoadingButton>
      </Stack>
    </>
  );
}
