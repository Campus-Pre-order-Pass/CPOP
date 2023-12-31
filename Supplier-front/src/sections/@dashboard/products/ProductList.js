import PropTypes from 'prop-types';
// @mui
import { Grid } from '@mui/material';
import ShopProductCard from './ProductCard';

// ----------------------------------------------------------------------

ProductList.propTypes = {
  products: PropTypes.array.isRequired,
};

export default function ProductList({ products, setSelectProduct, ...other }) {
  return (
    <Grid container spacing={3} {...other}>
      {products.map((product) => (
        <Grid key={product.product_id} item xs={12} sm={6} md={3}>
          <ShopProductCard product={product} setSelectProduct={setSelectProduct} />
        </Grid>
      ))}
    </Grid>
  );
}
