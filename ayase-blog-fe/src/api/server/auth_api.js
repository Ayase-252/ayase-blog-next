import ajax from './ajax'

async function authenticateUser (username, password) {
  try {
    await ajax.post('/sessions/', {
      username,
      password,
      duration: 3600
    }, {
      withCredentials: true
    })
  } catch (err) {
    throw err
  }
}

async function validateSession (sessionId) {
  try {
    const res = await ajax.get('/sessions/', {
      withCredentials: true
    })
    return res.data
  } catch (err) {
    throw err
  }
}

const AuthAPI = {
  authenticateUser,
  validateSession
}

export default AuthAPI
