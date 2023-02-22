<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          <router-link to="/">Math Notes</router-link>
          <router-link to="/home">Home</router-link>
        </q-toolbar-title>

        <div v-if="connection.isConnected">
          Online
        </div>
        <div v-else>
          Offline
        </div>
        <UserStatus></UserStatus>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { useConnectionStore } from 'src/stores/connection'
import UserStatus from '../components/UserStatus.vue'

const connection = useConnectionStore()
</script>
