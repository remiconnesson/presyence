import { defineStore } from "pinia";
import Worker from "@/assets/worker.ts?worker";
import { ref } from "vue";
import type { TestReport } from "@/testReport";

export const useTestsReportsStore = defineStore("testsReports", () => {
  const testsReports = ref<TestReport[]>([]);

  const worker = new Worker();
  worker.addEventListener("message", (event) => {
    // once we get the reply it will contain the test report
    const _testReports = event.data as TestReport[];
    // we need to add an ID to each testReport so that it helps with filtering (v-for & :key)
    for (const [index, element] of _testReports.entries()) {
      element.id = index;
    }
    testsReports.value = _testReports;
  });
  worker.postMessage("ready"); // the worker will reply the tests reports

  return { testsReports };
});
