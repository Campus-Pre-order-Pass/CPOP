import React, { useState } from 'react';
// @mui
import { styled } from '@mui/material/styles';
import { Badge, Button, Box, Paper, IconButton, Stack } from '@mui/material';
import CancelIcon from '@mui/icons-material/Cancel';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

// component
import Iconify from '../../../components/iconify';
import AddMenuItemFrom from '../../@product/AddMenuItemForm';

// ----------------------------------------------------------------------

const StyledRoot = styled('div')(({ theme }) => ({
  zIndex: 999,
  right: 0,
  display: 'flex',
  cursor: 'pointer',
  position: 'fixed',
  alignItems: 'center',
  top: theme.spacing(16),
  height: theme.spacing(5),
  paddingLeft: theme.spacing(2),
  paddingRight: theme.spacing(2),
  paddingTop: theme.spacing(1.25),
  boxShadow: theme.customShadows.z20,
  color: theme.palette.text.primary,
  backgroundColor: theme.palette.background.paper,
  borderTopLeftRadius: Number(theme.shape.borderRadius) * 2,
  borderBottomLeftRadius: Number(theme.shape.borderRadius) * 2,
  transition: theme.transitions.create('opacity'),
  '&:hover': { opacity: 0.72 },
}));

// ----------------------------------------------------------------------

export default function CartWidget() {
  const [isCardOpen, setIsCardOpen] = useState(false);

  const handleToggleCard = () => {
    setIsCardOpen((prev) => !prev);
  };
  return (

    <>

      <StyledRoot>
        {/* <Badge showZero badgeContent={0} color="error" max={99}>
        <Iconify icon="gridicons:add-outline" width={24} height={24} />
      </Badge> */}
        <IconButton onClick={handleToggleCard}>
          <Iconify icon="gridicons:add-outline" width={24} height={24} />
        </IconButton>

      </StyledRoot>
      {isCardOpen && (
        <Card
          sx={{
            width: 345,
            maxHeight: 500,
            overflow: 'auto',
            p: 2,
            border: '1px  grey',
            position: 'fixed',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            zIndex: 999,
          }}
        >
          <Stack
            direction="row"
            justifyContent="space-between" // 在两侧对齐
            alignItems="center" // 在垂直方向上居中
          >
            <Typography variant="h5" component="div">
              新增菜單
            </Typography>
            <Stack direction="row" spacing={1}>

              <IconButton onClick={handleToggleCard} size="small">
                <CancelIcon />
              </IconButton>
            </Stack>
          </Stack>
          {/* body */}
          <CardContent>

            <AddMenuItemFrom />
          </CardContent>
        </Card >
      )
      }


    </>
  );
}
