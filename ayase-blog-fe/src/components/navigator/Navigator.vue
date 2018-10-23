<template>
<nav id="navigator">
    <navi-header v-bind:navItems="navItems"></navi-header>
    <footer> Powered by django<br>Theme adopted from Rams<br> Copyright 2016 Ayase-252 </footer>
</nav>
</template>

<script>
import NaviHeader from './NaviHeader'
export default {
  data: function () {
    return {
      navItems: [{
        name: 'Hello world',
        link: '/hello/'
      }]
    }
  },
  components: {
    NaviHeader
  }
}
</script>

<style lang="less">
@import '../../styles/variables.less';

nav {
  font-family: "Microsoft Yahei", Tahoma, Geneva, sans-serif;
  background-color: @main-color;
}

footer {
  position: absolute;
  bottom: 50px;
  right: 30px;
  font-size: 0.8em;
  color: rgba(255, 255, 255, 0.4)
}
</style>
