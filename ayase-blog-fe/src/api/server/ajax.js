import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8100',
  headers: {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
})

export default axiosInstance
