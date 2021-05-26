const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('Returns the expected sum', function() {
  it('Should return correct sum', function() {
    assert.equal(calculateNumber(3, 4), 7);
  });
  it('Should return rounded sum', function() {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
  it('Should return rounded sum', function() {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('Should return rounded sum', function() {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
  it('Should return rounded sum', function() {
    assert.equal(calculateNumber(-1.2, -3.8), -5);
  });
});
