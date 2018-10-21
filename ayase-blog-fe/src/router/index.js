import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/components/Layout'
import PageList from '@/components/page_list/PageList'
import PageDisplay from '@/components/page_display/PageDisplay'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: Layout,
      children: [{
        path: '',
        component: PageList
      }, {
        path: 'post/:id',
        name: 'postview',
        component: PageDisplay,
        props: true
      }]
    }
  ]
})
