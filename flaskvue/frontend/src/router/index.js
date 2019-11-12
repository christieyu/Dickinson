import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import Poems from '@/components/Poems'

const routerOptions = [
  { path: '/', component: 'HelloWorld' },
  { path: '/poems', component: 'Poems' }
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes
})
