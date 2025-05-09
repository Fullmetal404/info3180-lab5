import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieForm from '../components/MovieForm.vue'
import AddMovieFormView from '../views/AddMovieFormView.vue'
import MoviesView from '../views/MoviesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/movies/create',
      name: 'movies',
      component: AddMovieFormView
    },
    {
      path: '/movies',
      name: 'movies_list',
      component: MoviesView
    }
  ]
})

export default router