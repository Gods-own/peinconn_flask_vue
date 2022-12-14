import { getAllCountries } from "@/api/backend_helper";

const state = {
  countries: [],
  loading: false,
  error: null,
  success: false,
};

const getters = {
  countries: (state) => state.countries,
  loading: (state) => state.loading,
  error: (state) => state.error,
  success: (state) => state.success,
};

const actions = {
  fetchCountries({ commit }) {
    let isCountryRequestLoading = true;
    commit("countryRequestLoading", isCountryRequestLoading);

    const callGetCountries = async () => {
      const response = await getAllCountries();
      commit("setCountries", response.data);
      return response;
    };

    callGetCountries()
      .then(() => {
        let isCountryRequestLoading = false;
        commit("countryRequestLoading", isCountryRequestLoading);
      })
      .catch((err) => {
        let isCountryRequestLoading = false;
        commit("countryRequestLoading", isCountryRequestLoading);
        commit("countryRequestError", err);
      });
    // try {
    //   commit("setAuthUser", response.data);
    // } catch (error) {
    //   commit("registrationError", error);
    // }
  },
};

const mutations = {
  setCountries: (state, countries) => (state.countries = countries),
  countryRequestError: (state, error) => {
    state.error = error.response.data.message;
  },
  countryRequestLoading: (state, loading) => {
    state.loading = loading;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
