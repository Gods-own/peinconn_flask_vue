<template>
  <div></div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "LogoutForm",
  methods: {
    ...mapActions("auth", ["logoutUser"]),
  },
  created() {
    this.logoutUser();
  },
};
</script>
