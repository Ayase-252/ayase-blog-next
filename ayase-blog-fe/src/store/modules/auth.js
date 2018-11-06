// import ajax from '@/api/ajax'

export const AuthModule = {
  namespaced: true,
  state: {
    isLoggedIn: false
  },
//   mutations: {
//     setLoggedIn(state) {
//       state.isLoggedIn = true
//     }
//   },
//   actions: {
//     checkSession(ctx, payload) {
//       ajax.get('/api/sessions/')
//         .then( res => {
//           ctx.commit('setLoggedIn')
//         })
//         .catch( err => {
//           console.log('session invalid')
//         })
//     }
//   }
}
