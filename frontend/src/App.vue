<template>
  <router-view />
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useAuthStore } from './stores/auth';
import { useConnectionStore } from './stores/connection';

onMounted(() => {
  const connection = useConnectionStore()
  connection.connect()
  
  const auth = useAuthStore()
  auth.loadLoginInfo()
})
</script>
