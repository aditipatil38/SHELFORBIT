
import React, { useState } from 'react';
import { db, auth } from '../firebase';
import { addDoc, collection, serverTimestamp } from 'firebase/firestore';
import { Input, Button, Box } from '@mui/material';

function SendMessage({ scroll, roomCode }) {
  const [msg, setMsg] = useState('');

  const sendMessage = async (e) => {
    e.preventDefault();
    const { uid, photoURL, displayName } = auth.currentUser || {};

    if (!msg.trim()) return; // Prevent empty messages

    try {
      await addDoc(collection(db, `rooms/${roomCode}/messages`), {
        text: msg,
        photoURL: photoURL || '/dp4.png', // Default image if no photoURL is provided
        uid,
        displayName: displayName || 'Anonymous', // Default name if none is provided
        createdAt: serverTimestamp(),
      });

      setMsg(''); // Clear the message input
      scroll.current?.scrollIntoView({ behavior: 'smooth' }); // Scroll to the latest message
    } catch (error) {
      console.error('Error sending message:', error.message);
    }
  };

  return (
    <Box component="form" onSubmit={sendMessage} className="sendMessageForm">
      <Input
        fullWidth
        placeholder="Type your message..."
        value={msg}
        onChange={(e) => setMsg(e.target.value)}
        className="msgInput"
      />
      <Button
        type="submit"
        variant="contained"
        className="sendButton"
      >
        Send
      </Button>
    </Box>
  );
}

export default SendMessage;
