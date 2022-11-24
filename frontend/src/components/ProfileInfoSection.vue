<template>
  <div class="profile-div">
    <!-- <div class="profile-cover">
    <img
        class="profile-cover-photo"
        src="images/07fed676740c12268445f25288b67972.jpg"
    />
    </div> -->
    <div class="profile-header">
      <div class="profile-cover">
        <img class="profile-cover-photo" :src="userProfile.userImage" />
        <div class="profile-action-container">
          <img class="profile-page-img" :src="userProfile.userImage" />
          <div></div>
          <div class="action-btns">
            <button v-if="isAuthenticatedUserProfile">Edit Profile</button>
            <button @click="onMessage" v-else>
              <router-link :to="{ name: 'ChatRoom', params: { userId: userId, room: getRoomName } }">Message</router-link>
            </button>
          </div>
        </div>
      </div>
      <div class="profile-info">
        <h1>{{ userProfile.username }}</h1>
        <p class="profile-bio">{{ userProfile.introduction }}</p>
        <div class="profile-interests">
          <p v-for="interest in userProfile.interests" :key="interest.id"><i class="fa fa-tag"></i>{{ interest.hobby }}</p>
        </div>
      </div>
    </div>
    <div class="profile-filter">
      <button v-for="interest in userProfile.interests" :key="interest.id">{{ interest.hobby }}</button>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import generateName from "../services/generateRoomName.service.js";
// import socketioService from "../services/socketio.service.js";
// import { currUser } from "../api/jwt-access-token";
export default {
  name: "ProfileInfoSection",
  data() {
    return {
      userId: this.$route.params.userId,
      authUser: JSON.parse(localStorage.getItem("authenticatedUser")),
    };
  },
  computed: {
    ...mapGetters("user", ["userProfile"]),
    ...mapGetters("chat", ["roomInfo"]),
    isAuthenticatedUserProfile() {
      let checkifmatch = this.authUser.user.id == this.userId ? true : false;
      return checkifmatch;
    },
    getRoomName() {
      let roomName = this.roomInfo.status ? this.roomInfo.room_name : generateName(this.authUser.user, this.userProfile);
      console.log(roomName);
      return roomName;
    },
  },
  methods: {
    ...mapActions("user", ["fetchUserProfile"]),
    ...mapActions("chat", ["fetchRoomStatus"]),
    // onMessage() {
    //   let socketData = {
    //     username: currUser.username,
    //     room: this.roomName,
    //   };
    //   socketioService.emit("join", JSON.stringify(socketData));
    // },
  },
  created() {
    let authUser = JSON.parse(localStorage.getItem("authenticatedUser"));
    this.fetchUserProfile(this.userId);
    if (authUser.user.id != this.userId) {
      const payload = {
        user1_id: authUser.user.id,
        user2_id: this.userId,
      };
      this.fetchRoomStatus(payload);
    }
  },
};
</script>
