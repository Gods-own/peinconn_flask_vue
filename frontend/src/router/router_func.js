// import router from ".";
import { currUser } from "../api/jwt-access-token.js";

const router_functions = (router) => {
  router.beforeEach((to, from, next) => {
    // instead of having to check every route record with
    // to.matched.some(record => record.meta.requiresAuth)
    if (to.meta.requiresAuth && !currUser) {
      // this route requires auth, check if logged in
      // if not, redirect to login page.
      next({
        path: "/login",
        replace: true,
      });
    } else if (to.meta.requiresAuth == false && currUser) {
      next({
        path: "/activities",
        replace: true,
      });
    } else {
      next();
    }
  });
};

export default router_functions;
