// //App.js

import './App.css';
import Chat from './components/Chat';
import SignIn from './components/SignIn';
import Room from './components/Room';
import { auth } from './firebase';
import { useAuthState } from 'react-firebase-hooks/auth';
import React, { useState } from 'react';

function App() {
  const [user] = useAuthState(auth);
  const [roomCode, setRoomCode] = useState('');

  return (
    <>
      {user ? (
        roomCode ? (
          <Chat roomCode={roomCode} setRoomCode={setRoomCode} />
        ) : (
          <Room setRoomCode={setRoomCode} />
        )
      ) : (
        <SignIn />
      )}
    </>
  );
}

export default App;
