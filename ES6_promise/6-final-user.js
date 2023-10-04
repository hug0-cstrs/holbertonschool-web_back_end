import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((values) => {
      const results = [];
      values.forEach((value) => {
        if (value.status === 'fulfilled') {
          results.push(value.value);
        } else {
          results.push(value.reason.toString());
        }
      });
      return results;
    });
}
