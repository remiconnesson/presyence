<script setup lang="ts">
import { ref } from "vue";
import Worker from "@/assets/worker.ts?worker";

const worker = new Worker();

const messageFromTheWorker = ref("No message yet...");

worker.addEventListener("message", (event) => {
  messageFromTheWorker.value = event.data;
});

worker.postMessage("");
</script>

<template>
  <pre>
  {{ messageFromTheWorker }}
  </pre>
</template>
