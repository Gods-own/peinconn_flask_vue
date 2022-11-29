import { registerUser, loginUser } from "@/api/backend_helper";

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
  // addUser({ commit }, registration_payload) {
  //   let isRegFormLoading = true;
  //   commit("formLoading", isRegFormLoading);
  //   console.log(registration_payload);

  //   const callRegisterUser = async () => {
  //     console.log(registration_payload);
  //     const response = await registerUser(registration_payload);
  //     console.log(response);
  //     commit("setAuthUser", response.data);
  //     console.log(response);
  //     return response;
  //   };

  //   callRegisterUser()
  //     .then(() => {
  //       let isRegFormLoading = false;
  //       commit("formLoading", isRegFormLoading);
  //       commit("registrationSuccess");
  //     })
  //     .catch((err) => {
  //       let isRegFormLoading = false;
  //       console.log(err);
  //       commit("formLoading", isRegFormLoading);
  //       commit("registrationError", err);
  //     });
  //   // try {
  //   //   commit("setAuthUser", response.data);
  //   // } catch (error) {
  //   //   commit("registrationError", error);
  //   // }
  // },
  addUser({ commit }, registration_payload) {
    let isFormLoading = true;
    commit("formLoading", isFormLoading);
    console.log([...registration_payload]);

    const callRegisterUser = async () => {
      console.log(registration_payload);
      const response = await registerUser(registration_payload);
      console.log(response);
      commit("setAuthUser", response.data);
      console.log(response);
      return response;
    };

    callRegisterUser()
      .then(() => {
        let isFormLoading = false;
        commit("formLoading", isFormLoading);
        commit("authSuccess");
      })
      .catch((err) => {
        let isFormLoading = false;
        console.log(err);
        commit("formLoading", isFormLoading);
        commit("authError", err);
      });
    // try {
    //   commit("setAuthUser", response.data);
    // } catch (error) {
    //   commit("registrationError", error);
    // }
  },
  authenticateUser({ commit }, login_payload) {
    let isFormLoading = true;
    commit("formLoading", isFormLoading);
    console.log(login_payload);

    const callLoginUser = async () => {
      console.log(login_payload);
      const response = await loginUser(login_payload);
      console.log(response);
      commit("setAuthUser", response.data);
      console.log(response);
      return response;
    };

    callLoginUser()
      .then(() => {
        console.log("here");
        let isFormLoading = false;
        commit("formLoading", isFormLoading);
        commit("authSuccess");
      })
      .catch((err) => {
        let isFormLoading = false;
        console.log(err);
        commit("formLoading", isFormLoading);
        commit("authError", err);
      });
    // try {
    //   commit("setAuthUser", response.data);
    // } catch (error) {
    //   commit("registrationError", error);
    // }
  },
  logoutUser({ commit }) {
    if (localStorage.getItem("authenticatedUser")) {
      localStorage.removeItem("authenticatedUser");
    }
    commit("logoutAuthUser");
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
    if (localStorage.getItem("authenticatedUser")) {
      localStorage.removeItem("authenticatedUser");
    }
    localStorage.setItem("authenticatedUser", parsed);
  },
  logoutAuthUser: () => {
    if (localStorage.getItem("authenticatedUser")) {
      localStorage.removeItem("authenticatedUser");
    }
  },
  authError: (state, error) => {
    state.error = error.response.data.message;
    state.success = false;
  },
  authSuccess: (state) => {
    state.error = null;
    state.success = true;
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
