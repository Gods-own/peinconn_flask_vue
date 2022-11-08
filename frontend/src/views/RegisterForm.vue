<template>
  <AuthForm>
    <form class="login-register-form" method="post">
      <div class="form-header">
        <input type="text" class="invinscible" v-model="good" />
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
        <label for="email">Email</label>
        <input id="email" class="form-control" type="email" placeholder="Email Address" v-model="email" />
      </div>
      <div class="form-group">
        <label for="dateofbirth">Date of Birth</label>
        <input id="dateofbirth" class="form-control" type="date" placeholder="D.O.B" v-model="dateofbirth" />
      </div>
      <div class="form-group gender-div">
        <label>Gender</label>
        <div class="form-control gender">
          <div class="radio-btn">
            <input class="form-check-input" type="radio" id="maleRadioBtn" v-model="male" />
            <label class="form-check-label" for="maleRadioBtn"> Male </label>
          </div>
          <div class="radio-btn">
            <input class="form-check-input" type="radio" id="femaleRadioBtn" v-model="female" />
            <label class="form-check-label" for="femaleRadioBtn"> Female </label>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="country">Country</label>
        <select class="form-control" id="country" v-model="country">
          <option value="Select">Select</option>
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
import AuthForm from "@/components/AuthForm.vue";
export default {
  name: "RegisterForm",
  components: { AuthForm },
};
</script>
