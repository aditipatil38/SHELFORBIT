// //Room.js

import React, { useState } from 'react';

function Room({ setRoomCode }) {
  const [code, setCode] = useState('');

  const handleJoinRoom = () => {
    if (code.trim()) {
      setRoomCode(code.trim());
    }
  };

  return (
    <div className="roomContainer">
      <h2>Enter Room Code</h2>
      <input
        type="text"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Room Code"
        className="roomInput"
      />
      <button onClick={handleJoinRoom} className="joinRoomButton">
        Join Room
      </button>
    </div>
  );
}

export default Room;
