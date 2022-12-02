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
              <router-link :to="{ name: 'ChatRoom', params: { userId: userProfile.id, room: getRoomName } }">Message</router-link>
            </button>
          </div>
        </div>
      </div>
      <div class="profile-info">
        <h1>{{ userProfile.username }}</h1>
        <p class="profile-bio">{{ userProfile.introduction }}</p>
        <div class="profile-interests">
          <p v-for="interest in userProfile.interests" @click="onFilter(interest.id)" :key="interest.id"><i class="fa fa-tag"></i>{{ interest.hobby }}</p>
        </div>
      </div>
    </div>
    <div class="profile-filter">
      <button v-for="interest in userProfile.interests" @click="onFilter(interest.id)" :key="interest.id">{{ interest.hobby }}</button>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import generateName from "../services/generateRoomName.service.js";
// import socketioService from "../services/socketio.service.js";
import { currUser } from "../api/jwt-access-token";
export default {
  name: "ProfileInfoSection",
  data() {
    return {
      authUser: currUser,
      userId: this.$route.params.userId,
    };
  },
  computed: {
    ...mapGetters("user", ["userProfile"]),
    ...mapGetters("chat", ["roomInfo"]),
    isAuthenticatedUserProfile() {
      let checkifmatch = this.authUser.id == this.userProfile.id ? true : false;
      return checkifmatch;
    },
    getRoomName() {
      let roomName = this.roomInfo.status ? this.roomInfo.room_name : generateName(this.authUser, this.userProfile);
      console.log(roomName, this.roomInfo);
      return roomName;
    },
  },
  methods: {
    ...mapActions("user", ["fetchUserProfile", "fetchUserActivities"]),
    ...mapActions("chat", ["fetchRoomInfo"]),
    onFilter(interest) {
      console.log(interest);
      const payload = {
        user_id: this.userId,
        searchData: { filter: interest },
      };
      console.log(payload);
      this.fetchUserActivities(payload);
    },
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
    console.log(this.$route.params);
    this.fetchUserProfile(this.$route.params.userId);
    if (authUser.user.id != this.$route.params.userId) {
      const payload = {
        user1_id: authUser.user.id,
        user2_id: this.$route.params.userId,
      };
      this.fetchRoomInfo(payload);
    }
  },
};
</script>
