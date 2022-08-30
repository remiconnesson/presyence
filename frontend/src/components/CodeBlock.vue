<script setup lang="ts">
import { computed } from "vue";
import highlightjs from "highlight.js";

const props = defineProps<{
  code: string;
}>();

const highlightedCode = computed(() => {
  return highlightjs.highlight(props.code, { language: "python" }).value;
});
</script>

<template>
  <pre>
  <code>
  <div v-html="highlightedCode" />
  </code></pre>
</template>
