const assert = require('assert');
const sum = require('./0-calcul');

describe('Returns the expected sum', function(){
  it('Should return correct sum', function() {
    assert.equal(sum.calculateNumber(3, 4), 7);
  });
  it('Should return rounded sum', function() {
    assert.equal(sum.calculateNumber(1, 3.7), 5);
  });
});
