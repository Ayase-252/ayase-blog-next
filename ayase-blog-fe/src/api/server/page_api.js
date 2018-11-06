import ajax from './ajax'

export default class PageApi {
  static requestPage (pageIdx) {
    return ajax.get(`post/${pageIdx}`)
  }

  static requestMorePage (nextPageIdx, maxPages) {
    const params = {}
    if (nextPageIdx > 0) {
      params.from = nextPageIdx
    }
    if (maxPages) {
      params.maxPages = maxPages
    }
    return ajax.get('posts', {
      params
    })
  }
}
