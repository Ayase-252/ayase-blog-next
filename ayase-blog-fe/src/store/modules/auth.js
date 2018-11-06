// import ajax from '@/api/ajax'
import apiClient from 'api-client'

const AuthAPI = apiClient.AuthAPI

export const AuthModule = {
  namespaced: true,
  state: {
    isLoggedIn: false,
    sessionId: '',
    userInfo: {}
  },
  mutations: {
    setUserLoggedIn (state, { userInfo, sessionId }) {
      state.isLoggedIn = true
      state.userInfo = userInfo
      state.sessionId = sessionId
    }
  },
  actions: {
    async validateExistingSession (ctx) {
      const session = JSON.parse(window.localStorage.getItem('session'))
      if (!session) {
        throw 'Session does not exist'
      }
      if (session.expiredAt < Date.now()) {
        window.localStorage.removeItem('session')
        throw 'Session is expired'
      }
      try {
        const userInfo = await AuthAPI.ValidateSession(session.sessionId)
        ctx.commit('setUserLoggedIn', userInfo)
      } catch (err) {
        throw err
      }
    },
    async login (ctx, { username, password }) {
      try {
        const { userInfo, session } = await AuthAPI.AuthenticateUser(
          username,
          password
        )
        window.localStorage.setItem('session', JSON.stringify(session))
        ctx.commit('setUserLoggedIn', { userInfo, sessionId: session.sessionId })
      } catch (err) {
        throw err
      }
    }
  }
}
