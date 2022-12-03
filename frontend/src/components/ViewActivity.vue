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
                  ><h3>{{ activity.user.username }}</h3>
                  <i class="fa fa-envelope"></i
                ></span>
              </div>
            </div>
            <div class="post-user-info-icons">
              <span>{{ activity.like_no }}<i class="fa fa-heart"></i></span>
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
    ...mapActions("likeInfo", ["fetchLikers"]),
  },
  emits: ["hideModalFunc"],
  created() {
    this.fetchLikers(this.activity.id);
  },
};
</script>

<style scoped>
@import "../assets/css/activityView.css";
</style>
