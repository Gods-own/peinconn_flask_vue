import { getAllActivities } from "@/api/backend_helper";

const state = {
  allActivities: [],
  loading: false,
  error: null,
  success: false,
};

const getters = {
  allActivities: (state) => state.allActivities,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  fetchActivities({ commit }) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetAllActivities = async () => {
      const response = await getAllActivities();
      console.log(response);
      commit("setActivities", response.data);
      console.log(response);
      return response;
    };

    callGetAllActivities()
      .then(() => {
        let isRequestLoading = false;
        commit("requestLoading", isRequestLoading);
        commit("requestSuccess");
      })
      .catch((err) => {
        let isRequestLoading = false;
        console.log(err);
        commit("requestLoading", isRequestLoading);
        commit("requestError", err);
      });
    // try {
    //   commit("setAuthUser", response.data);
    // } catch (error) {
    //   commit("registrationError", error);
    // }
  },
};

const mutations = {
  setActivities: (state, activities) => {
    state.allActivities = activities;
  },
  requestError: (state, error) => {
    state.error = error;
    state.success = false;
  },
  requestSuccess: (state) => {
    state.error = null;
    state.success = true;
  },
  requestLoading: (state, loading) => {
    state.loading = loading;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
