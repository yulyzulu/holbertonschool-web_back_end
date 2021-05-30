const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('Test getPaymentTokenFromAPI function', function() {
  it('Async test', (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        expect(res).to.eql({ data: 'Successful response from the API' })
      })
      done();
  });
});
