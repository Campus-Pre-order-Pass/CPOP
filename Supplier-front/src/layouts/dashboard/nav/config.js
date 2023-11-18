// component
import SvgColor from '../../../components/svg-color';

// ----------------------------------------------------------------------

const icon = (name) => <SvgColor src={`/assets/icons/navbar/${name}.svg`} sx={{ width: 1, height: 1 }} />;

const navConfig = [
  {
    title: '分析',
    path: '/dashboard/app',
    icon: icon('ic_analytics'),
  },
  {
    title: '廠商資料',
    path: '/dashboard/@me',
    icon: icon('ic_user'),
  },
  {
    title: '產品',
    path: '/dashboard/products',
    icon: icon('ic_cart'),
  },
  {
    title: '狀態',
    path: '/dashboard/current',
    icon: icon('ic_cart'),
  },


];

export default navConfig;
