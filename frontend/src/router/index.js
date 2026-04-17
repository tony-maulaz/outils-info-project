import { createRouter, createWebHistory } from 'vue-router'
import { useAppStore } from '../stores/app'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Guard de navigation — à compléter pour protéger les routes
router.beforeEach((to) => {
  console.log(`[router] navigation vers "${to.name}"`)
  const appStore = useAppStore()

  // Pages accessibles sans être connecté
  const publicPages = ['login']

  // TODO: Décommenter et adapter pour activer la protection des routes
  // if (!publicPages.includes(to.name) && !appStore.currentUser) {
  //   return { name: 'login' }
  // }
})

export default router
