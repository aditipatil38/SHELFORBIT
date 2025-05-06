// //SignOut.js

import React from 'react';
import { auth } from '../firebase';
import { Button } from '@mui/material';

function SignOut() {
  const handleSignOut = () => auth.signOut();

  return (
    <div className="signOut">
      <Button variant="contained" onClick={handleSignOut}>
        Sign Out
      </Button>
    </div>
  );
}

export default SignOut;
