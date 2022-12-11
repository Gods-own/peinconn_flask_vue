<template>
  <div>
    <section class="main-section">
      <div class="message-grid">
        <MessageList />
        <MessageView />
      </div>
    </section>
  </div>
</template>

<script>
import socketioService from "../../services/socketio.service.js";
import MessageList from "@/components/MessageList";
import MessageView from "@/components/MessageView";
import { currUser } from "../../api/jwt-access-token.js";
export default {
  name: "DirectInbox",
  components: { MessageList, MessageView },
  data() {
    return {
      roomName: this.$route.params.room,
    };
  },
  created() {
    if (this.$route.params.room) {
      // socketioService.connect();
      // socketioService.on("connect", () => {
      //   console.log(currUser);
      let socketData = {
        username: currUser.username,
        user_id: currUser.id,
        room: this.$route.params.room,
      };
      // console.log(socketData);
      socketioService.emit("userConnected", JSON.stringify(socketData));
      // });
    }
  },
  beforeUnmount() {
    console.log(currUser);
    let socketData = {
      username: currUser.username,
      user_id: currUser.id,
      room: this.roomName,
    };
    console.log(socketData);
    socketioService.emit("userDisconnected", JSON.stringify(socketData));
    // socketioService.disconnect();
  },
};
</script>

<style>
@import "../../assets/css/chatRoom.css";
</style>
