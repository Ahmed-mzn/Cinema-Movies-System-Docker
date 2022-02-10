import store from '../store'


import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import LogIn from '../views/LogIn.vue'
import Dashboard from '../views/Dashboard.vue'
import Categories from '../views/Categories.vue'
import Movies from '../views/Movies.vue'
import Bookings from '../views/Bookings.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/categories',
    name: 'Categories',
    component: Categories,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/movies',
    name: 'Movies',
    component: Movies,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/bookings',
    name: 'Bookings',
    component: Bookings,
    meta: {
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requireLogin) && !store.state.user.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})

export default router
