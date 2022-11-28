import { createRouter, createWebHistory } from "vue-router";
import RegistrationForm from "../views/authentication/RegisterForm";
import LoginForm from "../views/authentication/LoginForm";
import LogoutForm from "../views/authentication/LogoutForm";
import ActivitiesPage from "../views/activity/Activities";
import DirectInbox from "../views/message/ChatRoom";
import UserProfile from "../views/profile/UserProfile";
import RegisterInterest from "../views/authentication/RegisterInterest";
import router_functions from "./router_func";

const routes = [
  {
    path: "/register",
    name: "Register",
    component: RegistrationForm,
    meta: { requiresAuth: false, requiresNav: false },
  },
  {
    path: "/login",
    name: "Login",
    component: LoginForm,
    meta: { requiresAuth: false, requiresNav: false },
  },
  {
    path: "/logout",
    name: "Logout",
    component: LogoutForm,
    meta: { requiresAuth: true, requiresNav: false },
  },
  {
    path: "/register/interest",
    name: "InterestPage",
    component: RegisterInterest,
    meta: { requiresAuth: true, requiresNav: false },
  },
  {
    path: "/activities",
    name: "Activities",
    component: ActivitiesPage,
    meta: { requiresAuth: true, requiresNav: true },
  },
  {
    path: "/direct/inbox/:userId?/:room?",
    name: "ChatRoom",
    component: DirectInbox,
    meta: { requiresAuth: true, requiresNav: true },
  },
  {
    path: "/profile/:userId",
    name: "Profile",
    component: UserProfile,
    meta: { requiresAuth: true, requiresNav: true },
  },
  { path: "/", redirect: { name: "Login" } },
];

const router = createRouter({
  history: createWebHistory(process.env.VUE_PEINCONN_APP_APIURL),
  routes,
});

router_functions(router);

export default router;
