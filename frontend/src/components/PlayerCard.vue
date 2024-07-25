<script setup lang="ts">
import { type User } from '@/stores';

const props = defineProps<{
  user: User;
}>();
</script>

<template>
  <v-card rounded="lg" class="bg-transparent">
    <v-avatar size="192" class="ma-8 bg-orange-accent-4" :class="{ 'buzzer-active': props.user.buzzerActive }">
      <v-icon size="160" class="w-100 h-100">mdi-account</v-icon>
    </v-avatar>

    <v-card-actions>
      <v-text-field label="Answer" disabled>{{ props.user.answer }}</v-text-field>
    </v-card-actions>
  </v-card>
</template>

<style scoped></style>
