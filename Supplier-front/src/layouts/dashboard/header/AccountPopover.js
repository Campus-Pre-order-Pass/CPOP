import { useState } from 'react';
import { Navigate, useRoutes, useNavigate } from 'react-router-dom';
// @mui
import { alpha } from '@mui/material/styles';
import { Box, Divider, Typography, Stack, MenuItem, Avatar, IconButton, Popover } from '@mui/material';
// context
import { useAppContext } from '../../../hooks/useContext';
// func
import { func } from 'prop-types';
// firebase
import auth from '../../../firebase/firebase';
// texts
import TEXTS from '../../../locales/text';

// ----------------------------------------------------------------------

const MENU_OPTIONS = [
  {
    label: TEXTS.DashbroadPage.name,
    icon: 'eva:home-fill',
  },
  {
    label: TEXTS.Vendorpage.name,
    icon: 'eva:person-fill',
  },
  {
    label: TEXTS.ProductsPage.name,
    icon: 'eva:settings-2-fill',
  },
];

// ----------------------------------------------------------------------



export default function AccountPopover() {
  const navigate = useNavigate();
  const { photoURL, displayName, email, setLogin } = useAppContext();
  const [open, setOpen] = useState(null);

  const handleOpen = (event) => {
    setOpen(event.currentTarget);
  };

  const handleClose = () => {
    setOpen(null);
  };

  const handleLogout = async () => {

    try {
      await auth.signOut(); // 调用 Firebase 的 signOut 方法
      setLogin(false); // 设置登录状态为 false
      navigate('/login');
    } catch (error) {
      console.error('Sign out error:', error);
    }

  }

  return (
    <>
      <IconButton
        onClick={handleOpen}
        sx={{
          p: 0,
          ...(open && {
            '&:before': {
              zIndex: 1,
              content: "''",
              width: '100%',
              height: '100%',
              borderRadius: '50%',
              position: 'absolute',
              bgcolor: (theme) => alpha(theme.palette.grey[900], 0.8),
            },
          }),
        }}
      >
        <Avatar src={photoURL} alt="photoURL" />
      </IconButton>

      <Popover
        open={Boolean(open)}
        anchorEl={open}
        onClose={handleClose}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
        transformOrigin={{ vertical: 'top', horizontal: 'right' }}
        PaperProps={{
          sx: {
            p: 0,
            mt: 1.5,
            ml: 0.75,
            width: 180,
            '& .MuiMenuItem-root': {
              typography: 'body2',
              borderRadius: 0.75,
            },
          },
        }}
      >
        <Box sx={{ my: 1.5, px: 2.5 }}>
          <Typography variant="subtitle2" noWrap>
            {displayName}
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary' }} noWrap>
            {email}
          </Typography>
        </Box>

        <Divider sx={{ borderStyle: 'dashed' }} />

        <Stack sx={{ p: 1 }}>
          {MENU_OPTIONS.map((option) => (
            <MenuItem key={option.label} onClick={handleClose}>
              {option.label}
            </MenuItem>
          ))}
        </Stack>

        <Divider sx={{ borderStyle: 'dashed' }} />

        <MenuItem onClick={handleLogout} sx={{ m: 1 }}>
          登出
        </MenuItem>
      </Popover>
    </>
  );
}
