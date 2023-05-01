import { post, get, put } from "./axios_setup";
import * as url from "./peinconn_api_url";

//AUTH
export const registerUser = (registration_payload) => post(url.REGISTER_USER, registration_payload);
export const loginUser = (login_payload) => post(url.LOGIN_USER, login_payload);
export const registerUserInterest = (interest_payload) => post(url.REGISTER_INTEREST, interest_payload);

//ACTIVITY
export const createActivity = (activity_data) => post(url.CREATE_ACTIVITY, activity_data);
export const getAllActivities = (params) => get(url.GET_ACTIVITIES, { params: params });
export const getSingleActivity = (activity_id) => get(`${url.GET_SINGLE_ACTIVITY}/${activity_id}`);
export const updateSingleActivity = (activity_id) => put(`${url.UPDATE_SINGLE_ACTIVITY}/${activity_id}`);
export const getUserActivities = (user_id, params) => get(`${url.GET_USER_ACTIVITIES}/${user_id}`, { params: params });

//LIKE
export const toggleLike = (activity_id) => put(`${url.TOGGLE_LIKE}/${activity_id}`);
export const likeStatus = (activity_id) => get(`${url.TOGGLE_LIKE}/${activity_id}`);
export const getLikers = (activity_id) => get(`${url.GET_LIKERS}/${activity_id}`);

//USER
export const getUserProfile = (user_id) => get(`${url.GET_USER_PROFILE}/${user_id}`);

//COUNTRY
export const getAllCountries = () => get(url.GET_COUNTRIES);

//INTEREST
export const getAllInterests = () => get(url.GET_INTERESTS);
export const getAllUserInterests = (user_id) => get(`${url.GET_USER_INTERESTS}/${user_id}`);

//Room
export const getRoomStatus = (user1_id, user2_id) => get(`${url.CHECK_ROOM_EXISTS}/${user1_id}/${user2_id}`);
export const getUserRooms = (params) => get(url.GET_USER_ROOMS, { params: params });

//Message
export const getUserMessages = (room_name, params) => get(`${url.GET_USER_MESSAGES}/${room_name}`, { params: params });

//Search
export const searchUser = (searchdata) => get(url.SEARCH_USER, { params: searchdata });
