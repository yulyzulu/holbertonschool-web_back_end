const chai = require('chai');
const chaiHttp = require('chai-http');
const expect = require('chai').expect;

chai.use(chaiHttp);
const url= 'http://localhost:7865';

describe('Test server with express', function() {
  it('Check the returns', function() {
    chai.request(url)
    .get('/')
    .end((err, res) => {
      if (err) {
        throw err;
      }
      expect(res).to.have.status(200);
      expect(res.text).to.equal('Welcome to the payment system');
    })
  });
});

describe('Test server with express', function() {
  it('Check the returns', function() {
    chai.request(url)
    .get('/cart/11')
    .end((err, res) => {
      if (err) {
        throw err;
      }
      expect(res).to.have.status(200);
      expect(res.text).to.equal('Payment methods for cart 18');
    })
  });
});

describe('Test server with express', function() {
  it('Check the returns', function() {
    chai.request(url)
    .get('/cart/eleven')
    .end((err, res) => {
      if (err) {
        throw err;
      }
      expect(res).to.have.status(404);
    })
  });
});
