import { Navigate, useRoutes, useNavigate } from 'react-router-dom';
// layouts
import DashboardLayout from './layouts/dashboard';
import SimpleLayout from './layouts/simple';
// pasges
import BlogPage from './pages/BlogPage';
import UserPage from './pages/UserPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import Page404 from './pages/Page404';
import ProductsPage from './pages/ProductsPage';
import DashboardAppPage from './pages/DashboardAppPage';
import VendorPage from './pages/VendorPage';
import CurrentStaterPage from './pages/CurrentStaterPage';
// context
import { useAppContext } from './hooks/useContext';

// ----------------------------------------------------------------------

export default function Router() {
  const { login } = useAppContext();

  const navigate = useNavigate();

  // 判断是否已登录，如果未登录且不在登录或注册页面，则重定向到登录页面
  if (!login && !['/login', '/register'].includes(window.location.pathname)) {
    navigate('/login');
  }
  const routes = useRoutes([
    {
      path: '/dashboard',
      element: <DashboardLayout />,
      children: [
        { element: <Navigate to="/dashboard/app" />, index: true },
        { path: 'app', element: <DashboardAppPage /> },
        { path: 'user', element: <UserPage /> },
        { path: 'products', element: <ProductsPage /> },
        { path: 'blog', element: <BlogPage /> },
        { path: 'current', element: <CurrentStaterPage /> },
        { path: '@me', element: <VendorPage /> },
        { path: '@me/:vendor', element: <VendorPage /> },
      ],
    },
    {
      path: 'login',
      element: <LoginPage />,
    },
    {
      path: 'register',
      element: <RegisterPage />,
    },
    {
      element: <SimpleLayout />,
      children: [
        { element: <Navigate to="/dashboard/app" />, index: true },
        { path: '404', element: <Page404 /> },
        { path: '*', element: <Navigate to="/404" /> },
      ],
    },
    {
      path: '*',
      element: <Navigate to="/404" replace />,
    },
  ]);

  return routes;
}
