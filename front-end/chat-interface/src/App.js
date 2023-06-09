import React, { useState } from 'react';
import { Helmet } from 'react-helmet';
import './ChatInterface.css';

const predefinedResponses = [
  { content: 'Olá! Como posso ajudar?', sender: 'chatbot' },
  { content: 'Estou bem, obrigado!', sender: 'chatbot' },
  { content: 'Desculpe, não entendi. Pode reformular a pergunta?', sender: 'chatbot' },
];

function ChatInterface() {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const fetchChatbotResponse = (userMessage) => {
    const randomIndex = Math.floor(Math.random() * predefinedResponses.length);
    const botMessage = predefinedResponses[randomIndex];
    const userMessageObj = {
      content: userMessage,
      sender: 'user',
    };
    setMessages([...messages, userMessageObj, botMessage]);
  };

  const handleMessageSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim() === '') {
      return;
    }

    const userMessage = inputValue;

    setMessages([...messages, { content: userMessage, sender: 'user' }]);
    setInputValue('');

    fetchChatbotResponse(userMessage);
  };

  return (
    <div>
      <Helmet>
        <title>SIDI</title>
      </Helmet>
      <h1>SIDI</h1>
      <div className="chat-container">
        <div className="chat-interface">
          <div className="chat-messages">
            {messages.map((message, index) => (
              <div key={index} className={`message ${message.sender}`}>
                <span className="sender">{message.sender === 'chatbot' ? 'CHATBOT' : 'Você'}</span>
                <span className="content">{message.content}</span>
              </div>
            ))}
          </div>
          <form onSubmit={handleMessageSubmit} className="chat-input-form">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Digite sua mensagem..."
              className="chat-input"
            />
            <button type="submit" className="send-button">
              Enviar
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default ChatInterface;
