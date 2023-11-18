// For Firebase JS SDK v7.20.0 and later, measurementId is optional
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

import "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyApK6gL_Riwn2kODFN5ez-ImZKenciWO0E",
  authDomain: "cpop-6d5a7.firebaseapp.com",
  projectId: "cpop-6d5a7",
  storageBucket: "cpop-6d5a7.appspot.com",
  messagingSenderId: "600191623312",
  appId: "1:600191623312:web:cb63622ec887fbcd027815",
  measurementId: "G-CQVM5LVCTR",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// Initialize Firebase Authentication
const auth = getAuth(app);

export default auth;
