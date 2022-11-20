import { getAllUserInterests, getAllInterests } from "@/api/backend_helper";

const state = {
  interests: [],
  userInterests: [],
  loading: false,
  error: null,
  success: false,
};

const getters = {
  interests: (state) => state.interests,
  userInterests: (state) => state.userInterests,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  fetchInterests({ commit }) {
    let isInterestRequestLoading = true;
    commit("interestRequestLoading", isInterestRequestLoading);

    const callGetInterests = async () => {
      const response = await getAllInterests();
      commit("setInterests", response.data);
      return response;
    };

    callGetInterests()
      .then(() => {
        let isInterestRequestLoading = false;
        commit("interestRequestLoading", isInterestRequestLoading);
      })
      .catch((err) => {
        let isInterestRequestLoading = false;
        commit("interestRequestLoading", isInterestRequestLoading);
        commit("interestRequestError", err);
      });
  },

  fetchUserInterests({ commit }) {
    let isInterestRequestLoading = true;
    commit("interestRequestLoading", isInterestRequestLoading);

    const callGetUserInterests = async () => {
      const response = await getAllUserInterests();
      commit("setUserInterests", response.data);
      return response;
    };

    callGetUserInterests()
      .then(() => {
        let isInterestRequestLoading = false;
        commit("interestRequestLoading", isInterestRequestLoading);
      })
      .catch((err) => {
        let isInterestRequestLoading = false;
        commit("interestRequestLoading", isInterestRequestLoading);
        commit("interestRequestError", err);
      });
  },
};

const mutations = {
  setInterests: (state, interests) => (state.interests = interests),
  setUserInterests: (state, user_interests) => (state.userInterests = user_interests),
  interestRequestError: (state, error) => {
    state.error = error;
  },
  interestRequestLoading: (state, loading) => {
    state.loading = loading;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
