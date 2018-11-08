import { delay } from './utils'
import Cookies from 'js-cookie'
const users = require('./data/account.json')
const sessions = require('./data/session.json')

function authenticateUser (username, password) {
  return delay((resolve, reject) => {
    const userIdx = users.findIndex((user) => {
      return user.username === username && user.password === password
    })
    if (userIdx !== -1) {
      const user = users[userIdx]
      Cookies.set('sessionId', user.sessionId, { expiredAt: 1 })
      resolve({
        userInfo: {
          username: user.username
        }
      })
    } else {
      reject('Authentication Error')
    }
  }, 1000)
}

function validateSession () {
  return delay((resolve, reject) => {
    const sessionId = Cookies.get('sessionId')
    const sessionIdx = sessions.findIndex((session) => {
      return session.sessionId === sessionId
    })
    if (sessionIdx === -1) {
      reject('Session Validation Fail')
    } else {
      resolve(sessions[sessionIdx])
    }
  }, 1500)
}

const AuthAPI = {
  authenticateUser,
  validateSession
}

export default AuthAPI
