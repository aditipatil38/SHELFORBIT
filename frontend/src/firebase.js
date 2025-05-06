import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
    apiKey: "AIzaSyC6aL68gpxn7FFxmHdsoPwA_jbJKBXSxzs",
    authDomain: "orbit-a2fb9.firebaseapp.com",
    projectId: "orbit-a2fb9",
    storageBucket: "orbit-a2fb9.firebasestorage.app",
    messagingSenderId: "945244426484",
    appId: "1:945244426484:web:8c9f1f9daf409bab820ea1",
    measurementId: "G-KYGRJSMR2D",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { auth, db };
