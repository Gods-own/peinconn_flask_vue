<template>
  <div>
    <!-- <CreateActivity v-if="showCreateModal" @hide-modal-func="$emit('hideModalFunc')" /> -->
    <!-- <ViewActivity v-if="viewActivity" @hide-modal-func="$emit('hideModalFunc')" /> -->
    <section class="main-section">
      <div class="activity-section">
        <article v-for="singleActivity in ndsu" :key="singleActivity.id" class="card">
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
                <p><router-link :to="{ name: 'Profile', params:{userId: singleActivity.user.id} }">{{ singleActivity.user.username }}</router-link></p>
              </div>
              <div class="info-container-item">
                <small>{{ singleActivity.like_no }}</small>
                <i @click="toggleLike($event, singleActivity.id)" class="fa fa-heart" :class="{ 'liked-color': singleActivity.is_liked == true }"></i>
              </div>
            </div>
          </div>
        </article>
        <button v-if="activitiesPagination?.meta?.paging?.hasNextPage" @click="pagination">Show More</button>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapState, mapActions, mapMutations } from "vuex";
// import CreateActivity from "@/components/CreateActivity.vue";
// import ViewActivity from "@/components/ViewActivity.vue";
import { currUser } from "@/api/jwt-access-token";

export default {
  name: "ActivitiesPage",
  // components: { ViewActivity },
  data() {
    return {
      jdk: []
    }
  },
  computed: {
    ...mapState("activity", ["allActivities", "activitiesPagination"]),
    ...mapGetters("interest", ["userInterests"]),
    ...mapGetters("likeInfo", ["likeStatus", "likeNo"]),
    ndsu(){
      const jrdk = this.jdk; 
      const hjgy = [...jrdk, ...this.allActivities];
      this.jdk = [...hjgy];
      return hjgy;
    }
  },
  methods: {
    ...mapActions("activity", ["fetchActivities", "fetchSingleActivity"]),
    ...mapActions("interest", ["fetchUserInterests"]),
    ...mapActions("likeInfo", ["setToggleLike", "fetchLikeStatus"]),
    ...mapMutations("activity", ["setActivities"]),
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
    pagination() {
      const payload = {
        searchParams: {
          filter: undefined,
          page: this.activitiesPagination.meta.paging.next_page_num,
          per_page: this.activitiesPagination.meta.paging.pageCount,
          max_per_page: this.activitiesPagination.meta.paging.pageCount,
        },
      };
      this.fetchActivities(payload);
    },
    // getNextSetActivities() {
    //   window.onscroll = () => {
    //     let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
    //     if (bottomOfWindow) {
    //       // axios.get(`https://randomuser.me/api/`).then(response => {
    //       //   this.users.push(response.data.results[0]);
    //       // });
    //       this.pagination();
    //     }
    //   }
    // }
  },
  // props: {
  //   // showCreateModal: Boolean,
  //   viewActivity: Boolean,
  // },
  emits: ["showActivityModalFunc"],
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
    const payload = {
      searchParams: {
        filter: undefined,
      },
    };
    this.fetchActivities(payload);
    this.fetchUserInterests(currUser.id);
  },
  // mounted() {
  //   this.getNextSetActivities();
  // },
  beforeUnmount(){
    // const state = {
    //   allActivities: []
    // }
    const activities = []
    this.setActivities(activities)
  }
};
</script>

<style scoped>
@import "../../assets/css/activity.css";
</style>
