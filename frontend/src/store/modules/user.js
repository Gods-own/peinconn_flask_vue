import { getUserProfile, getUserActivities } from "@/api/backend_helper";

const state = {
  userProfile: {},
  userActivities: [],
  loading: false,
  error: null,
  success: false,
  activitiesPagination: {}
};

const getters = {
  userActivities: (state) => state.userActivities,
  activitiesPagination: (state) => state.activitiesPagination,
  userProfile: (state) => state.userProfile,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  fetchUserProfile({ commit }, user_id) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetUserProfile = async () => {
      const response = await getUserProfile(user_id);
      console.log(response);
      commit("setUser", response.data);
      console.log(response);
      return response;
    };

    callGetUserProfile()
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
  },
  fetchUserActivities({ commit }, { user_id, searchData }) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetUserActivities = async () => {
      const response = await getUserActivities(user_id, searchData);
      console.log(searchData, response.links);
      commit("setUserActivities", response.data);
      commit("setPaginationLinks", response.links);
      console.log(response);
      return response;
    };

    callGetUserActivities()
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
  },
};

const mutations = {
  setUser: (state, user) => {
    state.userProfile = user;
  },
  setUserActivities: (state, activities) => {
    // state.userActivities = [...state.userActivities, ...activities];
      state.userActivities = activities;
  },
  setPaginationLinks: (state, links) => {
    state.activitiesPagination = links
  },
  requestError: (state, error) => {
    state.error = error.response.data.message;
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
