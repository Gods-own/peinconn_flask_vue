<template>
  <AuthForm>
    <form class="login-register-form" method="post">
      <div class="form-header">
        <div>
          <h2>REGISTRATION</h2>
          <p>Fill the form to register</p>
        </div>
      </div>
      <div class="form-group">
        <label for="username">Username</label>
        <input id="username" class="form-control" type="text" placeholder="Username" v-model="username" />
      </div>
      <div class="form-group">
        <label for="name">Name</label>
        <input id="name" class="form-control" type="text" placeholder="Name" v-model="name" />
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input id="email" class="form-control" type="email" placeholder="Email Address" v-model="email" />
      </div>
      <div class="form-group">
        <label for="dateofbirth">Date of Birth</label>
        <input id="dateofbirth" class="form-control" type="date" placeholder="D.O.B" v-model="date_of_birth" />
      </div>
      <div class="form-group gender-div">
        <label>Gender</label>
        <div class="form-control gender">
          <div class="radio-btn">
            <input class="form-check-input" type="radio" id="maleRadioBtn" v-model="gender" value="male" />
            <label class="form-check-label" for="maleRadioBtn"> Male </label>
          </div>
          <div class="radio-btn">
            <input class="form-check-input" type="radio" id="femaleRadioBtn" v-model="gender" value="female" />
            <label class="form-check-label" for="femaleRadioBtn"> Female </label>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="country">Country</label>
        <select class="form-control" id="country" v-model="country">
          <option value="Select">Select</option>
          <option v-for="country in countries" :key="country.id" value="country.id">{{ country.country }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input id="password" class="form-control" type="password" placeholder="Password" v-model="password" />
      </div>
      <div class="form-group">
        <label for="confirmation">Confirm Password</label>
        <input id="confirmation" class="form-control" type="password" placeholder="Confirm Password" v-model="confirmation" />
      </div>
      <div class="submit-btn-div form-group">
        <input class="submit-btn" type="submit" value="Register" />
      </div>
    </form>
  </AuthForm>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import AuthForm from "@/components/AuthForm.vue";
export default {
  name: "RegistrationForm",
  components: { AuthForm },
  data() {
    return {
      name: "",
      username: "",
      email: "",
      date_of_birth: "",
      country: "",
      gender: "",
      password: "",
      confirmation: "",
    };
  },
  computed: {
    ...mapGetters("country", ["countries"]),
  },
  methods: {
    ...mapActions("auth", ["addUser"]),
    ...mapActions("country", ["fetchCountries"]),
    onSubmit(e) {
      e.preventDefault();
      const payload = {
        name: this.name,
        username: this.username,
        email: this.email,
        date_of_birth: this.date_of_birth,
        country_id: this.country,
        gender: this.gender,
        password: this.password,
      };
      if (this.password == this.confirmation) {
        this.addUser(payload);
      }
    },
  },
  created() {
    this.fetchCountries();
  },
};
</script>

<style scoped>
@import "../assets/css/authForm.css";
</style>
