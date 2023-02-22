<template>
  <q-page class="row items-center justify-evenly">
    Welcome to MathNote. 
    
  </q-page>
</template>

<script setup lang="ts">
import { useConnectionStore } from 'src/stores/connection'
const connection = useConnectionStore()
if (!connection.isConnected) {
  connection.connect()
}

</script>
