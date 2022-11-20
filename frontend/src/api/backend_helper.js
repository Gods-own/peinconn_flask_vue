import { post, get, put } from "./axios_setup";
import * as url from "./peinconn_api_url";

//AUTH
export const registerUser = (registration_payload) => post(url.REGISTER_USER, registration_payload);
export const loginUser = (login_payload) => post(url.LOGIN_USER, login_payload);
export const registerUserInterest = (interest_payload) => post(url.REGISTER_INTEREST, interest_payload);

//ACTIVITY
export const createActivity = (activity_data) => post(url.CREATE_ACTIVITY, activity_data);
export const getAllActivities = () => get(url.GET_ACTIVITIES);
export const getSingleActivity = (activity_id) => get(`${url.GET_SINGLE_ACTIVITY}/${activity_id}`);
export const updateSingleActivity = (activity_id) => put(`${url.UPDATE_SINGLE_ACTIVITY}/${activity_id}`);
export const getUserActivities = () => get(url.GET_USER_ACTIVITIES);

//LIKE

//USER

//COUNTRY
export const getAllCountries = () => get(url.GET_COUNTRIES);

//INTEREST
export const getAllInterests = () => get(url.GET_INTERESTS);
export const getAllUserInterests = () => get(url.GET_USER_INTERESTS);
