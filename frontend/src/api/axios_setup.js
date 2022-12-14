import axios from "axios";
import accessToken from "./jwt-access-token";

//pass new generated access token here
const token = accessToken;

//apply base url for axios
const API_URL = process.env.VUE_APP_PEINCONN_APIURL;

const axiosApi = axios.create({
  baseURL: API_URL,
  // headers: { "content-type": "application/x-www-form-urlencoded" },
});

axiosApi.defaults.headers.common["Authorization"] = "Bearer " + token;
// axiosApi.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

axiosApi.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject(error)
);

export async function get(url, config = {}) {
  return await axiosApi.get(url, { ...config }).then((response) => response.data);
}

export async function post(url, data, config = {}) {
  return axiosApi.post(url, { ...data }, { transformRequest: () => data, ...config }).then((response) => response.data);
}

export async function put(url, data, config = {}) {
  return axiosApi.put(url, { ...data }, { ...config }).then((response) => response.data);
}

export async function patch(url, data, config = {}) {
  return axiosApi.patch(url, { ...data }, { ...config }).then((response) => response.data);
}

export async function del(url, config = {}) {
  return await axiosApi.delete(url, { ...config }).then((response) => response.data);
}
