<template>
  <q-page padding>
    <!-- content -->
    <div class="q-pa-md" style="max-width: 400px">

      <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
        <q-input filled v-model="name" label="Your name *" hint="Name and surname" lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please type something']" />

        <q-input filled type="password" v-model="password" label="Password *" lazy-rules :rules="[
          val => val && val.length >= 8 || 'Password must be at least 8 characters long.'
        ]" />
        
        <q-input filled type="email" v-model="email" label="Email *" lazy-rules />
        
        <q-toggle v-model="accept" label="I accept the license and terms" />

        <div>
          <q-btn label="Submit" type="submit" color="primary" v-bind:disable="cannotSubmit"/>
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
import { computed } from '@vue/reactivity';

const connection = useConnectionStore()
const name = ref('')
const password = ref('')
const email = ref('')
const accept = ref(false)

const cannotSubmit = computed(() => !(accept && connection.isConnected))

function onReset () {
  name.value = ''
  password.value = ''
  accept.value = false
}

function onSubmit (event: Event) {
  event.preventDefault()
  if (!connection.isConnected) {
    console.log("Can't register because you are not connected")
  } else {
    const auth = useAuthStore()
    auth.register(name.value, password.value, email.value)
  }
}
</script>
