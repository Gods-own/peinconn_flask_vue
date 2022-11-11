<template>
  <RegistrationForm v-if="isAuthenticatedRoute">
    <router-view/>
  </RegistrationForm>
</template>

<script>
import RegistrationForm from './views/RegisterForm';
export default {
  name: "App",
  components: {
    RegistrationForm,
  },
  data() {
    return {
      isAuthenticatedRoute: this.$route.meta.requiresAuth
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
