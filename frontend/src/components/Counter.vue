<script setup lang="ts">
import { useCounterStore } from "@/stores/counter";

const counterStore = useCounterStore();
</script>

<template>
  <h1>Counter : {{ counterStore.counter }}</h1>
  <br />
  <button @click="counterStore.increment">+ 1</button>
</template>
