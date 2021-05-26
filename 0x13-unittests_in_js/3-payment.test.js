const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./3-payment.js');
const sinon = require('sinon');
const Utils = require('./utils.js');

describe('Test function with sinon', function() {
  const utilsSpy = sinon.spy(Utils, 'calculateNumber');

  it('Test calculator in Utils', function() {
    sendPaymentRequestToApi(100, 20);
    expect(utilsSpy.calledOnce).to.be.true;
    expect(utilsSpy.calledWith('SUM', 100, 20)).to.be.true;
    utilsSpy.restore();    
  });
});
