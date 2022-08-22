<script setup lang="ts">
import { ref } from "vue";
import Worker from "@/assets/worker.js?worker";

let worker: Worker;

const enthusiasmLevel = ref("!!!");

const messageFromTheWorker = ref("No message yet...");

const workerLaunched = ref(false);

function launchWorker() {
  if (workerLaunched.value) return;
  worker = new Worker();
  worker.addEventListener("message", (event) => {
    messageFromTheWorker.value = event.data;
  });
  workerLaunched.value = true;
}

const messageToWorker = ref("Hey");

const sendMessageToWorker = () => {
  if (!workerLaunched.value) return;
  worker.postMessage(messageToWorker.value);
  messageToWorker.value = "";
};
</script>

<template>
  <h1>Hello, World{{ enthusiasmLevel }}</h1>
  <br />
  <button @click="launchWorker" v-if="!workerLaunched">
    Launch the worker
  </button>
  <br />
  <p>{{ messageFromTheWorker }}</p>
  <br />
  <div v-if="workerLaunched">
    <input v-model="messageToWorker" /><button @click="sendMessageToWorker()">
      SEND
    </button>
  </div>
</template>
