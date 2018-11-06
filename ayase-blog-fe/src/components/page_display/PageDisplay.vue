<template>
  <div>
    <article class="page-display">
      <base-page-header v-bind="{time: selectedPage.createdAt, title: selectedPage.title}"></base-page-header>
      <base-page-content v-bind:content="selectedPage.content"></base-page-content>
    </article>
  </div>
</template>

<script>
import BasePageContent from '../base_components/BasePageContent'
import BasePageHeader from '../base_components/BasePageHeader'
import { mapState, mapActions } from 'vuex'

export default {
  data: function () {
    return {
      time: '',
      title: '',
      content: ''
    }
  },
  props: {
    postLink: {
      type: String
    }
  },
  components: {
    BasePageContent, BasePageHeader
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
    this.setPageUnderView(this.postLink).then(() => {
      document.title = `${this.selectedPage.title} | Ayase-blog`
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
