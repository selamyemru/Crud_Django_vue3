<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { Icon } from '@Iconify/vue';
import { useRouter } from 'vue-router';

const employees = ref([]);
const router=useRouter()
const fetchdata = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/');
    employees.value = response.data;
  } catch (error) {
    console.error(error);
  }
};
const deleteEmployee = async (id) => {
  try {
    const response = await axios.delete(`http://127.0.0.1:8000/${id}/`);
    employees.value = response.data;
    if(response){
      router.push('/')
    }
  } catch (error) {
    console.error(error);
  }
};
onMounted(fetchdata);
const goToEditPage = (id) => {
  router.push({ name: 'EditEmployee', params: { id: id } });
};
</script>

<template>
  <main class="flex flex-col items-center justify-center mt-10">
    <h1 class="text-3xl">You can see the employee</h1>
    <table class="table border-2 border-gray-200 mt-10">
      <thead class="text-green-800">
        <th class="border-r-2 border-gray-200 px-6 py-2 border-b-2">Id</th>
        <th class="border-r-2 border-gray-200 px-6 py-2 border-b-2">Name</th>
        <th class="border-r-2 border-gray-200 px-6 py-2 border-b-2">Department</th>
        <th class="border-r-2 border-gray-200 px-6 py-2 border-b-2">Edit</th>
        <th class="px-6 py-2 border-b-2">Delete</th>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <td class="border-r-2 border-gray-200 px-6 py-2 border-b-2">{{ employee.id }}</td>
          <td class="border-r-2 border-gray-200 px-6 py-2 border-b-2">{{ employee.Ename }}</td>
          <td class="border-r-2 border-gray-200 px-6 py-2 border-b-2">{{ employee.department }}</td>
          
          <td class="px-6 py-2 border-b-2 border-r-2">
           <button @click="goToEditPage(employee.id)"><Icon icon="material-symbols:edit" class="h-4 w-4 text-gary-300 hover:text-green-700" /></button> 
          </td>
          <td  class="px-6 py-2 border-b-2">
           <button @click="deleteEmployee(employee.id)"><Icon icon="material-symbols:delete" class="h-4 w-4 text-red-500 hover:text-red-700" />
          </button> 
          </td>
        </tr>
      </tbody>
    </table>
  </main>
</template>