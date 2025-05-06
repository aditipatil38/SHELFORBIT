// //SignIn.js

import React from 'react';
import { auth, db } from '../firebase';
import { Button, Box, Typography } from '@mui/material';
import { GoogleAuthProvider, signInWithPopup } from 'firebase/auth';
import { doc, setDoc } from 'firebase/firestore';

function SignIn() {
  async function signInWithGoogle() {
    const provider = new GoogleAuthProvider();
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;

      // Save user details to Firestore
      await setDoc(doc(db, 'users', user.uid), {
        uid: user.uid,
        displayName: user.displayName || 'Anonymous',
        photoURL: user.photoURL || '/dp.png',
      });
    } catch (error) {
      console.error('Error during sign-in:', error.message);
    }
  }

  return (
    <Box className="signIn">
      <Typography variant="h4" mb={3}>
        Welcome to Chat App
      </Typography>
      <Button
        onClick={signInWithGoogle}
        variant="contained"
        size="large"
        className="signInButton"
      >
        Sign in with Google
      </Button>
    </Box>
  );
}

export default SignIn;
