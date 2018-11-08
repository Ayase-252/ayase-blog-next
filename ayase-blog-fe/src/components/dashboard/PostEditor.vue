<template>
  <dash-board-content>
    <template slot="breadcrumb">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item to="/dashboard">Dashboard</el-breadcrumb-item>
        <el-breadcrumb-item>New Post</el-breadcrumb-item>
      </el-breadcrumb>
    </template>
    <template slot="content">
      <div class="post-editor-form-wrapper">
        <el-form label-width="50px" :rules="formRules" :model="post">
          <el-form-item label="Title" prop="title">
            <el-input v-model="post.title"></el-input>
          </el-form-item>
          <el-form-item label="Link" prop="link">
            <el-input v-model="post.link"></el-input>
          </el-form-item>
          <el-form-item label="Tags">
            <el-input v-model="post.tags"></el-input>
          </el-form-item>
          <el-form-item>
            <mavon-editor v-model="post.content"></mavon-editor>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">Submit</el-button>
            <el-button type="danger" @click="onReset">Reset</el-button>
          </el-form-item>
        </el-form>
      </div>
    </template>
  </dash-board-content>
</template>

<script>
import MavonEditor from 'mavon-editor'
import DashBoardContent from './DashBoardContent'
import apiClient from 'api-client'
import 'mavon-editor/dist/css/index.css'

export default {
  data () {
    return {
      post: {
        title: '',
        link: '',
        tags: '',
        content: ''
      },
      formRules: {
        title: { required: true, message: 'Title cannot be empty', trigger: 'blur' },
        link: { required: true, message: 'Link cannot be empty', trigger: 'blur' }
      }
    }
  },
  components: {
    MavonEditor: MavonEditor.mavonEditor,
    DashBoardContent
  },
  methods: {
    onSubmit () {
      apiClient.PageAPI.postNewPage(this.post).then(() => {
        this.$message({
          message: 'Success',
          type: 'success'
        })
      }).catch((err) => {
        this.$message({
          message: err,
          type: 'error'
        })
      })
    },
    onReset () {
      Object.assign(this.post, this.$options.data().post)
    }
  }
}
</script>

<style lang="less">
</style>
