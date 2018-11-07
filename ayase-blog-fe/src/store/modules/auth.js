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
    setUserLoggedIn (state, { userInfo }) {
      state.isLoggedIn = true
      state.userInfo = userInfo
    }
  },
  actions: {
    async validateExistingSession (ctx) {
      try {
        const userInfo = await AuthAPI.validateSession()
        ctx.commit('setUserLoggedIn', userInfo)
      } catch (err) {
        console.log(err)
        throw err
      }
    },
    async login (ctx, { username, password }) {
      try {
        await AuthAPI.authenticateUser(username, password)
        ctx.commit('setUserLoggedIn', {
          userInfo: {
            username
          }
        })
      } catch (err) {
        throw err
      }
    }
  }
}
