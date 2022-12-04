import { getLikers, toggleLike, likeStatus } from "@/api/backend_helper";

const state = {
  likers: [],
  likeStatus: false,
  likeNo: 0,
  loading: false,
  error: null,
  success: false,
};

const getters = {
  likers: (state) => state.likers,
  likeStatus: (state) => state.likeStatus,
  likeNo: (state) => state.likeNo,
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
      commit("setLikeStatus", response.data.is_liked);
      commit("setLikeNo", response.data.like_no);
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
      commit("setLikeStatus", response.data.is_liked);
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
  setLikeNo: (state, like_no) => {
    state.likeNo = like_no;
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
