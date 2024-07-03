<script setup>
import { ref, computed } from 'vue';
import axios from 'axios';
import { useRoute ,useRouter} from 'vue-router';
const route=useRoute();
const router=useRouter()
const Ename = ref('');
const department = ref('');
const formErrors = ref({});

const validateForm = () => {
  formErrors.value = {};

  if (!Ename.value) {
    formErrors.value.Ename = 'Employee name is required.';
  }

  if (!department.value) {
    formErrors.value.department = 'Department is required.';
  }

  return Object.keys(formErrors.value).length === 0;
};

const updateEmployee = async () => {
const employeeId=route.params.id;

  if (!validateForm()) {
    return;
  }

  try {
    const response = await axios.put(`http://127.0.0.1:8000/${employeeId}/`, {
      Ename: Ename.value,
      department: department.value,
    });
    if (response) {
      console.log('Success!');
      Ename.value = '';
      department.value = '';
      router.push('/employeeview')
    }
  } catch (error) {
    console.log(error);
  }
};

const hasError = (field) => {
  return computed(() => formErrors.value[field]);
};
</script>

<template>
  <div class="flex flex-col justify-center items-center mt-10">
    <h1 class="text-3xl mb-20">Add Employee</h1>
    <form @submit.prevent="updateEmployee">
      <div class="mb-3 flex flex-col gap-1">
        <label for="name">Ename</label>
        <input
          class="border-2 border-gray-300 outline-none px-[10vw] py-2"
          v-model="Ename"
          type="text"
          id="name"
          name="name"
          placeholder="Enter your name?"
        />
        <p v-if="hasError('Ename')" class="text-red-500">{{ hasError('Ename') }}</p>
      </div>
      <div class="mb-3 flex flex-col gap-1">
        <label for="department">Department</label>
        <input
          class="border-2 border-gray-300 outline-none px-[10vw] py-2"
          v-model="department"
          type="text"
          id="department"
          name="department"
          placeholder="Enter your department?"
        />
        <p v-if="hasError('department')" class="text-red-500">{{ hasError('department') }}</p>
      </div>
      <button type="submit" class="bg-green-800 px-16 text-white py-2 rounded-lg">Update</button>
    </form>
  </div>
</template>