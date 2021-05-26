const assert = require('assert');
const sum = require('./0-calcul.js');

describe('Returns the expected sum', () => {
  it('Should return correct sum', () => {
    assert.equal(sum.calculateNumber(3, 4), 7);
  });
  it('Should return rounded sum', () => {
    assert.equal(sum.calculateNumber(1, 3.7), 5);
  });
  it('Should return rounded sum', () => {
    assert.equal(sum.calculateNumber(1.2, 3.7), 5);
  });
  it('Should return rounded sum', () => {
    assert.equal(sum.calculateNumber(1.5, 3.7), 6);
  });
});
