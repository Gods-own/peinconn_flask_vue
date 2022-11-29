<template>
  <form class="login-register-form" @submit="onSubmit">
    <LoadingCover v-show="loading" />
    <div class="form-header">
      <ErrorMessage v-show="error" :errorMessage="error" />
      <div>
        <h2>REGISTRATION</h2>
        <p>Fill the form to register</p>
      </div>
    </div>
    <div>
      <div v-for="(interest, index) in interests" :key="interest.id">
        <input :id="'hobby' + index" :value="interest.id" v-model="hobbies" type="checkbox" />
        <div>
          <label :for="'hobby' + index">{{ interest.hobby }}</label>
        </div>
        <img :src="interest.hobby_image" width="100" height="100" />
      </div>
      <button type="submit">Done</button>
    </div>
  </form>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import LoadingCover from "@/components/LoadingCover.vue";
import ErrorMessage from "@/components/requestResponse/ErrorMessage.vue";
import { currUser } from "../../api/jwt-access-token.js";
export default {
  name: "RegisterInterest",
  components: { LoadingCover, ErrorMessage },
  data() {
    return {
      hobbies: [],
      authUser: currUser,
    };
  },
  watch: {
    "$store.state.interest.success": function () {
      if (this.$store.state.interest.success) {
        window.location.href = "/activities";
      }
    },
  },
  computed: {
    ...mapGetters("interest", ["interests", "userInterests", "loading", "error", "success"]),
  },
  methods: {
    ...mapActions("interest", ["fetchInterests", "addInterest", "fetchUserInterests"]),
    onSubmit(e) {
      e.preventDefault();
      const searchParams = new URLSearchParams();
      for (let hobby of this.hobbies) {
        searchParams.append("interests", hobby);
      }
      this.addInterest(searchParams);

      this.hobbies = [];
    },
  },
  created() {
    console.log(this.authUser);
    this.fetchInterests();
    this.fetchUserInterests(currUser.id);
  },
};
</script>

<style scoped>
@import "../../assets/css/interestForm.css";
@import "../../assets/css/authForm.css";
</style>
