import Vue from 'vue'
import Router from 'vue-router'
import Farmers from '@/components/Farmers'
import Farms from '@/components/Farms'
import Harvests from '@/components/Harvests'
import Login from '@/components/Login'
import Dashboard from '@/components/Dashboard'
Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Farmers',
      component: Farmers,
      meta: { requiresAuth: true },
    },
    {
      path: '/farms',
      name: 'Farms',
      component: Farms,
      meta: { requiresAuth: true },
    },
    {
      path: '/harvests',
      name: 'Harvests',
      component: Harvests,
      meta: { requiresAuth: true },
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: { requiresAuth: false },
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      meta: { requiresAuth: true },
    },
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (window.localStorage.getItem('token') == null) {
      next({ name: 'Login' });
    } else {
      next();
    }
  } else if (window.localStorage.getItem('token') != null) {
    next({ name: 'Farmers' });
  } else {
    next();
  }
});

export default router;