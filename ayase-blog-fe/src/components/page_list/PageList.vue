<template>
  <div ref="pageListWrapper" v-on:scroll="onScroll" v-dynamic-title="`Ayase-blog`">
    <page-item v-for="page in pageList" v-bind:key="page.link" v-bind="page"></page-item>
    <p v-if="noMorePage"> ~~ No more page ~~</p>
  </div>
</template>

<script>
import PageItem from './PageItem'
import { mapState, mapActions } from 'vuex'
import _ from 'lodash'

export default {
  data: function () {
    return {
    }
  },
  computed: {
    ...mapState('page', ['pageList', 'noMorePage'])
  },
  components: {
    PageItem
  },
  methods: {
    ...mapActions('page', [
      'getMorePage'
    ]),
    debouncedScrollHandler: _.debounce(function () {
      const pageListWrapper = this.$refs.pageListWrapper
      const scrollTop = pageListWrapper.scrollTop
      const clientHeight = pageListWrapper.clientHeight
      const scrollHeight = pageListWrapper.scrollHeight
      if (scrollHeight - (scrollTop + clientHeight) < 50) {
        this.getMorePage()
      }
    }, 500),
    onScroll (event) {
      this.debouncedScrollHandler()
    }
  },
  created () {
    this.getMorePage()
  }
}
</script>

<style lang="less">
</style>
