import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: '',
    component: Home,
    children: [
      {
        path: "inventory",
        name: "inventory",
        component: () =>
          import(
            "../pages/Inventory/Inventory.vue"
          )
      }
    ]
  },
  {
    path: '/navigation',
    name: 'Navigation',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "navigation" */ '../views/Navigation.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
