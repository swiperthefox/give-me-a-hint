import { Cell, BookInfo, Book, ChangeDefinition} from './models'
import { defineStore } from 'pinia';
import { useConnectionStore } from './connection'
import { useAuthStore } from './auth'
import { NewBookInfo, Response } from '../types'

const auth = useAuthStore()

export const useBookStore = defineStore('book', {
  state: () => ({
    bookInfos: [] as BookInfo[],
    bookContents: {} as Map<number, Book>,
    currentBook: null as number | null
  }),
  
  getters: {
    bookContent: (state) => {
      return state.currentBook ?
        state.bookContents.get(state.currentBook) || [] :
        []
      }
  },
  
  actions: {
    processResponse(response: Response<BookInfo[]>) {
      if (response.success) {
        const booklist = response.data
        this.bookInfos.splice(0, this.bookInfos.length, ...booklist) 
      } else {
        console.log(response.error)
      }
    },
    
    updateBookInfos() {
      if (!auth.isLoggedIn) return
      const connection = useConnectionStore()      
      // send login token, if the token is valid, get a list of bookinfos back
      connection.ws?.emit(
        'get-book-list',
        auth.token,
        this.processResponse
      )
    },
    
    setBookInfos(books: BookInfo[]) {
      this.bookInfos.splice(0, this.bookInfos.length, ...books)
    },
    
    sendNewBookInfo(bookInfo: NewBookInfo) {
      const connection = useConnectionStore()
      connection.ws?.emit(
        'new-book',
        auth.token, 
        bookInfo,
        this.processResponse
      )
    },
    
    selectBook(bookId: number) {
      // set bookId as currentBook
    },
    
    fetchBookContent(bookid: number) {
      // send login token and bookid, get the contents of bookid,
      // update the content in bookContents
    },
    
    onBookUpdate(changes: ChangeDefinition[]) {
      // apply the changes to the bookContents
    }
  }
})