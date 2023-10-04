export default function signUpUser(user) {
  return new Promise((resolve) => {
    resolve({
      firstName: user,
      lastName: user,
    });
  });
}
