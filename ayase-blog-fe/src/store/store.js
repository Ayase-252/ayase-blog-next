import Vuex from 'vuex'
import PageModule from './modules/page'

const store = new Vuex({
  modules: {
    page: PageModule
  }
})

export default store