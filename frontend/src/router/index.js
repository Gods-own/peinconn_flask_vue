import { createRouter, createWebHistory } from "vue-router";
import RegistrationForm from "../views/authentication/RegisterForm";
import LoginForm from "../views/authentication/LoginForm";
import ActivitiesPage from "../views/activity/Activities";
import DirectInbox from "../views/message/ChatRoom";

const routes = [
  {
    path: "/register",
    name: "Register",
    component: RegistrationForm,
    meta: { requiresAuth: false },
  },
  {
    path: "/login",
    name: "Login",
    component: LoginForm,
    meta: { requiresAuth: false },
  },
  {
    path: "/activities",
    name: "Activities",
    component: ActivitiesPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/direct/inbox/:room?",
    name: "ChatRoom",
    component: DirectInbox,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.VUE_PEINCONN_APP_APIURL),
  routes,
});

export default router;
