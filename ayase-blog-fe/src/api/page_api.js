import ajax from './ajax'

export default class PageApi {
  static requestPage (pageIdx) {
    return ajax.get(`post/${pageIdx}/`)
  }

  static requestMorePage (lastPageIdx, numPage) {
    const params = {}
    if (lastPageIdx !== 0) {
      params.from = lastPageIdx
    }
    if (!numPage) {
      params.max_page = numPage
    }
    return ajax.get('posts', {
      params
    })
  }
}
