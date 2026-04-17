import axios from 'axios'
import { useAppStore } from './stores/app'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
})

// Injecte automatiquement le token JWT sur chaque requête
api.interceptors.request.use((config) => {
  const appStore = useAppStore()
  if (appStore.token) {
    config.headers.Authorization = `Bearer ${appStore.token}`
  }
  return config
})

export default api
