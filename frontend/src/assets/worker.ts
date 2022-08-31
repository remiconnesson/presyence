import json from "@/assets/input.json";

const testReport = json.testReport;

console.log("Worker is executed");

self.onmessage = () => {
  self.postMessage(testReport);
};
