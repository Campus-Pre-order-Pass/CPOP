import { Helmet } from 'react-helmet-async';
import { useState, useEffect } from 'react';
import axios from 'axios';
// @mui
import {
  Container,
  Stack,
  Typography,
  Button,
  Grid,
  Skeleton,
  CircularProgress,
  Box,
  Card,
  IconButton
} from '@mui/material';
import CancelIcon from '@mui/icons-material/Cancel';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
// components
import { ProductSort, ProductList, ProductCartWidget, ProductFilterSidebar } from '../sections/@dashboard/products';
import ToolMenuItemCard from '../sections/@product/ToolMenuItemCard';
// mock
import PRODUCTS from '../_mock/products';
// conf
import { URLCONF } from '../conf';
// texts
import TEXTS from '../locales/text';
// context
import { useAppContext } from '../hooks/useContext';


// ----------------------------------------------------------------------

export default function ProductsPage() {
  const { uid } = useAppContext();


  const [productList, setProductList] = useState(null);

  const [selectProduct, setSelectProduct] = useState(null);

  const [openFilter, setOpenFilter] = useState(false);

  useEffect(() => {
    axios.get(URLCONF.MenuUrl(uid))
      .then((response) => {
        // console.log('Success:', response.data);
        setProductList(response.data);
      })
      .catch((error) => {
        console.error('Error:', error);
        // 在这里处理请求错误，可以显示错误信息或采取其他措施
      });

  }, []);


  const handleOpenFilter = () => {
    setOpenFilter(true);
  };

  const handleCloseFilter = () => {
    setOpenFilter(false);
  };

  const handleToggleCard = () => {
    // setIsCardOpen((prev) => !prev);
    setSelectProduct(null);
    // window.location.reload();
  };

  return (
    <>
      <Helmet>
        <title> {TEXTS.ProductsPage.name}| {TEXTS.projName} </title>
      </Helmet>

      <Container>

        <Typography variant="h4" sx={{ mb: 5 }}>
          {TEXTS.ProductsPage.name}
        </Typography>


        <Stack direction="row" flexWrap="wrap-reverse" alignItems="center" justifyContent="flex-end" sx={{ mb: 5 }}>
          <Stack direction="row" spacing={1} flexShrink={0} sx={{ my: 1 }}>
            <ProductFilterSidebar
              openFilter={openFilter}
              onOpenFilter={handleOpenFilter}
              onCloseFilter={handleCloseFilter}
            />
            <ProductSort />
          </Stack>
        </Stack>


        {productList === null ? (
          (
            <div style={{ width: '100%', height: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>

              <Box sx={{ display: 'flex' }}>
                <CircularProgress />
              </Box>
            </div>
          )) : (

          <ProductList products={productList} setSelectProduct={setSelectProduct} />
        )}

        <ProductCartWidget />
      </Container >


      {selectProduct && (
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
              菜單細節
            </Typography>
            <Stack direction="row" spacing={1}>

              <IconButton onClick={handleToggleCard} size="small">
                <CancelIcon />
              </IconButton>
            </Stack>
          </Stack>
          {/* body */}
          <CardContent>
            <ToolMenuItemCard props={selectProduct} />

          </CardContent>
        </Card >
      )}
    </>
  );
}
