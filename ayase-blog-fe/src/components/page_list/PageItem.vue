<template>
<article class="page-item">
    <base-page-header v-bind="{title, date}"></base-page-header>
    <base-page-content v-bind:content="first_paragraph"></base-page-content>
    <router-link class="post-btn page-item-footer" v-bind:to="{ name: 'postview', params: {postLink: link}}">Read More</router-link>
</article>
</template>

<script>
import BasePageContent from '../base_components/BasePageContent'
import BasePageHeader from '../base_components/BasePageHeader'

export default {
  data: function () {
    return {}
  },
  props: {
    date: {
      type: String,
      default: '2008-1-1 10:00'
    },
    title: {
      type: String,
      default: ''
    },
    content: {
      type: String,
      default: ''
    },
    link: {
      type: String,
      default: ''
    }
  },
  computed: {
    first_paragraph () {
      const firstP = this.content.match(/^(<p>.*?<\/p>)/)
      return (firstP && firstP[0]) || this.content
    }
  },
  components: {
    BasePageHeader, BasePageContent
  }
}
</script>

<style lang="less">
@import '../../styles/common.less';

.page-item {
  background-color: #fff;
  padding: 64px;
  margin-bottom: 30px;
}

.page-item-footer {
  margin-top: 30px;
}

</style>
