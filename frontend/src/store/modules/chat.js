import { getRoomStatus } from "@/api/backend_helper";

const state = {
  roomInfo: false,
  loading: false,
  error: null,
  success: false,
};

const getters = {
  roomInfo: (state) => state.roomInfo,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  fetchRoomStatus({ commit }, { user1_id, user2_id }) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetRoomStatus = async () => {
      const response = await getRoomStatus(user1_id, user2_id);
      console.log(response);
      commit("setRoomStatus", response.data);
      console.log(response);
      return response;
    };

    callGetRoomStatus()
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
  setRoomStatus: (state, roomInfo) => {
    state.roomStatus = roomInfo;
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
