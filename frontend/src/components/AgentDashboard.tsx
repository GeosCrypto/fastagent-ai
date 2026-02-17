import React, { useState, useEffect } from 'react';
import { api, AgentConfig } from '../api/client';

interface Agent extends AgentConfig {
  id: string;
  created_at: string;
}

const AgentDashboard: React.FC = () => {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [loading, setLoading] = useState(false);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [runningAgent, setRunningAgent] = useState<string | null>(null);
  const [taskInput, setTaskInput] = useState('');
  const [result, setResult] = useState<string>('');

  const [newAgent, setNewAgent] = useState<AgentConfig>({
    name: '',
    description: '',
    provider: 'openai',
    model: 'gpt-4',
    temperature: 0.7,
    max_tokens: 2000,
    tools: [],
  });

  const availableTools = ['web_search', 'calculator', 'code_executor'];

  useEffect(() => {
    loadAgents();
  }, []);

  const loadAgents = async () => {
    try {
      const response = await api.listAgents();
      setAgents(response.data);
    } catch (error) {
      console.error('Failed to load agents:', error);
    }
  };

  const handleCreateAgent = async () => {
    if (!newAgent.name || !newAgent.description) {
      alert('Please fill in all required fields');
      return;
    }

    setLoading(true);
    try {
      await api.createAgent(newAgent);
      setShowCreateForm(false);
      setNewAgent({
        name: '',
        description: '',
        provider: 'openai',
        model: 'gpt-4',
        temperature: 0.7,
        max_tokens: 2000,
        tools: [],
      });
      loadAgents();
    } catch (error) {
      console.error('Failed to create agent:', error);
      alert('Failed to create agent');
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteAgent = async (agentId: string) => {
    if (!confirm('Are you sure you want to delete this agent?')) return;

    try {
      await api.deleteAgent(agentId);
      loadAgents();
    } catch (error) {
      console.error('Failed to delete agent:', error);
      alert('Failed to delete agent');
    }
  };

  const handleRunAgent = async (agentId: string) => {
    if (!taskInput.trim()) {
      alert('Please enter a task');
      return;
    }

    setRunningAgent(agentId);
    setResult('');

    try {
      const response = await api.runAgent(agentId, taskInput);
      setResult(response.data.result || 'Task completed successfully');
    } catch (error) {
      console.error('Failed to run agent:', error);
      setResult('Error: Failed to run agent');
    } finally {
      setRunningAgent(null);
    }
  };

  const toggleTool = (tool: string) => {
    setNewAgent(prev => ({
      ...prev,
      tools: prev.tools.includes(tool)
        ? prev.tools.filter(t => t !== tool)
        : [...prev.tools, tool],
    }));
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-gray-900">🤖 Agent Dashboard</h2>
        <button
          onClick={() => setShowCreateForm(!showCreateForm)}
          className="px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 transition font-medium"
        >
          {showCreateForm ? 'Cancel' : '+ Create Agent'}
        </button>
      </div>

      {showCreateForm && (
        <div className="bg-white p-6 rounded-lg shadow-lg border">
          <h3 className="text-xl font-semibold mb-4">Create New Agent</h3>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Name *
              </label>
              <input
                type="text"
                value={newAgent.name}
                onChange={(e) => setNewAgent({ ...newAgent, name: e.target.value })}
                className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-primary"
                placeholder="My AI Agent"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Description *
              </label>
              <textarea
                value={newAgent.description}
                onChange={(e) => setNewAgent({ ...newAgent, description: e.target.value })}
                className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-primary"
                rows={3}
                placeholder="Describe what this agent does..."
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Provider
                </label>
                <select
                  value={newAgent.provider}
                  onChange={(e) => setNewAgent({ ...newAgent, provider: e.target.value })}
                  className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-primary"
                >
                  <option value="openai">OpenAI</option>
                  <option value="claude">Claude</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Model
                </label>
                <select
                  value={newAgent.model}
                  onChange={(e) => setNewAgent({ ...newAgent, model: e.target.value })}
                  className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-primary"
                >
                  {newAgent.provider === 'openai' ? (
                    <> 
                      <option value="gpt-4">GPT-4</option>
                      <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
                    </>
                  ) : (
                    <> 
                      <option value="claude-3-opus-20240229">Claude 3 Opus</option>
                      <option value="claude-3-sonnet-20240229">Claude 3 Sonnet</option>
                    </>
                  )}
                </select>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Temperature: {newAgent.temperature}
                </label>
                <input
                  type="range"
                  min="0"
                  max="1"
                  step="0.1"
                  value={newAgent.temperature}
                  onChange={(e) => setNewAgent({ ...newAgent, temperature: parseFloat(e.target.value) })}
                  className="w-full"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Max Tokens
                </label>
                <input
                  type="number"
                  value={newAgent.max_tokens}
                  onChange={(e) => setNewAgent({ ...newAgent, max_tokens: parseInt(e.target.value) })}
                  className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-primary"
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Tools
              </label>
              <div className="flex gap-3">
                {availableTools.map(tool => (
                  <label key={tool} className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="checkbox"
                      checked={newAgent.tools.includes(tool)}
                      onChange={() => toggleTool(tool)}
                      className="w-4 h-4 text-primary focus:ring-2 focus:ring-primary"
                    />
                    <span className="text-sm text-gray-700">{tool}</span>
                  </label>
                ))}
              </div>
            </div>

            <button
              onClick={handleCreateAgent}
              disabled={loading}
              className="w-full px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-300 transition font-medium"
            >
              {loading ? 'Creating...' : 'Create Agent'}
            </button>
          </div>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {agents.length === 0 && !showCreateForm && (
          <div className="col-span-2 text-center py-12 bg-white rounded-lg shadow">
            <p className="text-gray-500">No agents yet. Create your first agent to get started!</p>
          </div>
        )}

        {agents.map(agent => (
          <div key={agent.id} className="bg-white p-6 rounded-lg shadow-lg border hover:shadow-xl transition">
            <div className="flex items-start justify-between mb-4">
              <div>
                <h3 className="text-lg font-semibold text-gray-900">{agent.name}</h3>
                <p className="text-sm text-gray-600 mt-1">{agent.description}</p>
              </div>
              <button
                onClick={() => handleDeleteAgent(agent.id)}
                className="text-red-500 hover:text-red-700 text-sm font-medium"
              >
                Delete
              </button>
            </div>

            <div className="space-y-2 mb-4">
              <div className="flex items-center gap-2 text-sm">
                <span className="font-medium text-gray-700">Provider:</span>
                <span className="text-gray-600">{agent.provider}</span>
              </div>
              <div className="flex items-center gap-2 text-sm">
                <span className="font-medium text-gray-700">Model:</span>
                <span className="text-gray-600">{agent.model}</span>
              </div>
              <div className="flex items-center gap-2 text-sm">
                <span className="font-medium text-gray-700">Tools:</span>
                <span className="text-gray-600">{agent.tools.length > 0 ? agent.tools.join(', ') : 'None'}</span>
              </div>
            </div>

            <div className="space-y-2">
              <input
                type="text"
                value={taskInput}
                onChange={(e) => setTaskInput(e.target.value)}
                placeholder="Enter a task for this agent..."
                className="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-primary"
              />
              <button
                onClick={() => handleRunAgent(agent.id)}
                disabled={runningAgent === agent.id}
                className="w-full px-4 py-2 bg-secondary text-white rounded-lg hover:bg-purple-600 disabled:bg-gray-300 transition font-medium text-sm"
              >
                {runningAgent === agent.id ? 'Running...' : 'Run Task'}
              </button>
            </div>

            {result && runningAgent === null && (
              <div className="mt-4 p-3 bg-gray-50 rounded-lg border">
                <p className="text-sm text-gray-700">{result}</p>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default AgentDashboard;
