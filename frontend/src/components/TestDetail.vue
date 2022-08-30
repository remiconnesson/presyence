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
  <h1>{{ test.result.status }} -- {{ test.test.title }}</h1>
  <CodeBlock
    v-if="test.result.status === 'WrongResult'"
    :code="test.result.assertion_error_message"
  >
    Pandas Error Message
  </CodeBlock>
  <DataFrameBlock :csv="test.test.expected_output">
    The Expected Result
  </DataFrameBlock>

  <DataFrameBlock
    v-if="test.result.status === 'WrongResult'"
    :csv="test.result.testrun_output"
    >The Test Result</DataFrameBlock
  >

  <CodeBlock v-if="test.result.status === 'Crash'" :code="test.result.traceback"
    >Crash Traceback</CodeBlock
  >
  <CodeBlock :code="test.test.function">Tested Function</CodeBlock>
  <DataFrameBlock :csv="test.test.input"> The Test Input </DataFrameBlock>
</template>
