<template>
  <div>
    <loading :active.sync="isLoading" :is-full-page="true"></loading>
    <article class="page-display">
      <base-page-header v-bind="{time: selectedPage.createdAt, title: selectedPage.title}"></base-page-header>
      <base-page-content v-bind:content="selectedPage.content"></base-page-content>
    </article>
  </div>
</template>

<script>
import BasePageContent from '../base_components/BasePageContent'
import BasePageHeader from '../base_components/BasePageHeader'
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import { mapState, mapActions } from 'vuex'

export default {
  data: function () {
    return {
      isLoading: true
    }
  },
  props: {
    postLink: {
      type: String
    }
  },
  components: {
    BasePageContent, BasePageHeader, Loading
  },
  computed: {
    ...mapState('page', {
      selectedPage: 'pageUnderViewing'
    })
  },
  methods: {
    ...mapActions('page', [
      'setPageUnderView'
    ])
  },
  created () {
    this.setPageUnderView(this.postLink).then((res) => {
      document.title = `${this.selectedPage.title} | Ayase-blog`
      this.isLoading = false
    })
  }
}
</script>

<style lang="less">
.page-display {
  background-color: #fff;
  padding: 64px;
}
</style>
