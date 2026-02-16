import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import ChatInterface from './components/ChatInterface';
import AgentDashboard from './components/AgentDashboard';

function App() {
  const [activeTab, setActiveTab] = useState('chat');

  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <header className="bg-white shadow-sm border-b">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div className="flex items-center justify-between">
              <h1 className="text-2xl font-bold text-gray-900">
                ⚡ FAST AI Platform
              </h1>
              <nav className="flex space-x-4">
                <Link
                  to="/"
                  onClick={() => setActiveTab('chat')}
                  className={`px-4 py-2 rounded-lg transition ${
                    activeTab === 'chat'
                      ? 'bg-primary text-white'
                      : 'text-gray-600 hover:bg-gray-100'
                  }`}
                >
                  💬 Chat
                </Link>
                <Link
                  to="/agents"
                  onClick={() => setActiveTab('agents')}
                  className={`px-4 py-2 rounded-lg transition ${
                    activeTab === 'agents'
                      ? 'bg-primary text-white'
                      : 'text-gray-600 hover:bg-gray-100'
                  }`}
                >
                  🤖 Agents
                </Link>
              </nav>
            </div>
          </div>
        </header>

        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <Routes>
            <Route path="/" element={<ChatInterface />} />
            <Route path="/agents" element={<AgentDashboard />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;