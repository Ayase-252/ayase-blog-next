import PageApi from'@/api/page_api'
import Page from '@/model/page'

export const PageModule = {
  privateState: {
    lastPageIdx: 1
  },
  state: {
    pageList: [],
    curPage: {}
  },
  mutations: {
    addPageToList(state, newPage) {
      state.pageList.append(newPage)
    },
    setPageAsCurPage(state, curPage) {
      state.curPage = curPage
    }
  },
  actions: {
    getMorePage(context) {
      PageApi.requestPage(context.privateState.lastPageIdx + 1).then(
        res => {
          const newPage = new Page(res.data)
          context.commit('addPageToList', newPage)
        }
      )
    }
  }
}