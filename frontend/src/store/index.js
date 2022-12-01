import { createStore } from "vuex";

import auth from "./modules/auth";
import country from "./modules/country";
import interest from "./modules/interest";
import activity from "./modules/activity";
import user from "./modules/user";
import chat from "./modules/chat";
import message from "./modules/message";
import search from "./modules/search";

export default createStore({
  modules: {
    auth: {
      namespaced: true,
      ...auth,
    },
    country: {
      namespaced: true,
      ...country,
    },
    activity: {
      namespaced: true,
      ...activity,
    },
    interest: {
      namespaced: true,
      ...interest,
    },
    user: {
      namespaced: true,
      ...user,
    },
    chat: {
      namespaced: true,
      ...chat,
    },
    message: {
      namespaced: true,
      ...message,
    },
    search: {
      namespaced: true,
      ...search,
    },
  },
});
