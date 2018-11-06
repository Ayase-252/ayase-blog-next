<template>
  <div>
    Hello, welcome back {{ userInfo.username }}.
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  computed: {
    ...mapState('auth', [
      'userInfo'
    ])
  }
}
</script>

<style>

</style>
