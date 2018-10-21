<template>
<div>
  <page-item v-for="(page, idx) in pages" v-bind:key="idx" v-bind="page"></page-item>
</div>
</template>

<script>
import PageItem from './PageItem'
import { mapState, mapActions } from 'vuex'
import _ from 'lodash'

export default {
  data: function () {
    return {
      // pages: [{
      //   title: 'Hello world',
      //   content: 'Hello world TOOOO'
      // }, {
      //   title: 'another post',
      //   content: 'hello'
      // }, {
      //   title: 'another post',
      //   content: 'hello'
      // }, {
      //   title: 'Ohhhhh NOOOOOOOO',
      //   content: 'hello'
      // }]
    }
  },
  computed: {
    ...mapState('page', ['pageList'])
  },
  components: {
    PageItem
  },
  methods: {
    ...mapActions('page', [
      'getMorePage'
    ]),
    onScroll () {
      
    }
  }
}
</script>

<style lang="less">
</style>
