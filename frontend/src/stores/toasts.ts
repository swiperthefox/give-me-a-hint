import { defineStore } from 'pinia';

export const useCounterStore = defineStore('counter', {
  state: () => ({
    messages: [] as string[]
  }),

  getters: {
    current(): string[] {
        return this.messages.splice(0)
    }
  },

  actions: {
    addMsg(m: string) {
        this.messages.push(m)
    },
    
  }
});
