<script setup lang="ts">
import { computed } from "vue";
import * as d3 from "d3";

const props = defineProps<{
  csv: string;
}>();

const dataFrame = computed(() => {
  return d3.csvParse(props.csv);
});
</script>

<template>
  <table class="table is-narrow is-hoverable is-striped">
    <thead>
      <tr>
        <th v-for="col in dataFrame.columns" :key="col">
          {{ col }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(row, index) in dataFrame" :key="index">
        <td v-for="(el, index) in row" :key="index">
          {{ el }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped></style>
