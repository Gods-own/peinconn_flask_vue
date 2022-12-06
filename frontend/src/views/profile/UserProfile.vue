<template>
  <div>
    <section class="main-section">
      <ProfileInfoSection></ProfileInfoSection>
      <div class="divider"></div>
      <ProfileActivity
        :viewActivity="viewActivity"
        @hide-modal-func="$emit('hideModalFunc')"
        @show-activity-modal-func="$emit('showActivityModalFunc')"
      ></ProfileActivity>
    </section>
  </div>
</template>

<script>
import ProfileInfoSection from "@/components/ProfileInfoSection.vue";
import ProfileActivity from "@/components/ProfileActivity.vue";
export default {
  name: "UserProfile",
  components: { ProfileInfoSection, ProfileActivity },
  emits: ["hideModalFunc", "showActivityModalFunc"],
  props: {
    viewActivity: Boolean,
  },
};
</script>

<style>
@import "../../assets/css/profile.css";
</style>
