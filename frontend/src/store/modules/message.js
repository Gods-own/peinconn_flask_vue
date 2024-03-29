import { getUserMessages } from "@/api/backend_helper";

const state = {
  messages: [],
  loading: false,
  error: null,
  success: false,
  messagePagination: {}
};

const getters = {
  messages: (state) => state.messages,
  messagePagination: (state) => state.messagePagination,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  fetchMessages({ commit }, {room_name, searchParams}) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetMessages = async () => {
      const response = await getUserMessages(room_name, searchParams);
      console.log(response);
      commit("setMessages", response.data);
      commit("setPaginationLinks", response.links);
      console.log(response);
      return response;
    };

    callGetMessages()
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
  setMessages: (state, messageList) => {
    state.messages = messageList;
  },
  setPaginationLinks: (state, links) => {
    state.messagePagination = links
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
