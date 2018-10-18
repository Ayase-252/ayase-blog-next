<template>
  <div id="navigator">
    <h1><a href="#">{{title}}</a></h1>
    <ul>
      <li v-for="(navItem, idx) in navItems" v-bind:key="idx">
        <a v-bind:href="navItem.link">{{navItem.name}}</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    navItems: {
      type: Array,
      default: function () {
        return []
      }
    },
    title: {
      type: String,
      default: function () {
        return 'Ayase-blog'
      }
    }
  },
  data: function () {
    return {}
  }
}
</script>

<style lang="less" scoped>
#navigator {
  margin-top: 150px;
}

h1, ul {
  margin:0 25px;
}

h1 {
  text-align: right;
  font-size: 1.5em;
  line-height: 1;
  font-weight: 700;

  &::after {
    margin-top: 30px;
    content: "";
    display: block;
    height: 2px;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.2);
  }
}

ul {
  list-style: none;
}

li {
  margin-top: 20px;
  text-align: right;

  a {
    font-size: 0.9em;
    font-weight: 700;
    color: rgba(255, 255, 255, 0.6);
    transition: all 0.1s ease-in-out;
    &:hover {
      color: #fff;
    }
  }
}

a {
  text-decoration: none;
  color: #fff;
}
</style>
