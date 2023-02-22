import { connect } from 'http2'
import { defineStore } from 'pinia'

import { LocalStorage, Notify } from 'quasar'
import { useConnectionStore } from './connection'

export const useAuthStore = defineStore('data', {
  state: () => ({
    name: 'gongfu panda',
    token: ''
  }),
  
  getters: {
    isLoggedIn: (state) => state.token !== ''
  },
  
  actions: {
    register (name: string, password: string, email: string) {
      // register users
      const connection = useConnectionStore()
      connection.ws?.emit('register', {
        name,
        password,
        email
      }, (success: boolean) => {
        if (success) {
          this.router.push('/login')
        } else {
          Notify.create('Register failed.')
        }
      })
    },

    login (name: string, password: string) {
      // do ajax call, save name and token on success
      const connection = useConnectionStore()
      if (connection.ws) {
        connection.ws.emit('login', {
          name,
          password,
        }, (response: any) => {
          console.log(response)
          if (response && response.token !== '') {
            LocalStorage.set('login', response)
            this.$patch(response)
            this.router.push('/home')
          } else {
            Notify.create({
              message: 'Username or password is incorrect.',
              color: 'negative',
              position: 'top',
              progress: true
            })
          }
        })
      } else {
        Notify.create('You are offline now.')
      }
    },
    
    varifyLoginToken() {
      const connection = useConnectionStore()
      connection.ws?.emit('verify-token', this.token,
        (response: any) => {
          console.log(response)
          if (!response) {
            this.name = ''
            this.token = ''
          }
        })
    },
    
    loadLoginInfo() {
      this.$patch(LocalStorage.getItem('login'))
      this.varifyLoginToken()
      if (!this.isLoggedIn) {
        this.router.push('/')
      }
    }
  }
})
