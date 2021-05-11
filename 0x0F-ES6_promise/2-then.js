export default function handleResponseFromAPI(promise) {
  promise = new Promise((resolve, reject) => {
    if (promise) {
      resolve({status: 200, body: 'success'});
    } else {
      reject(Error());
    }
  });

  promise
    .then(res => {console.log('Got a response from the API')})
    .catch(error => {console.log(error)})

}
