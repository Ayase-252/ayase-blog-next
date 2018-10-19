<template>
  <div class="wrapper">
    <navigator class="left-flex-elem"></navigator>
    <div class="right-flex-elem">
        <router-view></router-view>
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
  display: flex;
  flex-flow: row nowrap;
  background-color: @bg-color;
  min-height: 100vh;
}

.left-flex-elem {
  flex: 0 0 300px;
}

.right-flex-elem {
  flex: 1 1;
}

@media (max-width: 768px) {
  .wrapper {
    flex-flow: column nowrap;
  }

  .left-flex-elem {
    height: 50px;
    flex: 0;
  }
}
</style>
