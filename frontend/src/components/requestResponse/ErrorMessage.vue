<template>
  <div class="response-container error">
    <p>{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  name: "ErrorMessage",
  props: {
    errorMessage: String,
  },
};
</script>

<style scoped>
@import "../../assets/css/responseMessage.css";
</style>
