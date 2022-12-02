import { getAllActivities, createActivity } from "@/api/backend_helper";

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
  fetchActivities({ commit }, searchParams) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetAllActivities = async () => {
      const response = await getAllActivities(searchParams);
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
  },

  addActivity({ commit }, activity_data) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);
    console.log([...activity_data]);

    const callCreateActivity = async () => {
      console.log(activity_data);
      const response = await createActivity(activity_data);
      console.log(response);
      commit("newActivity", response.data);
      console.log(response);
      return response;
    };

    callCreateActivity()
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
  setActivities: (state, activities) => {
    state.allActivities = activities;
  },
  newActivity: (state, activity) => {
    // photo.liked = false
    state.allActivities.unshift(activity);
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
