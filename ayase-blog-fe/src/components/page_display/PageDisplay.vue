<template>
  <div>
    <article class="page-display" v-dynamic-title="title + ` | Ayase-blog`">
      <base-page-header v-bind="{time, title}"></base-page-header>
      <base-page-content v-bind:content="content"></base-page-content>
    </article>
  </div>
</template>

<script>
import BasePageContent from '../base_components/BasePageContent'
import BasePageHeader from '../base_components/BasePageHeader'
import PageApi from '@/api/page_api'

export default {
  data: function () {
    return {
      time: '2018-09-30 19:02',
      title: 'Default',
      content: '<p>Hello world <em>hello world</em><strong>Virtual DOM</strong></p>'
    }
  },
  props: {
    postId: {
      type: String
    }
  },
  components: {
    BasePageContent, BasePageHeader
  },
  created () {
    const vm = this
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
.page-display {
  background-color: #fff;
  padding: 64px;
}
</style>
