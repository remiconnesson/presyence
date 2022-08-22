<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/counter">Counter</RouterLink>
    <RouterLink to="/worker">Worker</RouterLink>
  </nav>

  <RouterView />
</template>
