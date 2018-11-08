import ajax from './ajax'

async function getPages (numPages) {
  try {
    const res = await ajax.get('/posts/')
    return res.data.posts
  } catch (err) {
    throw err
  }
}

async function getPageByLink (link) {
  try {
    const res = await ajax.get(`/posts/${link}`)
    return res.data.posts
  } catch (err) {
    throw err
  }
}

async function getPagesByLastLink (fromLink, numPages) {
  try {
    const res = await ajax.get('/posts/', {
      params: {
        from: fromLink,
        maxPages: numPages
      }
    })
    return res.data.posts
  } catch (err) {
    throw err
  }
}


// Post: {
//   link: String
//   title: String,
//   content: String,
//   tags: String
// }
async function postNewPage (posts) {
  try {
    const res = await ajax.post('/posts', posts, {
      withCredentials: true
    })
  } catch (err) {
    throw err
  }
}

const PageAPI = {
  getPagesByLastLink,
  getPages,
  getPageByLink,
  postNewPage
}

export default PageAPI
