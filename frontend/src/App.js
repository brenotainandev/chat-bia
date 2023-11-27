import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async (event) => {
    event.preventDefault();
    const response = await axios.get(`http://localhost:5000/resposta/${message}`);
    setChat([...chat, { message, user: 'user' }, { message: response.data, user: 'bot' }]);
    setMessage("");
  };

  return (
    <div className="App">
  <h1>Atendimento AgroTech</h1>
  <div className="chat">
    {chat.map((chat, index) => (
      <div key={index} className={chat.user}>
        <p>{chat.message}</p>
      </div>
    ))}
  </div>
  <form onSubmit={sendMessage}>
    <input value={message} onChange={e => setMessage(e.target.value)} />
    <button type="submit">Enviar</button>
  </form>
</div>
  );
}

export default App;