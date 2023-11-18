import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../components/iconify/index';
// firebase
// import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
import auth from '../../../firebase/firebase';
// conetxt
import { useAppContext } from '../../../hooks/useContext';
// ----------------------------------------------------------------------

export default function RegisterFirebaseFrom({ setCurrentStep, setUid, setEmail, setDisplayName }) {
    const { handleUserDataContextChange } = useAppContext();

    const providerGoogle = new GoogleAuthProvider();

    const handleClick = () => {
        // createUserWithEmailAndPassword(auth, email, password)
        //     .then((userCredential) => {
        //         // Signed in 
        //         const user = userCredential.user;
        //         const uid = user.uid;

        //         handleFirebaseFormChange("uid", uid);
        //         setUid(uid);
        //         handleFirebaseFormChange("displayName", user.displayName);
        //         handleFirebaseFormChange("email", user.email);

        //         console.log(uid)

        //         setCurrentStep(2);
        //     })
        //     .catch((error) => {
        //         const errorCode = error.code;
        //         const errorMessage = error.message;

        //         console.error(errorMessage, errorCode)
        //     });



        signInWithPopup(auth, providerGoogle)
            .then((result) => {
                const credential = GoogleAuthProvider.credentialFromResult(result);
                const token = credential.accessToken;
                const user = result.user;


                setUid(user.uid);
                setEmail(user.email);
                setDisplayName(user.displayName);





                setCurrentStep(2);


            }).catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;
                const email = error.email;
                const credential = GoogleAuthProvider.credentialFromError(error);

                console.log(errorMessage)
            });
    };



    return (
        <>
            <Stack direction={"column"} spacing={3}>

                <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={handleClick}>
                    <Stack direction={"row"} spacing={2} alignItems={"center"}>
                        <Iconify icon="ri:google-fill" />
                        <div>

                            註冊
                        </div>
                    </Stack>
                </LoadingButton>
            </Stack>
        </>
    );
}
