import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAppStore = defineStore('app', () => {
  // Utilisateur connecté (null si non connecté)
  const currentUser = ref(null)

  // Exemple d'une valeur dans le store (à titre démonstratif)
  const appMessage = ref('Bienvenue dans le cours WEB !')

  function setCurrentUser(user) {
    currentUser.value = user
  }

  function logout() {
    currentUser.value = null
  }

  return {
    currentUser,
    appMessage,
    setCurrentUser,
    logout,
  }
})
