<script setup lang="ts">
import { useTestsReportsStore } from "@/stores/testsReports";

const testsReportsStore = useTestsReportsStore();
</script>

<template>
  <main>
    <pre>
  {{ testsReportsStore.testsReports }}
    </pre>
  </main>
</template>
