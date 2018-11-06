<template>
  <div>
    <el-row class="dashboard-content-breadcrumb">
      <slot name="breadcrumb"></slot>
    </el-row>
    <div class="dashboard-content-wrapper">
      <slot name="content"></slot>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less">
.dashboard-content-breadcrumb {
  margin: 20px 0;
  padding: 0 0 15px 0;
  border-bottom: 1px solid #777;
}

.dashboard-content-wrapper {
  padding: 0 25px;
}
</style>
