<script lang="ts" setup>
import { useRoute } from "vue-router";
import { useTestsReportsStore } from "@/stores/testsReports";
import { computed } from "vue";
import type { TestReport } from "@/testReport";
import CodeBlock from "@/components/CodeBlock.vue";
import DataFrameBlock from "@/components/DataFrameBlock.vue";

const route = useRoute();
const testsReportsStore = useTestsReportsStore();

const test = computed<TestReport>(() => {
  const index = parseInt(route.params.index as string);
  return testsReportsStore.testsReports[index];
});

const successTagStyle = computed(() => {
  if (test.value.result.successful) return "is-success";
  else return "is-danger";
});
</script>

<template>
  <h1 class="title">
    <span class="tag is-medium" :class="successTagStyle">{{
      test.result.status
    }}</span>
    {{ test.test.title }}
  </h1>
  <div
    class="detail-card block"
    v-if="test.result.status === 'WrongResult'"
    data-testid="test-detail-pandas-error"
  >
    <h2 class="subtitle">Pandas Error Message</h2>
    <CodeBlock :code="test.result.assertion_error_message" />
  </div>
  <div class="detail-card block" data-testid="test-detail-expected-output">
    <h2 class="subtitle">The Expected Result</h2>
    <DataFrameBlock :csv="test.test.expected_output" />
  </div>
  <div
    class="detail-card block"
    v-if="test.result.status === 'WrongResult'"
    data-testid="test-detail-testrun-output"
  >
    <h2 class="subtitle">The Observed Result</h2>
    <DataFrameBlock :csv="test.result.testrun_output" />
  </div>

  <div
    class="detail-card block"
    v-if="test.result.status === 'Crash'"
    data-testid="test-detail-traceback"
  >
    <h2 class="subtitle">Crash Traceback</h2>
    <CodeBlock :code="test.result.traceback" />
  </div>
  <div class="detail-card block" data-testid="test-detail-function">
    <h2 class="subtitle">Tested Function</h2>
    <CodeBlock :code="test.test.function" />
  </div>

  <div class="detail-card block" data-testid="test-detail-input">
    <h2 class="subtitle">The Test Input</h2>
    <DataFrameBlock :csv="test.test.input" />
  </div>
</template>
