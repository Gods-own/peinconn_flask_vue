<template>
  <div class="msg-div">
    <header class="msg-header">
      <div>
        <div class="message-img-div">
          <img src="images/08ed9bade4dc70528f9bb5a77c2981e6.jpg" />
          <p>Tolu</p>
        </div>
      </div>
      <ul class="msg-header-ul">
        <li>
          <a href=""><i class="fa fa-eye"></i></a>
        </li>
      </ul>
    </header>

    <div class="msg-div-last-child" id="chat-messages">
      <div>
        <div
          v-for="message in messages"
          :key="message.id"
          class="msg-box"
          :class="{ 'chat-left': message.user.id != authUser.id, 'chat-right': message.user.id == authUser.id }"
        >
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>Mary</h4> -->
            <pre>{{ message.content }}</pre>
            <!-- <small>09/08/2022</small> -->
          </div>
        </div>
        <div class="clear"></div>
      </div>
    </div>

    <div class="chat-form">
      <form @submit="sendChat" class="form-message" method="POST">
        <input id="chat-message-input" v-model="chat_message" type="text" />
        <button id="chat-message-submit" type="submit">
          <i class="fa fa-paper-plane"></i>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import socketioService from "../services/socketio.service.js";
import { mapGetters, mapActions } from "vuex";
import { currUser } from "../api/jwt-access-token";
export default {
  name: "MessageView",
  data() {
    return {
      chat_message: "",
      authUser: currUser,
      roomName: this.$route.params.room,
      cvv: 0,
    };
  },
  computed: {
    ...mapGetters("message", ["messages"]),
  },
  methods: {
    ...mapActions("message", ["fetchMessages"]),
    sendChat(e) {
      e.preventDefault();
      let socketData = {
        user_id: currUser.id,
        room: this.roomName,
        message: this.chat_message,
        user1_id: currUser.id,
        user2_id: this.$route.params.userId,
      };
      socketioService.emit("join", JSON.stringify(socketData));
      this.chat_message = "";
    },
  },
  created() {
    socketioService.on("new_message", (data) => {
      let new_messages = this.messages.unshift(data);
      // this.$store.commit("setMessages", new_messages);
      console.log(data);
      console.log(new_messages);
      console.log(this.messages);
    });
    this.fetchMessages(this.$route.params.room);
  },
  Unmounted() {
    socketioService.emit("leave", JSON.stringify({ msg: "has left" }));
  },
  // mounted() {
  //   this.fetchMessages(this.$route.params.room);
  //   console.log("jjjj");
  // },
};
</script>
