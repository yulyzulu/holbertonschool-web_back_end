const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./5-payment.js');
const sinon = require('sinon');
const Utils = require('./utils.js');

describe('Test function with sinon - hooks', function() {
  let consoleSpy;
  beforeEach(function() {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    consoleSpy.restore();
  });

  it('Test sendPaymentRequestToAPI', function() {
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
  });

  it('Test sendPaymentRequestToAPI', function() {
    sendPaymentRequestToApi(10, 10);
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
  });
});
