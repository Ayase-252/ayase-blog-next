import Vue from 'vue'
import Router from 'vue-router'
const Layout = () => import('@/components/Layout')
const PageList = () => import('@/components/page_list/PageList')
const PageDisplay = () => import('@/components/page_display/PageDisplay')
const AdminLogin = () => import('@/components/admin_login/AdminLogin')
const DashBoard = () => import('@/components/dashboard/DashBoard')
import PostEditor from '@/components/dashboard/PostEditor'
import store from '../store'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Layout,
      children: [
        {
          path: '',
          name: 'homepage',
          component: PageList,
          meta: {
            title: 'Ayase-blog'
          }
        },
        {
          path: 'posts/:postLink',
          name: 'postview',
          component: PageDisplay,
          props: true,
          meta: {
            title: 'Post | Ayase-blog'
          }
        }
      ]
    },
    {
      path: '/login/',
      component: AdminLogin,
      meta: {
        title: 'Login | Ayase-blog'
      }
    },
    {
      path: '/dashboard/',
      component: DashBoard,
      meta: {
        requireLogin: true,
        title: 'Dashboard | Ayase-blog'
      },
      children: [{
        path: 'post',
        component: PostEditor,
        meta: {
          title: 'New Post | Ayase-blog'
        }
      }]
    }
  ]
})

// Redirect to /login/ if attempts to load sensitive page
router.beforeEach((to, from, next) => {
  if (
    to.matched.some(record => record.meta.requireLogin) &&
    !store.state.auth.isLoggedIn
  ) {
    next('/login/')
  } else {
    next()
  }
})

// Modify title according to value specified in meta of route
router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})

export default router
