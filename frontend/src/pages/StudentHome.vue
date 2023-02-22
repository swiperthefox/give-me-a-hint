<template>
  <q-page padding>
    <!-- content -->
    <h3>Book List</h3>
    <router-link to="/newbook">Create New Book</router-link>
    <div class="q-pa-md row items-start q-gutter-md">
      <book-item v-for="book in books.bookInfos" :book="book" :key="book.id"></book-item>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'

import { useBookStore } from 'src/stores/book'
import BookItem from '../components/BookItem.vue'
const books = useBookStore()

onMounted(() => {
  books.updateBookInfos()
})
</script>
