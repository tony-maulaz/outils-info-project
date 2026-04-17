<template>
  <div class="page-centered">
    <div class="card">
      <h1>Connexion</h1>

      <form @submit.prevent="handleLogin" novalidate>
        <div class="form-group">
          <label for="email">Email</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            placeholder="votre@email.com"
            :class="{ error: errors.email }"
            @blur="validateEmail"
          />
          <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
        </div>

        <!-- Erreur globale (ex: mauvais identifiants) -->
        <div v-if="serverError" class="alert alert-error">
          {{ serverError }}
        </div>

        <button type="submit" class="btn btn-primary" :disabled="loading">
          {{ loading ? 'Connexion...' : 'Se connecter' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api'
import { useAppStore } from '../stores/app'

const appStore = useAppStore()
const router = useRouter()

const form = reactive({ email: '' })
const errors = reactive({ email: '' })
const serverError = ref('')
const loading = ref(false)

function validateEmail() {
  if (!form.email) {
    errors.email = "L'email est requis."
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
    errors.email = "Format d'email invalide."
  } else {
    errors.email = ''
  }
}

function isFormValid() {
  validateEmail()
  return !errors.email
}

async function handleLogin() {
  serverError.value = ''
  if (!isFormValid()) return

  loading.value = true
  try {
    const response = await api.post('/api/login', {
      email: form.email,
    })
    appStore.setCurrentUser(response.data.user, response.data.access_token)
    router.push({ name: 'home' })
  } catch (err) {
    if (err.response?.status === 401) {
      serverError.value = 'Email ou mot de passe incorrect.'
    } else {
      serverError.value = 'Une erreur est survenue. Veuillez réessayer.'
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* Spécifique au bouton submit (pleine largeur) */
.btn {
  width: 100%;
}
</style>
