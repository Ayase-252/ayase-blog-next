import ajax from './ajax'

async function getPages (numPages) {
  try {
    const res = await ajax.get('/posts/')
    return res.data
  } catch (err) {
    throw err
  }
}

async function getPageByLink (link) {
  try {
    const res = await ajax.get('/posts/link')
    return res.data
  } catch (err) {
    throw err
  }
}

async function getPagesByLastLink (fromLink, numPages) {
  try {
    const res = await ajax.get('/posts/link', {
      params: {
        from: fromLink,
        maxPages: numPages
      }
    })
    return res.data
  } catch (err) {
    throw err
  }
}

const PageAPI = {
  getPagesByLastLink,
  getPages,
  getPageByLink
}

export default PageAPI
