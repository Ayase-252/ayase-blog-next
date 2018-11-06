// import ajax from '@/api/ajax'
import apiClient from 'api-client'

const AuthAPI = apiClient.AuthAPI

export const AuthModule = {
  namespaced: true,
  state: {
    isLoggedIn: false,
    userInfo: {}
  },
  mutations: {
    setUserLoggedIn(state, userInfo) {
      state.isLoggedIn = true
      state.userInfo = userInfo
    }
  },
  actions: {
    async login (ctx, { username, password }) {
      try {
        const userInfo = await AuthAPI.AuthenticateUser(username, password)
        console.log(userInfo)
        ctx.commit('setUserLoggedIn', userInfo)
      } catch (err) {
        throw err
      }
    }
  }
}
