<script setup lang="ts">
import { ref, computed } from "vue";
import { useTestsReportsStore } from "@/stores/testsReports";
import { RouterLink } from "vue-router";

const testsReportsStore = useTestsReportsStore();

// filter based on status
const allStatus = ["Crash", "WrongResult", "Success"] as const;
type Status = typeof allStatus[number];

const selectedStatus = ref<Status[]>([...allStatus]);

// filter based on title
const searchTerm = ref("");

const filteredTestsReports = computed(() => {
  return testsReportsStore.testsReports.filter((testReport) => {
    if (selectedStatus.value.includes(testReport.result.status)) {
      if (testReport.test.title.includes(searchTerm.value)) {
        return true;
      }
    }
    return false;
  });
});
</script>

<template>
  <div class="search-box">
    <label for="search">Filter</label>
    <input
      type="text"
      name="search"
      v-model="searchTerm"
      placeholder="search term"
    />
  </div>
  <div class="filter-options">
    <div class="option" v-for="status in allStatus" :key="status">
      <input
        type="checkbox"
        :id="status"
        :value="status"
        v-model="selectedStatus"
      />
      <label :for="status">{{ status }}</label>
    </div>
  </div>
  <ul>
    <li
      v-for="(testReport, index) in filteredTestsReports"
      :key="testReport.test.title"
    >
      <RouterLink :to="{ name: 'test-detail', params: { index } }">
        {{ testReport.result.status }} --
        {{ testReport.test.title }}
      </RouterLink>
    </li>
  </ul>
</template>

<style scoped>
li {
  list-style: none;
}
</style>
