<template>
  <div class="page-centered">
    <div class="card" style="text-align: center">
      <h1>Bienvenue au cours WEB</h1>

      <!-- Message lu depuis le store Pinia (exemple) -->
      <p class="store-message">{{ appStore.appMessage }}</p>

      <!-- Afficher le nom de l'utilisateur connecté -->
      <div v-if="appStore.currentUser" class="user-info">
        <p>
          Connecté en tant que :
          <strong>{{ appStore.currentUser.first_name }} {{ appStore.currentUser.last_name }}</strong>
        </p>
        <button @click="handleLogout" class="btn btn-secondary">Se déconnecter</button>
      </div>
      <div v-else>
        <p>Vous n'êtes pas connecté.</p>
        <RouterLink to="/login" class="btn btn-primary">Se connecter</RouterLink>
      </div>
    </div>

    <!-- Exemple de requête authentifiée -->
    <div class="card" style="margin-top: 1.5rem">
      <h2>Liste des utilisateurs</h2>
      <p v-if="loading">Chargement...</p>
      <p v-else-if="error" class="error-message">{{ error }}</p>
      <ul v-else-if="users.length">
        <li v-for="user in users" :key="user.id">
          {{ user.first_name }} {{ user.last_name }} — {{ user.email }}
        </li>
      </ul>
      <p v-else>Aucun utilisateur.</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import api from '../api'
import { useAppStore } from '../stores/app'

const appStore = useAppStore()
const router = useRouter()

const users = ref([])
const loading = ref(false)
const error = ref('')

function handleLogout() {
  appStore.logout()
  router.push({ name: 'login' })
}

onMounted(async () => {
  loading.value = true
  try {
    const response = await api.get('/api/users')
    users.value = response.data
  } catch (err) {
    if (err.response?.status === 401) {
      error.value = 'Non autorisé — connectez-vous pour voir les utilisateurs.'
    } else {
      error.value = 'Erreur lors du chargement des utilisateurs.'
    }
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.store-message {
  color: #666;
  font-style: italic;
  margin-bottom: 1.5rem;
}

.user-info {
  background: #e8f5e9;
  border-radius: 6px;
  padding: 1rem;
  margin-top: 1rem;
}

.user-info p {
  margin-bottom: 0.75rem;
}
</style>
