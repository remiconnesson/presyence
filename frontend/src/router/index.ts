import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CounterView from "../views/CounterView.vue";
import WorkerView from "../views/WorkerView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/counter",
      name: "counter",
      component: CounterView,
    },
    {
      path: "/worker",
      name: "worker",
      component: WorkerView,
    },
  ],
});

export default router;
