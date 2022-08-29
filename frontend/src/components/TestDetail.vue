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
</script>

<template>
  <pre>
  {{ test.test.title }}
  {{ test.result.status }}
  </pre>
  <CodeBlock>
    {{ test.test.function }}
  </CodeBlock>
  <DataFrameBlock>
    {{ test.test.input }}
  </DataFrameBlock>
  <DataFrameBlock>
    {{ test.test.expected_output }}
  </DataFrameBlock>
  <DataFrameBlock v-if="test.result.status === 'WrongResult'">
    {{ test.result.testrun_output }}
  </DataFrameBlock>
  <CodeBlock v-if="test.result.status === 'WrongResult'">
    {{ test.result.assertion_error_message }}
  </CodeBlock>
  <CodeBlock v-if="test.result.status === 'Crash'">
    TRACEBACK
    {{ test.result.traceback }}
  </CodeBlock>
</template>
