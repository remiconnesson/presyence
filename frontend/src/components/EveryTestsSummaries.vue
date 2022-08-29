<script setup lang="ts">
import { useTestsReportsStore } from "@/stores/testsReports";

const testsReportsStore = useTestsReportsStore();
</script>

<template>
  <main>
    <pre
      v-for="testReport in testsReportsStore.testsReports"
      :key="testReport.test.title"
    >
  {{ testReport }}
    </pre>
  </main>
</template>
