self.postMessage("Hello from the worker");

import json from "@/assets/input.json";

const prefix = json.prefix;

console.log("Worker is executed");

self.onmessage = (event) => {
  self.postMessage(`${prefix} : I am the worker and I received: ${event.data}`);
};
