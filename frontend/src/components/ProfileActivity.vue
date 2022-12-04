<template>
  <div class="activity-section">
    <!-- <article class="card">
        <a class="listing-link" href="{% url 'viewPost' activity.id %}">
        <img
            src="images/08ed9bade4dc70528f9bb5a77c2981e6.jpg"
            width="100"
            height="100"
        />
        </a>
    </article> -->
    <article v-for="userActivity in userActivities" :key="userActivity.id" class="card" data-id="1">
      <a class="listing-link">
        <img :src="userActivity.picture" width="100" height="100" />
      </a>
      <div class="profile-info-container">
        <div class="profile-info-category">
          <i class="fas fa-tag"></i>
          <span>{{ userActivity.interest.hobby }}</span>
        </div>
        <div class="profile-info-container-item">
          <small>{{ userActivity.like_no }}</small>
          <i class="fa fa-heart" :class="{ 'liked-color': userActivity.is_liked == true }"></i>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "ProfileActivity",
  data() {
    return {
      userId: this.$route.params.userId,
    };
  },
  computed: {
    ...mapGetters("user", ["userActivities"]),
  },
  methods: {
    ...mapActions("user", ["fetchUserActivities"]),
  },
  created() {
    const payload = {
      user_id: this.userId,
      searchData: undefined,
    };
    this.fetchUserActivities(payload);
  },
};
</script>
