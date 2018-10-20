<template>
  <article>
    <h2>Hello world</h2>
    <page-display v-bind:content="content"></page-display>
  </article>
</template>

<script>
import PageDisplay from './PageDisplay'
import {PageApi} from '@/api/page_api'

export default {
  data: function () {
    return {
      title: 'Default',
      content: ''
    }
  },
  props: {
    postId: {
      type: String
    }
  },
  components: {
    PageDisplay
  },
  watch: {
    title(olderValue, newValue) {
      document.title = this.title
    }
  },
  created () {
    const vm = this
    document.title = this.title
    PageApi.requestPage(1).then(function (res) {
      vm.title = res.data.title
      vm.content = res.data.content
    }).catch(function (err) {
      console.log(err)
    })
  }
}
</script>

<style lang="less">
article {
  background-color: #fff;
  padding: 64px;
}

h2 {
  font-size: 1.5em;
}
</style>


