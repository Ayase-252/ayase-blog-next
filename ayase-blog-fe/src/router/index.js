import Vue from 'vue'
import Router from 'vue-router'
import BaseLayout from '@/components/BaseLayout'
import PageList from '@/components/PageList'
import PageView from '@/components/PageView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: BaseLayout,
      children: [{
        path: '',
        component: PageList
      }, {
        path: 'post/:id',
        name: 'postview',
        component: PageView,
        props: true
      }]
    }
  ]
})
