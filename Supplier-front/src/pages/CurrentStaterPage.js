import React, { useEffect, useState } from 'react';
import { Helmet } from 'react-helmet-async';
import axios from 'axios';
// @mui
import { Container, Skeleton } from '@mui/material';
// hooks
// components
// comp
import CurrentForm from '../sections/@current/CurrentForm';
// text
import TEXTS from '../locales/text';
// conf
import { URLCONF } from '../conf';
// useAppContext
import { useAppContext } from '../hooks/useContext';

// fb

// ----------------------------------------------------------------

export default function CurrentStaterPage() {
    const { uid } = useAppContext();
    // const uid = auth.currentUser.uid;

    const [currentState, setCurrentState] = useState(null);

    useEffect(() => {
        axios.get(URLCONF.CurrentStateUrl(uid)).then((response) => {

            setCurrentState(response.data);
        });
    }, []);

    return (<>
        <Helmet>
            <title> {TEXTS.CurrentStaterPage.name} | {TEXTS.projName} </title>
        </Helmet>

        <Container>
            {
                currentState == null ? (
                    <Skeleton height={"1000px"} />
                ) : (
                    <CurrentForm currentState={currentState} />
                )
            }
        </Container>
    </>);
}