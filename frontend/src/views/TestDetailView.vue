<script setup lang="ts">
import TestDetail from "@/components/TestDetail.vue";
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="columns">
    <div class="column is-four-fifths">
      <RouterLink to="/" class="button">Back</RouterLink>
      <TestDetail></TestDetail>
    </div>
  </div>
</template>
