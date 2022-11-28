<template>
  <AuthForm>
    <form class="login-register-form" @submit="onSubmit">
      <LoadingCover v-show="loading" />
      <div class="form-header">
        <ErrorMessage v-show="error" :errorMessage="error" />
        <div>
          <h2>LOGIN</h2>
          <p>Fill the form to login</p>
        </div>
      </div>
      <div class="form-group">
        <label for="username">Username</label>
        <input id="username" class="form-control" type="text" placeholder="Username" v-model="username" />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input id="password" class="form-control" type="password" placeholder="Password" v-model="password" />
      </div>
      <div class="submit-btn-div form-group">
        <input class="submit-btn" type="submit" value="Login" />
      </div>
    </form>
  </AuthForm>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
// import { checkAuthUser } from "../../api/jwt-access-token.js";
import AuthForm from "@/components/AuthForm.vue";
import LoadingCover from "@/components/LoadingCover.vue";
import ErrorMessage from "@/components/requestResponse/ErrorMessage.vue";
export default {
  name: "LoginForm",
  components: { AuthForm, LoadingCover, ErrorMessage },
  data() {
    return {
      username: "",
      password: "",
      // authUser: currUser,
    };
  },
  computed: {
    ...mapGetters("auth", ["loading", "error", "success"]),
  },
  watch: {
    "$store.state.auth.success": function () {
      if (this.$store.state.auth.success) {
        window.location.href = "/activities";
        // this.$router.push({ path: "/register/interest" });
      }
    },
  },
  methods: {
    ...mapActions("auth", ["authenticateUser"]),
    onSubmit(e) {
      e.preventDefault();
      const payload = {
        username: this.username,
        password: this.password,
      };
      const searchParams = new URLSearchParams(payload);
      this.authenticateUser(searchParams);
      // this.$router.push({ path: "/activities" });
      // setTimeout(function () {
      //   console.log(this.isSuccess, this.error, this.loading);
      // }, 3000);
      // console.log(this.success, this.error, this.loading);
      // this.username = "";
      // this.password = "";
    },
  },
  // updated() {
  //   console.log(this.success);
  // },
  // created() {
  //   this.isSuccess = this.success;
  // },
};
</script>

<style scoped>
@import "../../assets/css/authForm.css";
</style>
