<template>
<div>
<div v-if="isAuthenticatedRoute">
  <router-view/>
</div>
  <RegistrationForm v-else>
    <router-view/>
  </RegistrationForm>
  </div>
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

</style>
