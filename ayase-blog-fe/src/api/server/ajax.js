import axios from 'axios'

const baseURL = process.env.NODE_ENV === 'development' ? 'http://localhost:8100/api' : '/api'

const axiosInstance = axios.create({
  baseURL,
  headers: {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json'
  }
})

export default axiosInstance
