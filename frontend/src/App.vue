<script setup lang="ts">
import { RouterView } from "vue-router";
</script>

<template>
  <div class="section">
    <div class="container">
      <RouterView />
    </div>
  </div>
</template>

<style>
@import "https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css";
@import url("https://fonts.googleapis.com/css2?family=Karla&display=swap");
@import url(https://fonts.googleapis.com/css?family=Inconsolata:400,700|Open+Sans:400,800);
@import "highlight.js/styles/mono-blue.css";

body {
  font-family: Karla;
}
</style>
