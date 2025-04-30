<!-- <div v-if="successMessage" class="alert alert-success mt-3">
<div v-if="errorMessage" class="alert alert-danger mt-3"> -->
<template>
  <div class="container mt-5">
    <h2>Upload Form</h2>
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>
    <div v-if="errorMessage" class="alert alert-danger">
      <ul>
        <li v-for="error in errorMessage" :key="error">{{ error }}</li>
      </ul>
    </div>
    <form id="movieForm" @submit.prevent="saveMovie">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" class="form-control"></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Photo Upload</label>
        <input type="file" name="poster" class="form-control" />
      </div>
      <button type="submit" name="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
let csrf_token = ref("");
let successMessage = ref("");
let errorMessage = ref("");

onMounted(() => {
  getCsrfToken();
})

const getCsrfToken = () => {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    })
}

const saveMovie = () => {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);
  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      if (data.message) {
        successMessage.value = `Success: ${data.message}`;
        errorMessage.value = "";
      }
      else {
        successMessage.value = "";
        errorMessage.value = data;
      }
    })
    .catch(function (error) {
      successMessage.value = "";
      errorMessage.value = `Error: ${error.message}`;
    });
}
</script>