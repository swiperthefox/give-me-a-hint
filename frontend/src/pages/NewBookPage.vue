<template>
  <q-page padding>
    <!-- content -->
    <div class="q-pa-md" style="max-width: 400px">

      <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
        <q-input filled v-model="title" label="The title *" hint="The title of your book" lazy-rules
          :rules="[ val => val && val.length > 0 || 'Title can\'t be empty.']" />

        <q-input filled type="text" v-model="description" label="Description" />
        
        <q-file filled clearable v-model="coverImage" label="Choose an image for the cover" accept=".jpg, image/*" />
        <q-img :src="imageUrl" id="preview" spinner-color="white" style="height: 140px; max-width: 150px"/>
        <div>
          <q-btn label="Submit" type="submit" color="primary"/>
          <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
        </div>
      </q-form>

      </div>
  </q-page>
</template>

<script setup lang="ts">
import { computed } from '@vue/reactivity';
import { ref } from 'vue'

import { getBase64Image } from '../lib/image'
import { useConnectionStore } from 'src/stores/connection'
import { useAuthStore } from 'src/stores/auth'
import { useBookStore } from 'src/stores/book'
import { BookInfo } from 'src/stores/models';

const connection = useConnectionStore()
const auth = useAuthStore()
const bookStore = useBookStore()

const title = ref('')
const description = ref('')
const coverImage = ref(null)
const imageUrl = computed(() => coverImage.value ? URL.createObjectURL(coverImage.value) : '')
const preview = ref(null)

function onReset() {
  title.value = ''
  description.value = ''
  coverImage.value = null
}

function onSubmit() {
  if (!auth.isLoggedIn) {
    console.log("need to log in")
  }
  const dataurl = getBase64Image(document.getElementById('preview')?.querySelector('img'), 600)
  bookStore.sendNewBookInfo({
    title: title.value,
    description: description.value,
    cover: dataurl
  })
  
}

</script>
