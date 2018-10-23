import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/components/Layout'
import PageList from '@/components/page_list/PageList'
import PageDisplay from '@/components/page_display/PageDisplay'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Layout,
      children: [{
        path: '',
        name: 'homepage',
        component: PageList
      }, {
        path: 'post/:postId',
        name: 'postview',
        component: PageDisplay,
        props (route) {
          const props = {...route.params}
          props.postId = parseInt(props.postId)
          return props
        }
      }]
    }
  ]
})
