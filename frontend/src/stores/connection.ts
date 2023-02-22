import { defineStore } from "pinia";
import { io, Socket } from "socket.io-client"

const WS_URL = 'ws://localhost:5000'

export const useConnectionStore = defineStore('connection', {
  state: () => ({
    ws: null as Socket | null
  }),

  getters: {
    isConnected: (state) => state.ws != null
  },

  actions: {
    connect() {
      // create ws connection
      console.log('connecting to ws server')
      this.ws = io(WS_URL)
    },

    disconnect() {
      // disconnect
    }
  },
})