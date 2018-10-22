import Vue from 'vue'
import Vuex from 'vuex'
import { PageModule } from './modules/page'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    page: PageModule
  }
})

export default store
