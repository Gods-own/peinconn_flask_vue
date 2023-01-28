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

      <div @click="()=>{joinRoom(room.room, room.user1.id, room.user2.id)}" v-for="room in rooms" :key="room.id" class="messages-list">
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
      <button v-if="roomsPagination?.meta?.paging?.hasNextPage" @click="pagination">Show More</button>
    </div>
  </div>
</template>

<script>
import socketioService from "../services/socketio.service.js";
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
    ...mapGetters("chat", ["rooms", "roomsPagination"]),
  },
  methods: {
    ...mapActions("chat", ["fetchRooms"]),
    pagination() {
      const payload = {
        searchData: {
          filter: undefined,
          page: this.roomsPagination.meta.paging.next_page_num,
          per_page: this.roomsPagination.meta.paging.pageCount,
          max_per_page: this.roomsPagination.meta.paging.pageCount
          }
      }
      this.fetchRooms(payload);
    },
    joinRoom(roomName, userid1, userid2) {
      let socketData = {
        user_id: currUser.id,
        room: roomName,
        user1_id: currUser.id,
        user2_id: userid1 == currUser.id ? userid2 : userid1,
      };
      socketioService.emit("join", JSON.stringify(socketData));
      this.$router.push({ path: `/direct/inbox/${socketData.user2_id}/${socketData.room}` });
    }
  },
  created() {
    this.fetchRooms();
  },
};
</script>
