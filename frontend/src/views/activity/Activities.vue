<template>
  <div>
    <CreateActivity v-if="showCreateModal" @hide-modal-func="$emit('hideModalFunc')" />
    <ViewActivity v-if="viewActivity" @hide-modal-func="$emit('hideModalFunc')" />
    <section class="main-section">
      <div class="activity-section">
        <article v-for="singleActivity in allActivities" :key="singleActivity.id" class="card">
          <a class="listing-link">
            <img :src="singleActivity.picture" @click="showActivityModal(singleActivity.id)" width="100" height="100" />
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
                <i @click="toggleLike($event, singleActivity.id)" class="fa fa-heart" :class="{ 'liked-color': singleActivity.is_liked == true }"></i>
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
import ViewActivity from "@/components/ViewActivity.vue";
import { currUser } from "@/api/jwt-access-token";

export default {
  name: "ActivitiesPage",
  components: { CreateActivity, ViewActivity },
  computed: {
    ...mapGetters("activity", ["allActivities"]),
    ...mapGetters("interest", ["userInterests"]),
    ...mapGetters("likeInfo", ["likeStatus", "likeNo"]),
  },
  methods: {
    ...mapActions("activity", ["fetchActivities", "fetchSingleActivity"]),
    ...mapActions("interest", ["fetchUserInterests"]),
    ...mapActions("likeInfo", ["setToggleLike", "fetchLikeStatus"]),
    showActivityModal(id) {
      this.fetchSingleActivity(id);
      this.$emit("showActivityModalFunc");
    },
    toggleLike(e, activity_id) {
      this.setToggleLike(activity_id);
      if (e.target.classList.contains("liked-color")) {
        e.target.previousElementSibling.innerText = parseInt(e.target.previousElementSibling.innerText) - 1;
      } else {
        e.target.previousElementSibling.innerText = parseInt(e.target.previousElementSibling.innerText) + 1;
      }
      e.target.classList.toggle("liked-color");
    },
  },
  props: {
    showCreateModal: Boolean,
    viewActivity: Boolean,
  },
  emits: ["hideModalFunc", "showActivityModalFunc"],
  watch: {
    "$store.state.interest.userInterests": function () {
      console.log(this.$store.state.interest.userInterests);
      if (this.$store.state.interest.userInterests == 0) {
        window.location.href = "/register/interest";
        // this.$router.push({ path: "/register/interest" });
      }
    },
    // "$store.state.interest.likeNo": function () {
    //   console.log(this.$store.state.interest.userInterests);
    //   if (this.$store.state.interest.userInterests == 0) {
    //     window.location.href = "/register/interest";
    //     // this.$router.push({ path: "/register/interest" });
    //   }
    // },
  },
  created() {
    console.log("good");
    this.fetchActivities();
    this.fetchUserInterests(currUser.id);
  },
};
</script>

<style scoped>
@import "../../assets/css/activity.css";
</style>
