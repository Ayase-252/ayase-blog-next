import PageApi from '@/api/page_api'
import ajax from '@/api/ajax'

export const PageModule = {
  namespaced: true,
  state: {
    pageList: [],
    curPage: {},
    noMorePage: false,
    nextPostsUrl: 'posts/'
  },
  mutations: {
    addPageToList (state, page) {
      state.pageList.push(page)
    },
    setPageAsCurPage (state, curPage) {
      state.curPage = curPage
    },
    setNextPageIdx (state, idx) {
      state.nextPageIdx = idx
    },
    setNoMorePage (state, val) {
      state.noMorePage = val
    },
    setNextPostsUrl (state, val) {
      state.nextPostsUrl = val
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
      if (context.state.nextPostsUrl !== '') {
        ajax.get(context.state.nextPostsUrl)
          .then(res => {
            context.commit('setNextPostsUrl', res.data.next || '')
            for (const post of res.data.results) {
              context.commit('addPageToList', post)
            }
          })
          .catch(err => {
            console.log(err)
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
