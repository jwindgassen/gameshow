<script setup lang="ts">
import { ref } from 'vue';
import SettingsSidebar from '@/SettingsSidebar.vue';
import PlayerCard from '@/components/PlayerCard.vue';
import LoginDialog from '@/components/LoginDialog.vue';
import { questionStore, userStore } from '@/stores';
import BuzzerQuestion from '@/components/questions/BuzzerQuestion.vue';
import InputQuestion from '@/components/questions/InputQuestion.vue';

const showPlayers = ref(false);
</script>

<template>
  <v-layout class="rounded rounded-md">
    <v-app-bar>
      <v-app-bar-title text="Gameshow" />
      <v-app-bar-nav-icon @click="showPlayers = !showPlayers" />
    </v-app-bar>

    <v-main>
      <BuzzerQuestion v-if="questionStore.question?.input.type === 'buzzer'" />
      <InputQuestion v-else-if="questionStore.question?.input.type === 'textInput'" />
    </v-main>

    <v-navigation-drawer v-model="showPlayers" location="right" :width="300">
      <SettingsSidebar />
    </v-navigation-drawer>

    <v-footer app class="bg-transparent">
      <PlayerCard v-for="user in userStore.users" :key="user.name" :user="user" />
    </v-footer>
  </v-layout>

  <LoginDialog />
</template>

<style scoped></style>
