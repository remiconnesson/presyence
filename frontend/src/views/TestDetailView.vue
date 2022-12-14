<script setup lang="ts">
import { RouterLink } from "vue-router";
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
  <div class="columns">
    <div class="column is-four-fifths">
      <RouterLink to="/" class="button">Back</RouterLink>

      <h1 class="title title-strong-color box">
        <span class="tag is-medium" :class="successTagStyle">{{
          test.result.status
        }}</span>
        {{ test.test.title }}
      </h1>
      <div
        class="detail-card block box"
        v-if="test.result.status === 'WrongResult'"
        data-testid="test-detail-pandas-error"
      >
        <h2 class="subtitle subtitle-strong-color">Pandas Error Message</h2>
        <CodeBlock :code="test.result.assertion_error_message" />
      </div>
      <div
        class="detail-card block box"
        data-testid="test-detail-expected-output"
      >
        <h2 class="subtitle">The Expected Result</h2>
        <DataFrameBlock :csv="test.test.expected_output" />
      </div>
      <div
        class="detail-card block box"
        v-if="test.result.status === 'WrongResult'"
        data-testid="test-detail-testrun-output"
      >
        <h2 class="subtitle">The Observed Result</h2>
        <DataFrameBlock :csv="test.result.testrun_output" />
      </div>

      <div
        class="detail-card block box"
        v-if="test.result.status === 'Crash'"
        data-testid="test-detail-traceback"
      >
        <h2 class="subtitle">Crash Traceback</h2>
        <CodeBlock :code="test.result.traceback" />
      </div>
      <div class="detail-card block box" data-testid="test-detail-function">
        <h2 class="subtitle">Tested Function</h2>
        <CodeBlock :code="test.test.function" />
      </div>

      <div class="detail-card block box" data-testid="test-detail-input">
        <h2 class="subtitle">The Test Input</h2>
        <DataFrameBlock :csv="test.test.input" />
      </div>
    </div>
  </div>
</template>
