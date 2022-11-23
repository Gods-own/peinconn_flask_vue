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
export default {
  name: "DirectInbox",
  components: { MessageList, MessageView },
  created() {
    socketioService.on("connect", () => {
      alert("connected");
    });
  },
  beforeUnmount() {
    socketioService.disconnect();
  },
};
</script>

<style>
@import "../../assets/css/chatRoom.css";
</style>
