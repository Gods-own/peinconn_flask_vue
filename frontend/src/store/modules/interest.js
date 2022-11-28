import { getAllUserInterests, getAllInterests, registerUserInterest } from "@/api/backend_helper";

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
  addInterest({ commit }, interestPayload) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);
    console.log([...interestPayload]);

    const callRegisterUserInterest = async () => {
      console.log(interestPayload);
      const response = await registerUserInterest(interestPayload);
      console.log(response);
      commit("newInterest", response.data);
      console.log(response);
      return response;
    };

    callRegisterUserInterest()
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
  fetchInterests({ commit }) {
    let isInterestRequestLoading = true;
    commit("requestLoading", isInterestRequestLoading);

    const callGetInterests = async () => {
      const response = await getAllInterests();
      commit("setInterests", response.data);
      return response;
    };

    callGetInterests()
      .then(() => {
        let isInterestRequestLoading = false;
        commit("requestLoading", isInterestRequestLoading);
      })
      .catch((err) => {
        let isInterestRequestLoading = false;
        commit("requestLoading", isInterestRequestLoading);
        commit("requestError", err);
      });
  },

  fetchUserInterests({ commit }, user_id) {
    let isInterestRequestLoading = true;
    commit("requestLoading", isInterestRequestLoading);

    const callGetUserInterests = async () => {
      const response = await getAllUserInterests(user_id);
      commit("setUserInterests", response.data);
      return response;
    };

    callGetUserInterests()
      .then(() => {
        let isInterestRequestLoading = false;
        commit("requestLoading", isInterestRequestLoading);
      })
      .catch((err) => {
        let isInterestRequestLoading = false;
        commit("requestLoading", isInterestRequestLoading);
        commit("requestError", err);
      });
  },
};

const mutations = {
  newInterest: (state, interest) => {
    // photo.liked = false
    state.userInterests.unshift(interest);
  },
  setInterests: (state, interests) => (state.interests = interests),
  setUserInterests: (state, user_interests) => (state.userInterests = user_interests),
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
