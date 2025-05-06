
import React, { useState, useEffect, useRef } from 'react';
import { db, auth } from '../firebase';
import { collection, query, orderBy, onSnapshot } from 'firebase/firestore';
import SendMessage from './SendMessage';
import SignOut from './SignOut';

function Chat({ roomCode, setRoomCode }) {
  const scroll = useRef();
  const [messages, setMessages] = useState([]);

  // Fetch messages from Firestore
  useEffect(() => {
    const q = query(
      collection(db, `rooms/${roomCode}/messages`),
      orderBy('createdAt')
    );
    const unsubscribe = onSnapshot(q, (snapshot) => {
      setMessages(snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() })));
    });
    return unsubscribe;
  }, [roomCode]);

  // Auto-scroll to the latest message
  useEffect(() => {
    scroll.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const leaveRoom = () => setRoomCode('');

  return (
    <div className="chatContainer">
      {/* Header Section */}
      <div className="chatHeader">
        <h3>Room Code: {roomCode}</h3>
        <div className="chatActions">
          <SignOut />
          <button onClick={leaveRoom}>Leave Room</button>
        </div>
      </div>

      {/* Messages Section */}
      <div className="messagesContainer">
        {messages.map(({ id, text, photoURL, displayName, uid }) => (
          <div
            key={id}
            className={`msg ${uid === auth.currentUser?.uid ? 'sent' : 'received'}`}
          >
            <img
              src={photoURL || '/dp4.png'} // Use fallback image if photoURL is null
              onError={(e) => (e.target.src = '/dp4.png')} // Handle broken image links
              alt="User Avatar"
              className="msgAvatar"
            />
            <div>
              <strong>{displayName || 'Anonymous'}</strong>
              <p>{text}</p>
            </div>
          </div>
        ))}
        <div ref={scroll}></div>
      </div>

      {/* Send Message Component */}
      <SendMessage scroll={scroll} roomCode={roomCode} />
    </div>
  );
}

export default Chat;

// // //Chat.js

// import React, { useState, useEffect, useRef } from 'react';
// import { db, auth } from '../firebase';
// import { collection, query, orderBy, onSnapshot } from 'firebase/firestore';
// import SendMessage from './SendMessage';
// import SignOut from './SignOut';

// function Chat({ roomCode, setRoomCode }) {
//   const scroll = useRef();
//   const [messages, setMessages] = useState([]);

//   useEffect(() => {
//     const q = query(
//       collection(db, `rooms/${roomCode}/messages`),
//       orderBy('createdAt')
//     );
//     const unsubscribe = onSnapshot(q, (snapshot) => {
//       setMessages(snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() })));
//     });
//     return unsubscribe;
//   }, [roomCode]);

//   useEffect(() => {
//     scroll.current?.scrollIntoView({ behavior: 'smooth' });
//   }, [messages]);

//   const leaveRoom = () => setRoomCode('');

//   return (
//     <div className="chatContainer">
//       {/* Header Section */}
//       <div className="chatHeader">
//         <h3>Room Code: {roomCode}</h3>
//         <div className="chatActions">
//           <SignOut />
//           <button onClick={leaveRoom}>Leave Room</button>
//         </div>
//       </div>

//       {/* Messages Section */}
//       <div className="messagesContainer">
//         {messages.map(({ id, text, photoURL, displayName, uid }) => (
//           <div
//             key={id}
//             className={`msg ${uid === auth.currentUser?.uid ? 'sent' : 'received'}`}
//           >
//             <img
//               src={photoURL || '/dp.png'}
//               alt="User Avatar"
//               className="msgAvatar"
//             />
//             <div>
//               <strong>{displayName || 'Anonymous'}</strong>
//               <p>{text}</p>
//             </div>
//           </div>
//         ))}
//         <div ref={scroll}></div>
//       </div>

//       {/* Send Message Component */}
//       <SendMessage scroll={scroll} roomCode={roomCode} />
//     </div>
//   );
// }

// export default Chat;
