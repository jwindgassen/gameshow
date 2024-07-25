<script setup lang="ts">
import { userStore } from '@/stores';
import { computed } from 'vue';

const moderators = computed(() => userStore.users.filter((u) => u.role === 'Moderator'));
const players = computed(() => userStore.users.filter((u) => u.role === 'Player'));

function clearBuzzer() {
  console.log('clearBuzzer');
  userStore.serverConnection.emit('clearBuzzers');
}

function revealAnswers() {
  console.log('revealAnswers');
  userStore.serverConnection.emit('revealAnswers');
}

function showSolution() {
  console.log('showSolution');
  userStore.serverConnection.emit('showSolution');
}

function nextQuestion() {
  console.log('nextQuestion');
  userStore.serverConnection.emit('nextQuestion');
}
</script>

<template>
  <v-list>
    <v-btn @click="clearBuzzer" block>Clear Buzzers</v-btn>
    <v-btn @click="revealAnswers" block>Reveal Answers</v-btn>
    <v-btn @click="showSolution" block>Show Solution</v-btn>
    <v-btn @click="nextQuestion" block>Next Question</v-btn>

    <div class="my-8" />

    <v-list-subheader>Moderators</v-list-subheader>
    <v-list-item v-for="user in moderators" :key="user.name">
      {{ user.name }}
    </v-list-item>

    <v-list-subheader>Players</v-list-subheader>
    <v-list-item v-for="user in players" :key="user.name">
      {{ user.name }}
    </v-list-item>
  </v-list>
</template>

<style scoped></style>
