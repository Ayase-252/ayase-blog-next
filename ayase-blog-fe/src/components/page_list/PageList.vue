<template>
  <div ref="pageListWrapper" v-on:scroll="onScroll">
    <loading :active.sync="isLoading" :is-full-page="true"></loading>
    <page-item v-for="page in pageList" v-bind:key="page.link" v-bind="page"></page-item>
    <p class="page-list-no-more" v-if="noMorePage"> ~~ No more page ~~</p>
  </div>
</template>

<script>
import PageItem from './PageItem'
import { mapState, mapActions } from 'vuex'
import Loading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/vue-loading.css'
import _ from 'lodash'

export default {
  data: function () {
    return {
      isLoading: true
    }
  },
  computed: {
    ...mapState('page', ['pageList', 'noMorePage'])
  },
  components: {
    PageItem, Loading
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
    this.getMorePage().then(() => {
      this.isLoading = false
    })
  }
}
</script>

<style lang="less">
.page-list-no-more {
  background-color: #FFF;
  padding: 30px;
  text-align: center;
}
</style>
