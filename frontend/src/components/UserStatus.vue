<template>
    <div v-if="auth.isLoggedIn">
      {{ auth.name }}
    </div>
    <div v-else>
      <router-link to='/register'>Register</router-link>
      <router-link to='/login'>Log In</router-link>
    </div>
</template>

<script setup lang="ts">
import { useAuthStore } from 'src/stores/auth';
const auth = useAuthStore()

</script>