<template>
<div class="base-page-header-wrapper">
  <time>{{ time }}</time>
  <h2>{{ title }}</h2>
</div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: ''
    },
    time: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="less">
time {
  font-size: 0.9em;
  font-weight: 700;
  color: #999
}

h2 {
  font-size: 1.5em;
  margin-bottom: 10px;
}

.base-page-header-wrapper {
  border-bottom: 2px solid rgba(170, 170, 170, 0.4);
}
</style>
