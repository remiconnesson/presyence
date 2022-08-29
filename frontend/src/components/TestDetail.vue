<script lang="ts" setup>
import { useRoute } from "vue-router";
import { useTestsReportsStore } from "@/stores/testsReports";

const route = useRoute();
const testsReportsStore = useTestsReportsStore();

const test = testsReportsStore.testsReports[route.params.index];
</script>

<template>
  {{ test }}
</template>
