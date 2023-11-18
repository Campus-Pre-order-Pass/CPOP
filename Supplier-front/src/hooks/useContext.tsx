import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  ReactNode,
} from "react";
import auth from "../firebase/firebase";

// 定义上下文值的类型
interface ContextValue {
  login: boolean;
  setLogin: React.Dispatch<React.SetStateAction<boolean>>;
  uid: string;
  setUid: React.Dispatch<React.SetStateAction<string>>;
  token: string;
  setToken: React.Dispatch<React.SetStateAction<string>>;
  displayName: string;
  setDisplayName: React.Dispatch<React.SetStateAction<string>>;
  photoURL: string;
  setPhotoURL: React.Dispatch<React.SetStateAction<string>>;
  email: string;
  setEmail: React.Dispatch<React.SetStateAction<string>>;
}

// 创建上下文对象
const MyContext = createContext<ContextValue | undefined>(undefined);

interface AppProviderProps {
  children: ReactNode;
}

// 创建自定义的上下文提供者组件
export default function AppProvider({ children }: AppProviderProps) {
  const [login, setLogin] = useState(false);
  const [uid, setUid] = useState("");
  const [token, setToken] = useState("");
  const [displayName, setDisplayName] = useState("");
  const [photoURL, setPhotoURL] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged((authUser) => {
      if (authUser) {
        setUid(authUser.uid);
        setDisplayName(authUser.displayName || "");
        setPhotoURL(authUser.photoURL || "");
        setEmail(authUser.email || "");
        setLogin(true);
      }
    });

    return () => {
      unsubscribe();
    };
  }, []);

  const contextValue: ContextValue = {
    login,
    setLogin,
    uid,
    setUid,
    token,
    setToken,
    displayName,
    setDisplayName,
    photoURL,
    setPhotoURL,
    email,
    setEmail,
  };

  return (
    // 使用 Provider 将数据提供给需要访问上下文的组件
    <MyContext.Provider value={contextValue}>{children}</MyContext.Provider>
  );
}

// 创建一个自定义钩子以在组件中使用上下文
export function useAppContext(): ContextValue {
  const context = useContext(MyContext);
  if (!context) {
    throw new Error("useAppContext must be used within an AppProvider");
  }
  return context;
}
