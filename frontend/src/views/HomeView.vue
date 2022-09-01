<script setup lang="ts">
import { ref, computed } from "vue";
import { useTestsReportsStore } from "@/stores/testsReports";
import { RouterLink } from "vue-router";
import type { TestReport } from "@/testReport";

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

const successTagStyle = (test: TestReport) => {
  if (test.result.successful) return "is-success";
  else return "is-danger";
};
</script>

<template>
  <section class="section">
    <div class="panel">
      <p class="panel-heading">Tests Reports</p>
      <div class="is-primary-panel">
        <div
          class="panel-block is-flex is-flex-direction-column is-align-items-flex-start"
        >
          <div class="field">
            <label for="search" class="label">Filter by search term</label>
            <div class="control">
              <input
                data-testid="search-bar"
                type="text"
                name="search"
                v-model="searchTerm"
                placeholder="search term"
              />
            </div>
          </div>
        </div>
        <div
          class="panel-block is-flex is-flex-direction-column is-align-items-flex-start"
        >
          <div class="field">
            <label for="search" class="label">Filter by status</label>
            <div class="filter-options">
              <div class="option" v-for="status in allStatus" :key="status">
                <label :for="status" class="checkbox">
                  <input
                    data-testid="filter-checkbox"
                    type="checkbox"
                    :id="status"
                    :value="status"
                    v-model="selectedStatus"
                  />

                  {{ status }}</label
                >
              </div>
            </div>
          </div>
        </div>

        <nav>
          <ul data-testid="home-all-tests-list">
            <li v-for="testReport in filteredTestsReports" :key="testReport.id">
              <RouterLink
                :to="{ name: 'test-detail', params: { index: testReport.id } }"
                class="panel-block is-flex is-flex-direction-column is-align-items-flex-start"
              >
                <span
                  data-testid="home-status-tag"
                  class="tag"
                  :class="successTagStyle(testReport)"
                  >{{ testReport.result.status }}</span
                >
                <span>{{ testReport.test.title }}</span>
              </RouterLink>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </section>
</template>

<style scoped>
li {
  list-style: none;
}

p.panel-heading {
  text-transform: uppercase;
  letter-spacing: 0.05rem;
  /*
  font-family: Inconsolata;
  font-size: 1.5rem;
  */
}
</style>
