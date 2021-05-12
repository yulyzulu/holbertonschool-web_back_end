import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = {
    status: 'pending',
  };

  const promise2 = {
    status: 'pending',
  };

  try {
    const user = await signUpUser(firstName, lastName);
    promise1.status = 'fulfilled';
    promise1.value = user;
  } catch (error) {
    promise1.status = 'rejected';
    promise1.value = error.toString();
  }

  try {
    const photo = await uploadPhoto(fileName);
    promise2.status = 'fulfilled';
    promise2.value = photo;
  } catch (error) {
    promise2.status = 'rejected';
    promise2.value = error.toString();
  }

  return [promise1, promise2];
}
