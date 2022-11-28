<template>
  <div>
    <CreateActivity v-show="showCreateModal" @hide-modal-func="$emit('hideModalFunc')" />
    <section class="main-section">
      <div class="activity-section">
        <article v-for="singleActivity in allActivities" :key="singleActivity.id" class="card">
          <a class="listing-link">
            <img :src="singleActivity.picture" width="100" height="100" />
          </a>
          <div class="info-container">
            <div class="info-category">
              <i class="fas fa-tag"></i>
              <span>{{ singleActivity.interest.hobby }}</span>
            </div>
            <div class="info-container-item-container">
              <div class="info-container-item">
                <img :src="singleActivity.user.userImage" />
                <p>{{ singleActivity.user.username }}</p>
              </div>
              <div class="info-container-item">
                <small>{{ singleActivity.like_no }}</small>
                <i class="fa fa-heart"></i>
              </div>
            </div>
          </div>
        </article>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import CreateActivity from "@/components/CreateActivity.vue";
import { currUser } from "@/api/jwt-access-token";

export default {
  name: "ActivitiesPage",
  components: { CreateActivity },
  computed: {
    ...mapGetters("activity", ["allActivities"]),
    ...mapGetters("interest", ["userInterests"]),
  },
  methods: {
    ...mapActions("activity", ["fetchActivities"]),
    ...mapActions("interest", ["fetchUserInterests"]),
  },
  data() {
    return {
      showAddModal: false,
      kkk: this.userInterests,
    };
  },
  props: {
    showCreateModal: Boolean,
  },
  emits: ["hideModalFunc"],
  watch: {
    "$store.state.interest.userInterests": function () {
      console.log(this.$store.state.interest.userInterests);
      if (this.$store.state.interest.userInterests == 0) {
        window.location.href = "/register/interest";
        // this.$router.push({ path: "/register/interest" });
      }
    },
  },
  created() {
    this.fetchActivities();
    this.fetchUserInterests(currUser.id);
  },
};
</script>

<style scoped>
@import "../../assets/css/activity.css";
</style>
