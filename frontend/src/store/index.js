import { createStore } from "vuex";

import auth from "./modules/auth";
import country from "./modules/country";
import activity from "./modules/activity";

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
  },
});
