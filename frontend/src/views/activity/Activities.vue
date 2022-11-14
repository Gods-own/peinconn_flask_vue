<template>
  <div>
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
export default {
  name: "ActivitiesPage",
  computed: {
    ...mapGetters("activity", ["allActivities"]),
  },
  methods: {
    ...mapActions("activity", ["fetchActivities"]),
  },
  created() {
    this.fetchActivities();
  },
};
</script>

<style scoped>
@import "../../assets/css/activity.css";
</style>
