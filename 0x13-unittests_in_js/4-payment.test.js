const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./4-payment.js');
const sinon = require('sinon');
const Utils = require('./utils.js');

describe('Test function with sinon', function() {
  const consoleSpy = sinon.spy(console, 'log');

  it('Test calculator in Utils', function() {
    const utilsSpy = sinon.stub(Utils, 'calculateNumber');
    utilsSpy.withArgs('SUM', 100, 20).returns(10);
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
    utilsSpy.restore();
    consoleSpy.restore();
  });
});
