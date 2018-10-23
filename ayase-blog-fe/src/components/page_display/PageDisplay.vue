<template>
  <div>
    <article class="page-display" v-dynamic-title="`${title} | Ayase-blog`">
      <base-page-header v-bind="{time, title}"></base-page-header>
      <base-page-content v-bind:content="content"></base-page-content>
    </article>
  </div>
</template>

<script>
import BasePageContent from '../base_components/BasePageContent'
import BasePageHeader from '../base_components/BasePageHeader'
import PageApi from '../../api/page_api'

export default {
  data: function () {
    return {
      time: '',
      title: '',
      content: ''
    }
  },
  props: {
    postId: {
      type: Number
    }
  },
  components: {
    BasePageContent, BasePageHeader
  },
  created () {
    const vm = this
    PageApi.requestPage(this.postId).then(function (res) {
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
