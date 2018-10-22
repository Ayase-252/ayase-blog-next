<template>
  <div ref="pageListWrapper">
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
    debouncedScrollHandler: _.debounce(() => {
      const scrollTop = this.$ref.pageListWrapper.scrollTop
      const clientHeight = this.$ref.pageListWrapper.clientHeight
      const scrollHeight = this.$ref.pageListWrapper.scrollHeight
      if (scrollHeight - (scrollTop + clientHeight) < 50) {
        console.log('getMorePage is dispatched from scroll headler')
        this.getMorePage({
          onError (err) {
            console.log(err)
          }
        })
      }
    }, 500),
    onScroll () {
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
