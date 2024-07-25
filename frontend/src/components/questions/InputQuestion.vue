<script setup lang="ts">
import { ref } from 'vue';
import { userStore } from '@/stores';
import QuestionCard from '@/components/questions/QuestionCard.vue';

const input = ref('');

function submitAnswer() {
  userStore.serverConnection?.emit('answer', input.value);
}
</script>

<template>
  <QuestionCard>
    <template #actions>
      <v-row>
        <v-text-field v-model="input" name="Answer"></v-text-field>
        <v-btn @click="submitAnswer">Submit</v-btn>
      </v-row>
    </template>
  </QuestionCard>
</template>

<style scoped></style>
