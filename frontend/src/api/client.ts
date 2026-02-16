import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface Message {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export interface ChatRequest {
  messages: Message[];
  provider?: string;
  model?: string;
  temperature?: number;
  max_tokens?: number;
}

export interface ChatResponse {
  response: string;
  model: string;
  tokens_used: number;
}

export interface AgentConfig {
  name: string;
  description: string;
  provider: string;
  model: string;
  temperature: number;
  max_tokens: number;
  tools: string[];
}

export const api = {
  health: () => apiClient.get('/health'),
  chat: (request: ChatRequest) => apiClient.post<ChatResponse>('/api/chat/completions', request),
  createAgent: (config: AgentConfig) => apiClient.post('/api/agents', config),
  listAgents: () => apiClient.get('/api/agents'),
  getAgent: (agentId: string) => apiClient.get(`/api/agents/${agentId}`),
  deleteAgent: (agentId: string) => apiClient.delete(`/api/agents/${agentId}`),
  runAgent: (agentId: string, task: string) => apiClient.post(`/api/agents/${agentId}/run`, { task }),
};

export default apiClient;