import apiClient from 'api-client'

export const PageModule = {
  namespaced: true,
  state: {
    pageList: [],
    curPage: {},
    noMorePage: false,
    nextPostsUrl: 'posts/'
  },
  mutations: {
    addPagesToList (state, pages) {
      state.pageList.push(...pages)
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
    },
  },
  actions: {
    async getMorePage (ctx, payload) {
      try {
        const posts = ctx.state.pageList
        let morePosts;
        if(posts.length){
          const linkOfLastPage = posts[posts.length - 1].link
          morePosts = await apiClient.getPagesByLastLink(linkOfLastPage, 10)
        } else {
          morePosts = await apiClient.getPages(10)
        }
        if(!morePosts.length) {
          ctx.commit('setNoMorePage', true)
        } else {
          ctx.commit('addPagesToList', morePosts)
        }
      } catch (err) {
        console.log(err)
      }
    },
    setCurrPage (context, payload) {
      context.commit('setPageAsCurPage', {
        curPage: payload.curPage
      })
    }
  }
}
