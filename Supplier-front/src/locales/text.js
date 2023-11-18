const projName = "CPOP";
const CONSTANT = {
    email: "信箱",
    password: "密碼",
}
// page


const DashbroadPage = {
    name: "分析",
    title_1: `歡迎回來`,
    title_2: "使用第三方登陸"
};

const RegisterPage = {
    name: "註冊",
    title_1: `歡迎註冊${projName}預購平台`,
    title_2: "使用第三方登陸"
};


const LoginPage = {
    name: "登錄",
    title_1: `歡迎回來`,
    title_2: "登錄CPOP後台",
    email: CONSTANT.email,
    password: CONSTANT.password,
};

const Vendorpage = {
    name: "廠商",
    title_1: `歡迎使用${projName}預購平台`,
    title_2: "使用第三方登陸"
};


const CurrentStaterPage = {
    name: "狀態",
};

const ProductsPage = {
    name: "產品",
};


const TEXTS = {
    projName,
    DashbroadPage,
    RegisterPage,
    LoginPage,
    Vendorpage,
    ProductsPage,
    CurrentStaterPage,
}


export default TEXTS;