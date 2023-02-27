<template>
  <ModalComponent @hide-modal-func="$emit('hideModalFunc')">
    <div class="post-view-div">
      <img class="post-view-img" :src="activity.picture" />
      <section class="post-view-info">
        <header v-if="activity.user" class="post-view-header">
          <div class="post-user-info-cotainer">
            <div class="post-user-info-group">
              <img :src="activity.user.userImage" />
              <div>
                <span
                  ><h3><router-link :to="{ name: 'Profile', params:{userId: activity.user.id} }">{{ activity.user.username }}</router-link></h3>
                  <i class="fa fa-envelope"></i
                ></span>
              </div>
            </div>
            <div class="post-user-info-icons">
              <span
                >{{ activity.like_no }} <i class="fa fa-heart" @click="toggleLike($event, activity.id)" :class="{ 'liked-color': activity.is_liked == true }"></i
              ></span>
            </div>
          </div>
          <p>{{ activity.activity }}</p>
        </header>
        <div class="post-view-body">
          <p>Liked By</p>
          <div class="post-view-likers">
            <div v-for="liker in likers" :key="liker.id">
              <img :src="liker.user.userImage" />
              <p>{{ liker.user.username }}</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  </ModalComponent>
</template>

<script>
import ModalComponent from "@/components/Modal.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "ViewActivity",
  components: { ModalComponent },
  computed: {
    ...mapGetters("likeInfo", ["likers"]),
    ...mapGetters("activity", ["activity"]),
  },
  methods: {
    ...mapActions("likeInfo", ["fetchLikers", "setToggleLike", "fetchLikeStatus"]),
    toggleLike(e, activity_id) {
      this.setToggleLike(activity_id);
      let gff = e.target.previousSibling.innerText;
      console.log(gff.trim());
      // if (e.target.classList.contains("liked-color")) {
      //   console.log(e.target.previousSibling.innerText.trim());
      //   e.target.previousSibling.innerText = parseInt(e.target.previousSibling.innerText.trim()) - 1;
      // } else {
      //   e.target.previousSibling.innerText = parseInt(e.target.previousSibling.innerText.trim()) + 1;
      // }
      e.target.classList.toggle("liked-color");
    },
  },
  emits: ["hideModalFunc"],
  created() {
    console.log('dds')
    this.fetchLikers(this.activity.id);
  },
};
</script>

<style scoped>
@import "../assets/css/activityView.css";
</style>
