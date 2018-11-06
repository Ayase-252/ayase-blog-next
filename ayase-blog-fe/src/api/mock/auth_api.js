const users = require('./data/account.json')
const sessions = require('./data/session.json')
import { delay } from './utils'

function AuthenticateUser(username, password) {
  return delay((resolve, reject) => {
    const userIdx = users.findIndex((user) => {
      return user.username === username && user.password === password
    })
    if (userIdx !== -1){
      const user = users[userIdx]
      resolve({
        userInfo: {
          username: user.username,
        },
        session: {
          sessionId: user.sessionId,
          expiredAt: Date.now().valueOf() + 3600 * 1000
        }
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
  AuthenticateUser,
  ValidateSession
}

export default AuthAPI
