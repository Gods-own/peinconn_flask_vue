<template>
  <div v-if="$route.params.userId" class="msg-div">
    <header class="msg-header">
      <div>
        <div class="message-img-div">
          <img :src="userProfile.userImage" />
          <p>{{ userProfile.username }}</p>
        </div>
      </div>
      <ul class="msg-header-ul">
        <li>
          <router-link :to="{ name: 'Profile', params:{ userId: $route.params.userId } }"><i class="fa fa-eye"></i></router-link>
        </li>
      </ul>
    </header>

    <div class="msg-div-last-child" id="chat-messages">
      <div v-for="message in allMessages" :key="message.id" class="chat-container" :class="{ 'chat-left': message.user.id != authUser.id, 'chat-right': message.user.id == authUser.id }">
        <div
          class="msg-box"
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
        <!-- <div class="clear"></div> -->
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
  <div v-else class="msg-div"></div>
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
      allMessages: []
    };
  },
  watch:{
    $route (to){
        this.fetchMessages(to.params.room);
    },
    '$route.params.userId': function() {
            this.fetchUserProfile(this.$route.params.userId)
    },
    messages: {
      handler(newValue){
        this.allMessages = [...this.allMessages, ...newValue];
      },
      deep: true
    }
},
  computed: {
    ...mapGetters("message", ["messages"]),
    ...mapGetters("user", ["userProfile"]),
  },
  methods: {
    ...mapActions("message", ["fetchMessages"]),
    ...mapActions("user", ["fetchUserProfile"]),
    sendChat(e) {
      e.preventDefault();
      let socketData = {
        user_id: currUser.id,
        room: this.roomName,
        message: this.chat_message,
        user1_id: currUser.id,
        user2_id: this.$route.params.userId,
      };
      socketioService.emit("message", JSON.stringify(socketData));
      this.chat_message = "";
    },
  },
  mounted(){
    this.fetchUserProfile(this.$route.params.userId)
    console.log(this.$route.params.userId)
  },
  created() {
    socketioService.on("new_message", (data) => {
      this.messages.unshift(data);
      // this.$store.commit("setMessages", new_messages);
    });
    // socketioService.on("received", () => {
    //   alert("reciebed");
    //   this.fetchUserProfile(this.authUser.id);
    // });
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
