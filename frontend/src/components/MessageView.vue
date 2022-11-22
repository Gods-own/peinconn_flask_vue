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
        <div class="msg-box chat-left">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>Mary</h4> -->
            <pre>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcae vvvv vvvv vvvvb bbvvbb</pre>
            <!-- <small>09/08/2022</small> -->
          </div>
        </div>
        <div class="msg-box chat-right">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>{{message.username.username}}</h4> -->
            <pre>lorem dddd dsjns</pre>
            <!-- <small>{{message.date_added}}</small> -->
          </div>
        </div>

        <div class="clear"></div>
        <div class="msg-box chat-left">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>Mary</h4> -->
            <pre>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcae vvvv vvvv vvvvb bbvvbb</pre>
            <!-- <small>09/08/2022</small> -->
          </div>
        </div>
        <div class="msg-box chat-right">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>{{message.username.username}}</h4> -->
            <pre>lorem dddd dsjns</pre>
            <!-- <small>{{message.date_added}}</small> -->
          </div>
        </div>

        <div class="clear"></div>
        <div class="msg-box chat-left">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>Mary</h4> -->
            <pre>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcae vvvv vvvv vvvvb bbvvbb</pre>
            <!-- <small>09/08/2022</small> -->
          </div>
        </div>
        <div class="msg-box chat-right">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>{{message.username.username}}</h4> -->
            <pre>lorem dddd dsjns</pre>
            <!-- <small>{{message.date_added}}</small> -->
          </div>
        </div>

        <div class="clear"></div>
        <div class="msg-box chat-left">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>Mary</h4> -->
            <pre>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcae vvvv vvvv vvvvb bbvvbb</pre>
            <!-- <small>09/08/2022</small> -->
          </div>
        </div>
        <div class="msg-box chat-right">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>{{message.username.username}}</h4> -->
            <pre>lorem dddd dsjns</pre>
            <!-- <small>{{message.date_added}}</small> -->
          </div>
        </div>

        <div class="clear"></div>
        <div class="msg-box chat-left">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>Mary</h4> -->
            <pre>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcae vvvv vvvv vvvvb bbvvbb</pre>
            <!-- <small>09/08/2022</small> -->
          </div>
        </div>
        <div class="msg-box chat-right">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>{{message.username.username}}</h4> -->
            <pre>lorem dddd dsjns</pre>
            <!-- <small>{{message.date_added}}</small> -->
          </div>
        </div>

        <div class="clear"></div>
        <div class="msg-box chat-left">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>Mary</h4> -->
            <pre>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcae vvvv vvvv vvvvb bbvvbb</pre>
            <!-- <small>09/08/2022</small> -->
          </div>
        </div>
        <div class="msg-box chat-right">
          <!-- <img
                    class="msg-box-img"
                    src="{% if message.username.userImage %}{{ message.username.userImage.url}}{% else %}#{% endif %}"
                  /> -->
          <div class="msg-box-div">
            <!-- <h4>{{message.username.username}}</h4> -->
            <pre>lorem dddd dsjns</pre>
            <!-- <small>{{message.date_added}}</small> -->
          </div>
        </div>

        <div class="clear"></div>
      </div>
    </div>

    <div class="chat-form">
      <form @submit="sendChat" class="form-message" method="POST">
        <input id="chat-message-input" type="text" />
        <button id="chat-message-submit" type="submit">
          <i class="fa fa-paper-plane"></i>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import socketioService from "../services/socketio.service.js";
export default {
  name: "MessageView",
  methods: {
    sendChat(e) {
      e.preventDefault();
      socketioService.on("");
    },
  },
};
</script>
