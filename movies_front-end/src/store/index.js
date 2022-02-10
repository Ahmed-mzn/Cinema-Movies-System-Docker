import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      id: 0,
      username: '',
      token: '',
      isAuthenticated : false
    },
  },
  mutations: {
    initializeStore(state) {
      if(localStorage.getItem('token')){
        state.user.token = localStorage.getItem('token')
        state.user.isAuthenticated = true
        state.user.id = localStorage.getItem('userid')
        state.user.username = localStorage.getItem('username')
      } else {
        state.user.token = ''
        state.user.isAuthenticated = false
        state.user.id = 0
        state.user.username = ''
      }
    },
    setToken(state, token){
      state.token = token
      state.user.isAuthenticated = true
    },
    removeToken(state){
      state.user.token = ''
      state.user.isAuthenticated = false
    },
    setUser(state, user){
      state.user.id = user.id
      state.user.username = user.username

      localStorage.setItem('username', user.username)
      localStorage.setItem('userid', user.id)
    },
  },
  actions: {
  },
  modules: {
  }
})
