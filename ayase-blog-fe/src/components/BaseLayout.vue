<template>
  <div class="wrapper">
    <navigator></navigator>
    <div class="content-wrapper">
      <div class="content-inner-wrapper">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import Navigator from './Navigator'
export default {
  data: function () {
    return {
    }
  },
  methods: {

  },
  components: {
    Navigator
  }
}
</script>

<style lang="less" scoped>
@import '~styles/reset.less';
@import '~styles/variables.less';

.wrapper {
  width: 100%;
  background-color: @bg-color;
}

.content-wrapper {
  margin: 0 0 0 300px;
  min-height: 100vh;
}

.content-inner-wrapper {
  width: 880px;
  max-width: 84%;
  margin: 0 auto;
  padding-top: @content-to-top;
}
</style>
