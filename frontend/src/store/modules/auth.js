import { registerUser } from "@/api/backend_helper";

const state = {
  loading: false,
  error: null,
  success: false,
};

const getters = {
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  addUser({ commit }, registration_payload) {
    let isRegFormLoading = true;
    commit("formLoding", isRegFormLoading);

    const callRegisterUser = async () => {
      const response = await registerUser(registration_payload);
      commit("setAuthUser", response.data);
      return response;
    };

    callRegisterUser()
      .then(() => {
        let isRegFormLoading = false;
        commit("formLoading", isRegFormLoading);
      })
      .catch((err) => {
        let isRegFormLoading = false;
        commit("formLoading", isRegFormLoading);
        commit("registrationError", err);
      });
    // try {
    //   commit("setAuthUser", response.data);
    // } catch (error) {
    //   commit("registrationError", error);
    // }
  },
};

const mutations = {
  setAuthUser: (state, user) => {
    const parsed = JSON.stringify(user);
    localStorage.setItem("authenticatedUser", parsed);
  },
  registrationError: (state, error) => {
    state.error = error;
  },
  formLoading: (state, loading) => {
    state.loading = loading;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
