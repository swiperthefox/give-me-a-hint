<template>
  <q-card flat bordered class="my-card bg-grey-1">
    <q-card-section>
      <div class="row items-center no-wrap">
        <div class="col">
          <div class="text-h6">{{ book.title }}</div>
        </div>

        <div class="col-auto">
          <q-btn color="grey-7" round flat icon="more_vert">
            <q-menu cover auto-close>
              <q-list>
                <q-item clickable>
                  <q-item-section>Delete Book</q-item-section>
                </q-item>
                <q-item clickable>
                  <q-item-section>Share</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </div>
      </div>
    </q-card-section>
    <q-card-section @click="open" style="cursor: pointer;">
      <q-img :src="'http://localhost:5000' + book.cover" height="300px" fit="none"></q-img>
    </q-card-section>
    <q-card-section>
      {{ book.description }}
    </q-card-section>
  </q-card>
</template>

<script setup lang="ts">
import { BookInfo } from 'src/stores/models'
const props = defineProps<{
  book: BookInfo
}>()

function open() {
  console.log("open the book")
}
</script>
