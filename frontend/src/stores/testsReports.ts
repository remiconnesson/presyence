import { defineStore } from "pinia";
import Worker from "@/assets/worker.ts?worker";
import { ref } from "vue";

export const useTestsReportsStore = defineStore("testsReports", () => {
  const testsReports = ref([]);

  const worker = new Worker();
  worker.addEventListener("message", (event) => {
    testsReports.value = event.data;
  });
  worker.postMessage("ready"); // the worker will reply the tests reports

  return { testsReports };
});
