<script setup lang="ts">
import { questionStore } from '@/stores';
</script>

<template>
  <v-card v-if="questionStore.question" width="800px" class="text-center pa-5">
    <v-card-title class="text-h4">Question {{ questionStore.question.number }}:</v-card-title>
    <v-card-text class="h-100 text-">{{ questionStore.question.question.text }}</v-card-text>

    <v-card-actions class="mt-8">
      <slot v-if="!questionStore.question.solution" name="actions" />
      <v-text-field v-else color="success" disabled>{{ questionStore.question.solution.text }}</v-text-field>
    </v-card-actions>
  </v-card>
</template>

<style scoped></style>
