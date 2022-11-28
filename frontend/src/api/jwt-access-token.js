import moment from "moment/moment";

export const checkAuthUser = () => {
  let authUser = JSON.parse(localStorage.getItem("authenticatedUser"));
  if (!authUser) {
    console.log("dd1");
    return undefined;
  } else if (authUser) {
    let token_time = authUser.user.token_expiry;
    let current_time_in_utc = moment.utc().format("YYYY-MM-DDTHH:mm:ss.SSS");
    let isexpired = moment(token_time).isBefore(current_time_in_utc);
    if (isexpired) {
      console.log("dd2");
      return undefined;
    } else {
      console.log("dd3");
      return authUser;
    }
  }
};

const authUser = checkAuthUser();

const accessToken = authUser ? authUser.bearer_token : "";
export const currUser = authUser ? authUser.user : undefined;

export default accessToken;
