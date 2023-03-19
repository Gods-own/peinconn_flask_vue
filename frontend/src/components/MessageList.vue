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

      <div @click="()=>{joinRoom(room.room, room.user1.id, room.user2.id)}" v-for="room in allRooms" :key="room.id" class="messages-list">
        <div>
          <img :src="room.user1.id == authUser.id ? room.user2.userImage : room.user1.userImage" />
        </div>
        <div class="messages-list-last">
          <div class="msg">
            <h4>
              <a href="#">{{ room.user1.id == authUser.id ? room.user2.username : room.user1.username }}</a>
            </h4>
            <small>{{ formatDate(room.dm_room[room.dm_room.length - 1].created_At, "YYYY/MM/DD") }}</small>
          </div>
          <div class="msg">
            <p>{{ room.dm_room[room.dm_room.length - 1].content }}</p>
            <!-- <small class v-if="room.dm_room[room.dm_room.length - 1].new_message[0].notification_read == 0 && room.dm_room[room.dm_room.length - 1].new_message[0].notification_user_id == authUser.id">{{  room.dm_room.filter(notifictationFilter).length }}</small> -->
            <small class="new-chat" v-if="room.dm_room[room.dm_room.length - 1].new_message[0].notification_read == 0 && room.dm_room[room.dm_room.length - 1].new_message[0].notification_user_id == authUser.id"><i class="fa fa-circle"></i></small>
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
import moment from "moment";
export default {
  name: "MessageList",
  data() {
    return {
      authUser: currUser,
      allRooms: []
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
      // this.$emit("currentRoom", )
      this.$router.push({ path: `/direct/inbox/${socketData.user2_id}/${socketData.room}` });
    },
    formatDate(date, format){
      let formattedDate = moment(date).format(format)
      return formattedDate
    },
    notifictationFilter(message){
      return message.new_message[0].notification_read == 0
    }
  },
  watch: {
    rooms: {
      handler(newValue){
        this.allRooms = [...this.allRooms, ...newValue];
      },
      deep: true
    }
  },
  created() {
    this.fetchRooms();
  },
};
</script>
