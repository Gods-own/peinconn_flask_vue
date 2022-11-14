const authUser = JSON.parse(localStorage.getItem("authenticatedUser"));

const accessToken = authUser ? authUser.bearer_token : "";
export const currUser = authUser ? authUser.user : {};

export default accessToken;
