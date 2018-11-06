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
import { mapActions } from 'vuex'

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
      const { username, password } = this.loginForm
      this.login({ username, password }).then(() => {
        this.$router.replace('/dashboard/')
      }).catch((err) => {
        this.$message.error('Username or password is wrong. Please check ~')
      })
    },
    ...mapActions('auth', [
      'login'
    ])
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
