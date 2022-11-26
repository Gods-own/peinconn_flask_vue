<template>
  <div class="messages-list-container">
    <div class="messages-list-header">
      <h2>Messages</h2>
    </div>
    <div class="message-list-form-container">
      <form class="message-search-form">
        <button class="search-back-btn">
          <i class="fa fa-arrow-left"></i>
        </button>
        <input class="message-search-input" type="search" placeholder="Search" />
      </form>

      <div v-for="room in rooms" :key="room.id" class="messages-list">
        <div>
          <img :src="room.user1.id == authUser.id ? room.user2.userImage : room.user1.userImage" />
        </div>
        <div class="messages-list-last">
          <div class="msg">
            <h4>
              <a href="#">{{ room.user1.id == authUser.id ? room.user2.username : room.user1.username }}</a>
            </h4>
            <small>07/09/22</small>
          </div>
          <div class="msg">
            <p>Lorem ipsum dolor</p>
            <small>2</small>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import { currUser } from "../api/jwt-access-token";
export default {
  name: "MessageList",
  data() {
    return {
      authUser: currUser,
    };
  },
  computed: {
    ...mapGetters("chat", ["rooms"]),
  },
  methods: {
    ...mapActions("chat", ["fetchRooms"]),
  },
  created() {
    this.fetchRooms();
  },
};
</script>
