<template>
<article>
    <time>{{ time }}</time>
    <h2>{{ title }}</h2>
    <page-display v-bind:content="content"></page-display>
    <router-link class="post-btn" v-bind:to="{ name: 'postview', params: {id: post_id}}">Read More</router-link>
</article>
</template>

<script>
import PageDisplay from './PageDisplay'
export default {
  data: function () {
    return {}
  },
  props: {
    time: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: ''
    },
    content: {
      type: String,
      default: ''
    },
    post_id: {
      type: Number,
      default: 1
    }
  },
  components: {
    PageDisplay
  }
}
</script>

<style lang="less" scoped>
time {
  font-size: 0.9em;
  font-weight: 700;
  margin-bottom: 10px;
  color: #999
}

h2 {
  margin-top: 0;
}

article {
  background-color: #fff;
  padding: 64px;
  margin-bottom: 30px;
}

.post-btn {
  padding: 15px 20px;
  text-decoration: none;
  background-color: #333;
  color: #fff;
  display: inline-block;
  font-size: 0.8em;
  transition: all 0.3s ease-in-out;

  &:hover {
    background-color: #6aa897;
  }
}
</style>
