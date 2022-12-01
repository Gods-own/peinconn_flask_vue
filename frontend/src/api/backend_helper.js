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
export const getUserActivities = (user_id) => get(`${url.GET_USER_ACTIVITIES}/${user_id}`);

//LIKE

//USER
export const getUserProfile = (user_id) => get(`${url.GET_USER_PROFILE}/${user_id}`);

//COUNTRY
export const getAllCountries = () => get(url.GET_COUNTRIES);

//INTEREST
export const getAllInterests = () => get(url.GET_INTERESTS);
export const getAllUserInterests = (user_id) => get(`${url.GET_USER_INTERESTS}/${user_id}`);

//Room
export const getRoomStatus = (user1_id, user2_id) => get(`${url.CHECK_ROOM_EXISTS}/${user1_id}/${user2_id}`);
export const getUserRooms = () => get(url.GET_USER_ROOMS);

//Message
export const getUserMessages = (room_name) => get(`${url.GET_USER_MESSAGES}/${room_name}`);

//Search
export const searchUser = (username, country, age, gender) => get(url.SEARCH_USER, { params: { username, country, age, gender } });
