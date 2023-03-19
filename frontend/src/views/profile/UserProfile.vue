<template>
  <div>
    <section class="main-section">
      <ProfileInfoSection @change-interest-activities="saveInterestName"></ProfileInfoSection>
      <div class="divider"></div>
      <ProfileActivity
      :hobby="interestName"
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
  data(){
    return{
      interestName: ""
    }
  },
  components: { ProfileInfoSection, ProfileActivity },
  emits: ["showActivityModalFunc"],
  // props: {
  //   viewActivity: Boolean,
  // },
  methods:{
    saveInterestName(hobbyName){
      this.interestName = hobbyName
    }
  }
};
</script>

<style>
@import "../../assets/css/profile.css";
</style>
