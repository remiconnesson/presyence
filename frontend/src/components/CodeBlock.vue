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
  <h2><slot></slot></h2>
  <pre class="code code-highlight">
    <code class="code code-highlight">
      <div v-html="highlightedCode" />
    </code>
  </pre>
</template>

<style scoped>
.code .code-highlight {
  font-family: Inconsolata;
}
</style>
