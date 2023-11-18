import { Helmet } from 'react-helmet-async';
import React, { useState } from 'react';
// @mui
import { styled } from '@mui/material/styles';
import { Link, Container, Typography, Divider, Stack, Button } from '@mui/material';
// hooks
import useResponsive from '../hooks/useResponsive';
// components
import Logo from '../components/logo';
import Iconify from '../components/iconify';
// sections
import { RegisterFirebaseFrom, RegisterFrom } from '../sections/auth/register';
import LoginFrom from '../sections/auth/login/LoginForm';
// text
import TEXTS from '../locales/text';

// ----------------------------------------------------------------------

const StyledRoot = styled('div')(({ theme }) => ({
    [theme.breakpoints.up('md')]: {
        display: 'flex',
    },
}));

const StyledSection = styled('div')(({ theme }) => ({
    width: '100%',
    maxWidth: 480,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    boxShadow: theme.customShadows.card,
    backgroundColor: theme.palette.background.default,
}));

const StyledContent = styled('div')(({ theme }) => ({
    maxWidth: 480,
    margin: 'auto',
    minHeight: '100vh',
    display: 'flex',
    justifyContent: 'center',
    flexDirection: 'column',
    padding: theme.spacing(12, 0),
}));

// ----------------------------------------------------------------------

export default function RegisterPage() {
    const mdUp = useResponsive('up', 'md');


    const [currentStep, setCurrentStep] = useState(1);

    const [uid, setUid] = useState();
    const [email, setEmail] = useState();
    const [displayName, setDisplayName] = useState();



    return (
        <>
            <Helmet>
                <title> {TEXTS.RegisterPage.name} | {TEXTS.projName} </title>
            </Helmet>

            <StyledRoot>
                <Logo
                    sx={{
                        position: 'fixed',
                        top: { xs: 16, sm: 24, md: 40 },
                        left: { xs: 16, sm: 24, md: 40 },
                    }}
                />

                {mdUp && (
                    <StyledSection>
                        <Typography variant="h3" sx={{ px: 5, mt: 10, mb: 5 }}>
                            Hi, Welcome Back
                        </Typography>
                        <img src="/assets/illustrations/illustration_login.png" alt="login" />
                    </StyledSection>
                )}

                <Container maxWidth="sm">
                    <StyledContent >
                        <Stack direction={"row"} spacing={10}>

                            <Typography style={{ margi: "20px" }} variant="h4" gutterBottom>
                                {TEXTS.RegisterPage.title_1}
                            </Typography>
                            {/* 
                            <Typography color={"blue"}>
                                第{currentStep}步驟
                            </Typography> */}
                            {/* 
                            <div>
                                {currentStep > 1 && (
                                    <Button onClick={handlePrevStep}>上一步</Button>
                                )}
                                {currentStep < 2 && (
                                    <Button onClick={handleNextStep}>下一步</Button>
                                )}
                            </div> */}
                        </Stack>
                        <Divider sx={{ my: 3 }} >
                            <Typography variant="body2" sx={{ color: 'text.secondary' }}>
                                <Iconify icon="devicon:google" color="#DF3E30" width={22} height={22} />
                            </Typography>
                        </Divider>


                        {currentStep === 1 && <RegisterFirebaseFrom
                            setCurrentStep={setCurrentStep}
                            setUid={setUid}
                            setEmail={setEmail}
                            setDisplayName={setDisplayName}
                        />}
                        {currentStep === 2 && <RegisterFrom
                            uid={uid}
                            setCurrentStep={setCurrentStep}
                            email={email}
                            displayName={displayName}
                        />}


                    </StyledContent>
                </Container>
            </StyledRoot>
        </>
    );
}
