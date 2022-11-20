import { io } from "socket.io-client";

class SocketioService {
  socket;
  constructor() {}

  setupSocketConnection() {
    this.socket = io(process.env.VUE_APP_SOCKET_ENDPOINT);
    this.socket.on("connect", () => {
      //   alert(data);
      //   console.log(data);
      console.log(window.location);
      this.socket.emit("my message", "Hello there from Vue.");
    });
    this.socket.on("my broadcast", (data) => {
      alert(data.data);
      console.log(data.data);
    });
  }
  disconnect() {
    if (this.socket) {
      this.socket.disconnect();
    }
  }
}

export default new SocketioService();
