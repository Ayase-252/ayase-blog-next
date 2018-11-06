import apiClient from 'api-client'

export const PageModule = {
  namespaced: true,
  state: {
    pageList: [],
    noMorePage: false,
    pageUnderViewing: {}
  },
  mutations: {
    addPagesToList (state, pages) {
      state.pageList.push(...pages)
    },
    setNoMorePage (state, val) {
      state.noMorePage = val
    },
    setPageUnderView (state, page) {
      state.pageUnderViewing = page
    }
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
    
    async setPageUnderView (ctx, link) {
      const posts = ctx.state.pageList
      let selectedPost = posts.find((post) => {
        return post.link === link
      })
      import('lodash').then(async (_) => {
        if(_.isEmpty(selectedPost)) {
          try {
            selectedPost = await apiClient.getPageByLink(link)
          } catch (err) {
            console.log(err)
          }
        }
        ctx.commit('setPageUnderView', selectedPost)
      })
    }
  }
}
