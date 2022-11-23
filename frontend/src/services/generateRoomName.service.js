const generateName = (user1, user2) => {
  console.log(user1.username);
  console.log(user2.username);
  let a = Math.round(Math.random() * 9);
  let b = Math.round(Math.random() * 9);
  let c = Math.round(Math.random() * 9);

  let username1 = user1?.username?.charAt(1);
  let username2 = user2?.username?.charAt(1);
  let roomName = `${username1}${username2}${user1.id}${user2.id}${a}${b}${c}`;

  return roomName;
};

export default generateName;
