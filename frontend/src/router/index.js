import { createRouter, createWebHistory } from "vue-router";
import RegistrationForm from "../views/authentication/RegisterForm";
import LoginForm from "../views/authentication/LoginForm";
import ActivitiesPage from "../views/activity/Activities";

const routes = [
  {
    path: "/register",
    name: "register",
    component: RegistrationForm,
    meta: { requiresAuth: false },
  },
  {
    path: "/login",
    name: "login",
    component: LoginForm,
    meta: { requiresAuth: false },
  },
  {
    path: "/activities",
    name: "activities",
    component: ActivitiesPage,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.VUE_PEINCONN_APP_APIURL),
  routes,
});

export default router;
