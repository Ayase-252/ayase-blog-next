<template>
  <div class="content" v-html="content"></div>
</template>

<script>
export default {
  props: {
    content: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang='less'>
.content {
  font-size: 1.25em;
  font-family: Georigiam, Times, KaiTi, STKaiTi, serif;
  color: #444; // Post Style Specification
  & > *:first-child {
    margin-top: 0;
  }
  & > *:last-child {
    margin-bottom: 0;
  }
  p,
  blockquote,
  ul,
  ol,
  address,
  dl,
  pre {
    line-height: 1.6em;
    margin-bottom: 1.3em;
  }
  pre,
  code {
    font-family: Consolas, Monaco, monospace;
  }
  hr {
    display: block;
    width: 96px;
    height: 3px;
    background-color: #ddd;
    margin: 40px auto;
    border: none;
  }
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-family: "Microsoft Yahei", sans-serif;
    margin: 50px 0 20px;
    line-height: 1.2em;
    font-weight: 700;
    color: #333;
  }
  h1 {
    font-size: 1.75em;
  }
  h2 {
    font-size: 1.5em;
  }
  h3 {
    font-size: 1.25em;
  }
  h4 {
    font-size: 1.1em;
    font-weight: 400;
  }
  h5 {
    font-size: 1em;
    font-weight: 400;
  }
  h6 {
    font-size: 0.8em;
    font-weight: 700;
    color: #666;
    margin-bottom: 10px;
  }
  blockquote {
    padding: 30px 30px 30px 90px;
    background-color: #f6f6f6f;
    position: relative;
    p {
      color: #666;
      font-style: italic;
    }
    cite {
      font-family: "Microsoft Yahei", "MS Gothic", sans-serif;
      font-size: 0.9rem;
      font-weight: 700;
      line-height: 1.2em;
      letter-spacing: 1px;
      &::before {
        content: "-";
      }
    }
    &::before {
      content: "”";
      display: block;
      width: 90px;
      font-family: Georigiam, Times, KaiTi, STKaiTi, serif;
      font-size: 72px;
      font-weight: 700;
      color: #aaa;
      text-align: center;
      position: absolute;
      top: 32px;
      left: 0;
    }
  }
  ul,
  ol {
    margin-left: 2em;
  }
  li {
    margin-bottom: 0.75em;
  }
  ol {
    list-style: decimal;
    & & {
      list-style: lower-alpha;
    }
  }
  ul {
    list-style: disc;
    & & {
      list-style: circle;
    }
  }
  table {
    border-collapse: collapse;
    border-spacing: 0;
    empty-cells: show;
    font-family: "Microsoft Yahei", sans-serif;
    font-size: 0.95rem;
    width: 100%;
    tr:nth-child(2n + 3) {
      background: #f6f6f6;
    }
  }
  th,
  td {
    padding: 2%;
    margin: 0;
    overflow: visible;
    line-height: 120%;
    border-bottom: 1px solid #eee;
  }
  th {
    font-size: 1rem;
    font-weight: 700;
  }
  code {
    font-size: 14px;
    line-height: 1.2em;
    position: relative;
  }
  li > code,
  p > code {
    background: rgba(0, 0, 0, 0.04);
    color: #333;
    border-radius: 2px;
  }
  a {
    text-decoration: underline;
  }
}
</style>
