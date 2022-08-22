self.postMessage("Hello from the worker");

console.log("Worker is executed");

self.onmessage = (event) => {
  self.postMessage(`I am the worker and I received: ${event.data}`);
};
