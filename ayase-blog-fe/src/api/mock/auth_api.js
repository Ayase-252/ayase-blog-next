const users = require('./data/account.json')
const sessions = require('./data/session.json')
import { delay } from './utils'

function AuthenticateUser(username, password) {
  return delay((resolve, reject) => {
    if (users.findIndex((user) => {
      return user.username === username && user.password === password
    }) !== -1) {
      resolve({
        username
      })
    } else {
      reject('Authentication Error')
    }
  }, 1000)
}

function ValidateSession(sessionId) {
  return delay((resolve, reject) => {
    const sessionIdx = sessions.findIndex((session) => {
      return session.sessionId === sessionId
    })
    if(sessionIdx === -1) {
      reject('Session Validation Fail')
    } else {
      resolve(sessions[sessionIdx])
    }
  }, 1500)
}

const AuthAPI = {
  AuthenticateUser
}

export default AuthAPI
