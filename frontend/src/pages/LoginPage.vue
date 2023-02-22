<template>
  <q-page padding>
    <!-- content -->
    <div class="q-pa-md" style="max-width: 400px">

      <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
        <q-input filled v-model="name" label="Your name *" hint="Your username" />

        <q-input filled type="password" v-model="password" label="Password *"/>
        
        <div>
          <q-btn label="Submit" type="submit" color="primary"/>
          <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
        </div>
      </q-form>

      </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { useConnectionStore } from 'src/stores/connection'
import { useAuthStore } from 'src/stores/auth'

const auth = useAuthStore()
const connection = useConnectionStore()

const name = ref('')
const password = ref('')

function onReset () {
  name.value = ''
  password.value = ''
}

function onSubmit (event: Event) {
  event.preventDefault()
  if (!connection.isConnected) {
    console.log("Can't login because you are not connected")
  } else {
    auth.login(name.value, password.value)
  }
}
</script>
