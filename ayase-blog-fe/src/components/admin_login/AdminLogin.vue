<template>
  <el-container class="admin-login-box">
    <el-form class="admin-login-form" label-width="80px" :model="loginForm">
      <el-form-item label="Username">
        <el-input placeholder="Username" v-model="loginForm.username"></el-input>
      </el-form-item>
      <el-form-item label="Password">
        <el-input type="password" placeholder="Password" v-model="loginForm.password"></el-input>
      </el-form-item>
      <el-button type="primary" @click="submit">Login</el-button>
      <el-button @click="resetForm">Reset</el-button>
    </el-form>
  </el-container>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    resetForm () {
      this.loginForm.username = ''
      this.loginForm.password = ''
    },
    submit () {
      axios.post('http://localhost:8100/api/sessions/', {
        username: this.loginForm.username,
        password: this.loginForm.password,
        duration: 3600
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((res) => {
          console.log('LOGGED IN')
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang='less'>
.admin-login-box {
  width: 100vw;
  height: 100vh;
  background-color: #ccc;
  justify-content: center;
  align-items: center;
}

.admin-login-form {
  padding: 50px;
  background-color: #fff;
}
</style>
