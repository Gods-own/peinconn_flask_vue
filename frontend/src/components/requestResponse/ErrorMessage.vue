<template>
  <div class="response-container error">
    <p>{{ eeMessage }}</p>
  </div>
</template>

<script>
export default {
  name: "ErrorMessage",
};
</script>

<style scoped>
@import "../../assets/css/responseMessage.css";
</style>
