<script setup lang="ts">
import { useTestsReportsStore } from "@/stores/testsReports";
import { RouterLink } from "vue-router";

const testsReportsStore = useTestsReportsStore();
</script>

<template>
  <ul>
    <li
      v-for="(testReport, index) in testsReportsStore.testsReports"
      :key="testReport.test.title"
    >
      <RouterLink :to="{ name: 'test-detail', params: { index } }">
        {{ testReport.result.status }} --
        {{ testReport.test.title }}
      </RouterLink>
    </li>
  </ul>
</template>

<style scoped>
li {
  list-style: none;
}
</style>
