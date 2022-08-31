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

const successTagStyle = (test) => {
  if (test.result.successful) return "is-success";
  else return "is-danger";
};
</script>

<template>
  <section class="section">
    <div class="panel">
      <p class="panel-heading">presyence tests reports</p>
      <div class="is-primary-panel">
        <div
          class="panel-block is-flex is-flex-direction-column is-align-items-flex-start"
        >
          <div class="field">
            <label for="search" class="label">Filter by search term</label>
            <div class="control">
              <input
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
          <ul>
            <li v-for="testReport in filteredTestsReports" :key="testReport.id">
              <RouterLink
                :to="{ name: 'test-detail', params: { index: testReport.id } }"
                class="panel-block is-flex is-flex-direction-column is-align-items-flex-start"
              >
                <span class="tag" :class="successTagStyle(testReport)">{{
                  testReport.result.status
                }}</span>
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
</style>
