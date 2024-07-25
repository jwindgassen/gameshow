<script setup lang="ts">
import { userStore } from '@/stores';
import QuestionCard from '@/components/questions/QuestionCard.vue';

function activateBuzzer() {
  userStore.serverConnection?.emit('buzzer');
}
</script>

<template>
  <QuestionCard>
    <template #actions>
      <v-btn block @mousedown="activateBuzzer" color="primary">Buzzer</v-btn>
    </template>
  </QuestionCard>
</template>

<style scoped></style>
