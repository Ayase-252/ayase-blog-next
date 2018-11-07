<template>
  <el-container class="dashboard-wrapper">
    <el-header class="dashboard-header"></el-header>
    <el-container>
      <el-aside class="dashboard-nav">
        <el-menu :router="true">
          <el-submenu index=1>
            <template slot="title">
              <span>Post Management</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/dashboard/post">Write New Post</el-menu-item>
              <el-menu-item index="1-2" disabled>Manage Post</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      listItem: [{
        label: 'Post Management',
        children: [{
          label: 'New Post'
        }, {
          label: 'Manage Posts'
        }]
      }]
    }
  }
}
</script>

<style lang="less">
@main-color: #409EFF;

.dashboard-wrapper {
  height: 100vh;
}

.dashboard-nav {
  width: 250px;
  padding: 10px 0 0 20px;
  border-right: 1px solid #777;
}

.dashboard-header {
  background: @main-color;
}
</style>
