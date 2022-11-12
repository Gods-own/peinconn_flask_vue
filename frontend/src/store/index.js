import { createStore } from "vuex";

import auth from "./modules/auth";
import country from "./modules/country";

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
  },
});
