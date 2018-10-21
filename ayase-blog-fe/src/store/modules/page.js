import PageApi from '@/api/page_api'

export const PageModule = {
  namespaced: true,
  privateState: {
    nextPageIdx: 0
  },
  state: {
    pageList: [],
    curPage: {}
  },
  mutations: {
    addPageToList (state, payload) {
      state.pageList.append(payload.page)
    },
    setPageAsCurPage (state, payload) {
      state.curPage = payload.curPage
    }
  },
  actions: {
    getMorePage (context, payload) {
      PageApi.requestPage(context.privateState.nextPageIdx)
        .then(res => {
          context.commit('addPageToList', {
            page: {
              title: res.data.title,
              postId: res.data.post_id,
              content: res.data.content,
              pubTime: res.data.pub_time
            }
          })
          context.privateState.nextPageIdx = res.data.post_id - 1 
        })
        .catch(error => {
          payload.onError(error)
        })
    },
    setCurrPage (context, payload) {
      context.commit('setPageAsCurPage', {
        curPage: payload.curPage
      })
    }
  }
}