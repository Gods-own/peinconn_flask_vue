import { getLikers, toggleLike, likeStatus } from "@/api/backend_helper";

const state = {
  likers: [],
  likeStatus: {},
  loading: false,
  error: null,
  success: false,
};

const getters = {
  likers: (state) => state.likers,
  likeStatus: (state) => state.likeStatus,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  fetchLikers({ commit }, activity_id) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetLikers = async () => {
      const response = await getLikers(activity_id);
      console.log(response);
      commit("setLikers", response.data);
      console.log(response);
      return response;
    };

    callGetLikers()
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

  setToggleLike({ commit }, activity_id) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callToggleLike = async () => {
      const response = await toggleLike(activity_id);
      console.log(response);
      return response;
    };

    callToggleLike()
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

  fetchLikeStatus({ commit }, activity_id) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetLikeStatus = async () => {
      const response = await likeStatus(activity_id);
      console.log(response);
      commit("setLikeStatus", response.data);
      console.log(response);
      return response;
    };

    callGetLikeStatus()
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
  setLikers: (state, likersInfo) => {
    state.likers = likersInfo;
  },
  setLikeStatus: (state, status) => {
    state.likeStatus = status;
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
