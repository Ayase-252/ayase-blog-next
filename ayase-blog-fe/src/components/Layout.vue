<template>
  <div class="wrapper">
    <navigator class="left-flex-elem"></navigator>
    <div class="right-flex-elem content-wrapper">
        <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Navigator from './navigator/Navigator'
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

<style lang="less">
@import '~styles/reset.less';
@import '~styles/variables.less';

.wrapper {
  width: 100%;
  display: flex;
  flex-flow: row nowrap;
  background-color: @bg-color;
  height: 100vh;
}

.left-flex-elem {
  flex: 0 0 300px;
}

.right-flex-elem {
  flex: 1 1;
  overflow: auto;
}

.content-wrapper {
  padding: 30px 8% 0 8%;
}

@media (max-width: 1200px) {
  .content-wrapper {
    padding: 0;
  }
}

@media (max-width: @mobile-width) {
  .wrapper {
    flex-flow: column nowrap;
  }

  .left-flex-elem {
    height: 50px;
    flex: 0;
  }
}
</style>
