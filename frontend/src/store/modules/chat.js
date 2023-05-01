import { getRoomStatus, getUserRooms } from "@/api/backend_helper";

const state = {
  roomInfo: {},
  rooms: [],
  loading: false,
  error: null,
  success: false,
  roomsPagination: {}
};

const getters = {
  roomInfo: (state) => state.roomInfo,
  roomsPagination: (state) => state.roomsPagination,
  rooms: (state) => state.rooms,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  fetchRoomInfo({ commit }, { user1_id, user2_id }) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetRoomInfo = async () => {
      const response = await getRoomStatus(user1_id, user2_id);
      console.log(response);
      commit("setRoomInfo", response.data);
      console.log(response);
      return response;
    };

    callGetRoomInfo()
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

  fetchRooms({ commit }, {searchParams}) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetRooms = async () => {
      const response = await getUserRooms(searchParams);
      console.log(response);
      commit("setRooms", response.data);
      commit("setPaginationLinks", response.links);
      console.log(response);
      return response;
    };

    callGetRooms()
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
  setRoomInfo: (state, roomdata) => {
    state.roomInfo = roomdata;
  },
  setRooms: (state, roomList) => {
    state.rooms = roomList;
  },
  setPaginationLinks: (state, links) => {
    state.roomsPagination = links
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
