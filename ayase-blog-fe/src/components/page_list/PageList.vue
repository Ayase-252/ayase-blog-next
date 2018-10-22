<template>
  <div ref="pageListWrapper" v-on:scroll="onScroll">
    <page-item v-for="(page, idx) in pageList" v-bind:key="idx" v-bind="page"></page-item>
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
    ...mapState('page', ['pageList'])
  },
  components: {
    PageItem
  },
  methods: {
    ...mapActions('page', [
      'getMorePage'
    ]),
    debouncedScrollHandler: _.debounce(function () {
      const scrollTop = this.$refs.pageListWrapper.scrollTop
      const clientHeight = this.$refs.pageListWrapper.clientHeight
      const scrollHeight = this.$refs.pageListWrapper.scrollHeight
      if (scrollHeight - (scrollTop + clientHeight) < 50) {
        this.getMorePage({
          onError (err) {
            console.log(err)
          }
        })
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
