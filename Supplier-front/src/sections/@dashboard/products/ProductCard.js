import PropTypes from 'prop-types';
import React, { useState } from 'react';
// @mui
import { Box, Card, Link, Typography, Stack } from '@mui/material';
import { styled } from '@mui/material/styles';
import Tooltip from '@mui/material/Tooltip';
import IconButton from '@mui/material/IconButton';
// utils
import { fCurrency } from '../../../utils/formatNumber';
// components
import Label from '../../../components/label';
import { ColorPreview } from '../../../components/color-utils';
// CONF
import { URLCONF } from '../../../conf';
// icon
import Iconify from '../../../components/iconify/Iconify';
// helper
import translateTypeToChinese from '../../../helper/index.d';
// ----------------------------------------------------------------------

const StyledProductImg = styled('img')({
  top: 0,
  width: '100%',
  height: '100%',
  objectFit: 'cover',
  position: 'absolute',
});

// ----------------------------------------------------------------------

ShopProductCard.propTypes = {
  product: PropTypes.object,
};

export default function ShopProductCard({ product, setSelectProduct }) {

  const { product_id, type, price, unit, hot, menu_img_url, desc, promotions
    , name, } = product;


  return (
    <>
      <Card>
        <Box sx={{ pt: '100%', position: 'relative' }}>
          {hot && (
            <Label
              variant="filled"
              color={"error"}
              sx={{
                zIndex: 9,
                top: 16,
                right: 16,
                position: 'absolute',
                textTransform: 'uppercase',
              }}
            >

              熱門推薦
            </Label>
          )}


          <Label
            variant="filled"
            color={"info"}
            sx={{
              zIndex: 9,
              top: 16,
              right: hot ? 90 : 16,
              position: 'absolute',
              textTransform: 'uppercase',
            }}
          >
            {translateTypeToChinese(type)}
          </Label>


          <StyledProductImg alt={name} src={`${URLCONF.BaseUrl}${menu_img_url}`} />
        </Box>


        <Stack spacing={2} sx={{ p: 3 }}>
          <Stack direction="row" >
            <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%' }}>
              <div>
                <Link color="inherit" underline="hover">
                  <Typography variant="subtitle2" noWrap>
                    {name}
                  </Typography>
                </Link>
              </div>
              <IconButton
                color="primary"
                onClick={() => setSelectProduct(product)}
              >
                <Iconify icon='tabler:tool' />
              </IconButton>
            </div>
          </Stack>

          <Stack direction="row" >
            <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%' }}>

              <Stack direction="row" alignItems="center" justifyContent="space-between">
                {/* <ColorPreview colors={colors} /> */}
                <Typography variant="overline" color="gray">

                  &nbsp;
                  {desc || "沒有解釋"}
                </Typography>
              </Stack>

              <Stack>
                <Typography variant="subtitle1">

                  &nbsp;
                  {fCurrency(price)}/{unit}
                </Typography>
              </Stack>
            </div>
          </Stack>

        </Stack>
      </Card >

    </>

  );
}
