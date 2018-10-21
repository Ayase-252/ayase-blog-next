<template>
<div id="page-list">
  <page-item v-for="(page, idx) in pages" v-bind:key="idx" v-bind="page"></page-item>
</div>
</template>

<script>
import PageItem from './PageItem'
export default {
  data: function () {
    return {
      pages: [{
        title: 'Hello world',
        content: 'Hello world TOOOO'
      }]
    }
  },
  components: {
    PageItem
  }
}
</script>

<style lang="less" scoped>
#page-list {
  padding: 30px 8% 0 8%;
}
</style>
