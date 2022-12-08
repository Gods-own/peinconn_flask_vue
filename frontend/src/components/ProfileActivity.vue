<template>
  <div class="activity-section">
    <!-- <ViewActivity v-if="viewActivity" @hide-modal-func="$emit('hideModalFunc')" /> -->
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
        <img :src="userActivity.picture" @click="showActivityModal(userActivity.id)" width="100" height="100" />
      </a>
      <div class="profile-info-container">
        <div class="profile-info-category">
          <i class="fas fa-tag"></i>
          <span>{{ userActivity.interest.hobby }}</span>
        </div>
        <div class="profile-info-container-item">
          <small>{{ userActivity.like_no }}</small>
          <i @click="toggleLike($event, userActivity.id)" class="fa fa-heart" :class="{ 'liked-color': userActivity.is_liked == true }"></i>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
// import ViewActivity from "@/components/ViewActivity.vue";
export default {
  name: "ProfileActivity",
  // components: { ViewActivity },
  data() {
    return {
      userId: this.$route.params.userId,
    };
  },
  // props: {
  //   viewActivity: Boolean,
  // },
  computed: {
    ...mapGetters("user", ["userActivities"]),
  },
  methods: {
    ...mapActions("activity", ["fetchSingleActivity"]),
    ...mapActions("user", ["fetchUserActivities"]),
    ...mapActions("likeInfo", ["setToggleLike", "fetchLikeStatus"]),
    toggleLike(e, activity_id) {
      this.setToggleLike(activity_id);
      if (e.target.classList.contains("liked-color")) {
        e.target.previousElementSibling.innerText = parseInt(e.target.previousElementSibling.innerText) - 1;
      } else {
        e.target.previousElementSibling.innerText = parseInt(e.target.previousElementSibling.innerText) + 1;
      }
      e.target.classList.toggle("liked-color");
    },
    showActivityModal(id) {
      this.fetchSingleActivity(id);
      this.$emit("showActivityModalFunc");
    },
  },
  emits: ["showActivityModalFunc"],
  created() {
    const payload = {
      user_id: this.userId,
      searchData: undefined,
    };
    this.fetchUserActivities(payload);
  },
};
</script>
