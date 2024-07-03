import { createRouter, createWebHistory } from 'vue-router'
import EmployeeView from '../views/EmployeeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: EmployeeView
    },
    {
      path: '/form',
      name: 'form',
     
      component: () => import('../views/FormView.vue')
    },
    {
      path: '/employeeview',
      name: 'employeeview',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/EmployeeView.vue')
    },
    {
      path: '/:id',
      name: 'EditEmployee',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/EditViews.vue')
    }
  ]
})

export default router
