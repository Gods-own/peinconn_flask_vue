import { getAllActivities, createActivity, getSingleActivity } from "@/api/backend_helper";

const state = {
  allActivities: [],
  activity: {},
  loading: false,
  error: null,
  success: false,
  activitiesPagination: {},
};

const getters = {
  allActivities: (state) => state.allActivities,
  activitiesPagination: (state) => state.activitiesPagination,
  activity: (state) => state.activity,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  fetchSingleActivity({ commit }, activity_id) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);

    const callGetSingleActivity = async () => {
      const response = await getSingleActivity(activity_id);
      console.log(response.data.picture);
      commit("setSingleActivity", response.data);
      return response;
    };

    callGetSingleActivity()
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
  fetchActivities({ commit }, { searchParams }) {
    let isRequestLoading = true;
    commit("requestLoading", isRequestLoading);
    console.log(searchParams);

    const callGetAllActivities = async () => {
      const response = await getAllActivities(searchParams);
      console.log(response);
      commit("setActivities", response.data);
      commit("setPaginationLinks", response.links);
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
    console.log(state)
    console.log(activities)
    state.allActivities = [...state.allActivities, ...activities];
  },
  setSingleActivity: (state, activity) => {
    state.activity = activity;
  },
  newActivity: (state, activity) => {
    // photo.liked = false
    state.allActivities.unshift(activity);
  },
  setPaginationLinks: (state, links) => {
    state.activitiesPagination = links;
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
