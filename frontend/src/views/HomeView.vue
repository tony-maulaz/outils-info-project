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
  </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { useAppStore } from '../stores/app'

const appStore = useAppStore()
const router = useRouter()

function handleLogout() {
  appStore.logout()
  router.push({ name: 'login' })
}
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
