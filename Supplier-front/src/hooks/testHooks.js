import { createContext, useContext, useState, useEffect } from 'react';
import auth from '../firebase/firebase'

// 创建上下文对象
const MyContext = createContext();

// 创建自定义的上下文提供者组件
export default function AppProvider({ children }) {
  const [login, setLogin] = useState(false);

  const [uid, setUid] = useState("");
  const [token, setToken] = useState("");
  const [displayName, setDisplayName] = useState("");
  const [photoURL, setPhotoURL] = useState("");
  const [email, setEmail] = useState("");

  // const handleUserDataContextChange = (fieldName, value) => {
  //   setUserData({
  //     ...userData,
  //     [fieldName]: value,
  //   });
  // };


  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged((authUser) => {
      if (authUser) {
        // 用户已登录
        // console.log(authUser)
        setUid(authUser.uid);
        // setToken(authUser.getIdToken);
        setDisplayName(authUser.displayName);
        setPhotoURL(authUser.photoURL);
        setEmail(authUser.email);
        setLogin(true);
      }
    });

    return () => {
      unsubscribe();
    };
  }, []);

  const contextValue = {
    login, setLogin,
    uid, setUid,
    token, setToken,
    displayName, setDisplayName,
    photoURL, setPhotoURL,
    email, setEmail,
  };

  return (
    // 使用 Provider 将数据提供给需要访问上下文的组件
    <MyContext.Provider value={contextValue}>
      {children}
    </MyContext.Provider>
  );
}

// 创建一个自定义钩子以在组件中使用上下文
export function useAppContext() {
  return useContext(MyContext);
}