const postMock = require('./data/posts.json')

function getPagesByLastLink (fromLink, numPages) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const idx = postMock.find(post => {
        return post.link === fromLink
      })
      resolve(postMock.slice(idx + 1, idx + 1 + numPages))
    }, 500)
  })
}

function getPages (numPages) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(postMock.slice(0, numPages))
    })
  }, 500)
}

export default {
  getPagesByLastLink,
  getPages
}
