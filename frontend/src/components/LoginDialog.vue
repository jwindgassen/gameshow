<script setup lang="ts">
import { ref } from 'vue';
import { initializeConnection } from '@/serverConnection';

const isOpen = ref(true);
const username = ref<string>('');
const role = ref<'Player' | 'Moderator' | null>(null);

function submit() {
  initializeConnection({
    name: username.value,
    role: role.value ?? 'Player',
    buzzerActive: false,
    answer: '',
  });
  isOpen.value = false;
}
</script>

<template>
  <v-dialog v-model="isOpen" width="512px" persistent>
    <v-card>
      <v-form @submit.prevent="submit" validate-on="input">
        <v-card-text>
          <v-text-field label="Username" v-model="username" />
          <v-combobox label="Role" v-model="role" :items="['Player', 'Moderator']" />
        </v-card-text>

        <v-card-actions>
          <v-btn block type="submit" @submit="submit" color="primary">Join</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<style scoped></style>
