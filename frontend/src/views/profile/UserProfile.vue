<template>
  <div>
    <section class="main-section">
      <ProfileInfoSection></ProfileInfoSection>
      <div class="divider"></div>
      <ProfileActivity></ProfileActivity>
    </section>
  </div>
</template>

<script>
import ProfileInfoSection from "@/components/ProfileInfoSection.vue";
import ProfileActivity from "@/components/ProfileActivity.vue";
export default {
  name: "UserProfile",
  components: { ProfileInfoSection, ProfileActivity },
};
</script>

<style>
@import "../../assets/css/profile.css";
</style>
