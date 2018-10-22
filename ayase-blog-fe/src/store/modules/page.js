import PageApi from '@/api/page_api'

export const PageModule = {
  namespaced: true,
  state: {
    pageList: [],
    curPage: {},
    nextPageIdx: null,
    noMorePage: false
  },
  mutations: {
    addPageToList (state, payload) {
      state.pageList.push(payload.page)
    },
    setPageAsCurPage (state, payload) {
      state.curPage = payload.curPage
    },
    setNextPageIdx (state, idx) {
      state.nextPageIdx = idx
    },
    setNoMorePage (state, val) {
      state.noMorePage = val
    }
  },
  actions: {
    getPage (context, payload) {
      PageApi.requestPage(context.state.nextPageIdx)
        .then(res => {
          context.commit('addPageToList', {
            page: {
              title: res.data.title,
              postId: res.data.postId,
              content: res.data.content,
              pubTime: res.data.pub_time
            }
          })
          context.commit('setNextPageIdx', res.data.postId - 1)
        })
        .catch(error => {
          payload.onError(error)
        })
    },
    getMorePage (context, payload) {
      const pageLimit = payload && payload.hasOwnProperty('pageLimit') ? payload.pageLimit : 3
      if (!context.state.noMorePage) {
        PageApi.requestMorePage(context.state.nextPageIdx, pageLimit)
          .then(res => {
            const numPages = res.data.numPages
            let nextPageIdx = 0
            for (let i = 0; i < numPages; i++) {
              const page = res.data.pages[i]
              console.log(page.postId)
              context.commit('addPageToList', {
                page
              })
              nextPageIdx = page.postId - 1
            }
            context.commit('setNextPageIdx', nextPageIdx)
            if (pageLimit !== numPages || nextPageIdx === 0) {
              context.commit('setNoMorePage', true)
            }
          })
      }
    },
    setCurrPage (context, payload) {
      context.commit('setPageAsCurPage', {
        curPage: payload.curPage
      })
    }
  }
}
