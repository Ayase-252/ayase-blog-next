import Vue from 'vue'
import Vuex from 'vuex'
import { PageModule } from './modules/page'
import { AuthModule } from './modules/auth'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    page: PageModule,
    auth: AuthModule
  }
})

export default store
