function getPagesByLastLink (fromLink, numPages) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const idx = postMock.findIndex(post => {
        return post.link === fromLink
      })
      resolve(postMock.slice(idx + 1, idx + 1 + numPages))
    }, 500)
  })
}

function getPageByLink(link) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const selected = postMock.find(post => {
        return post.link === link
      })
      resolve(selected)
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
  getPages,
  getPageByLink
}
