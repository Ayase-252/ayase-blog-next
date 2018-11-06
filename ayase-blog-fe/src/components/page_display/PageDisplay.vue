<template>
  <div>
    <article class="page-display" v-dynamic-title="`${title} | Ayase-blog`">
      <base-page-header v-bind="{time: selectedPage.createdAt, title: selectedPage.title}"></base-page-header>
      <base-page-content v-bind:content="selectedPage.content"></base-page-content>
    </article>
  </div>
</template>

<script>
import BasePageContent from '../base_components/BasePageContent'
import BasePageHeader from '../base_components/BasePageHeader'
import { mapState } from 'vuex'

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
    selectedPage () {
      console.log(this.pageList)
      return this.pageList.find((post) => {
        return post.link === this.postLink
      })
    },
    ...mapState('page', ['pageList'])
  }
}
</script>

<style lang="less">
.page-display {
  background-color: #fff;
  padding: 64px;
}
</style>
