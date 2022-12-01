import { searchUser } from "@/api/backend_helper";

const state = {
  searchResult: [],
  loading: false,
  error: null,
  success: false,
};

const getters = {
  searchResult: (state) => state.searchResult,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  searchUsers({ commit }, searchParams) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callSearchUser = async () => {
      const response = await searchUser(searchParams);
      console.log(searchParams);
      commit("setSearchResult", response.data);
      console.log(response);
      return response;
    };

    callSearchUser()
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
    setSearchResult: (state, searchdata) => {
    state.searchResult = searchdata;
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