const postMock = require('./data/posts.json')
import { delay } from './utils'

function getPagesByLastLink (fromLink, numPages) {
  return delay((resolve, reject) => {
    const idx = postMock.findIndex(post => {
      return post.link === fromLink
    })
    resolve(postMock.slice(idx + 1, idx + 1 + numPages))
  }, 1000)
}

function getPageByLink(link) {
  return delay((resolve, reject) => {
    const selected = postMock.find(post => {
      return post.link === link
    })
    resolve(selected)
  }, 500)
}

function getPages (numPages) {
  return delay((resolve, reject) => {
    resolve(postMock.slice(0, numPages))
  }, 500)
}

const PageAPI = {
  getPagesByLastLink,
  getPages,
  getPageByLink
}

export default PageAPI
