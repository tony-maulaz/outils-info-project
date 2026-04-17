import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAppStore = defineStore('app', () => {
  // Persistance du token entre les rechargements de page
  const token = ref(localStorage.getItem('token') || null)
  const currentUser = ref(JSON.parse(localStorage.getItem('user') || 'null'))

  const appMessage = ref('Bienvenue dans le cours WEB !')

  function setCurrentUser(user, accessToken) {
    currentUser.value = user
    token.value = accessToken
    localStorage.setItem('user', JSON.stringify(user))
    localStorage.setItem('token', accessToken)
  }

  function logout() {
    currentUser.value = null
    token.value = null
    localStorage.removeItem('user')
    localStorage.removeItem('token')
  }

  return {
    token,
    currentUser,
    appMessage,
    setCurrentUser,
    logout,
  }
})
