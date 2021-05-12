import { uploadPhoto, createUser } from "./utils";

export default async function asyncUploadUser() {
  let user = {};
  let photo = {};

  try {
    user = await createUser();
    photo = await uploadPhoto();
  } catch (error) {
    user = null;
    photo = null;
  }
  return ({
    photo,
    user,
  });
}
