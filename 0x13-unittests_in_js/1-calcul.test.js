const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('Returns the expected operation', function() {
  describe('Should return correct sum', function() {
    it('Should return positive number', function() {
      assert.equal(calculateNumber('SUM', 3, 4), 7);
    });
    it('Should return positive number', function() {
      assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
    });
    it('Should return a negative number', function() {
      assert.equal(calculateNumber('SUM', -1.2, -3.8), -5);
    });
  });
  describe('Should return rounded substraction', function() {
    it('Should return positive number', function() {
      assert.equal(calculateNumber('SUBTRACT', 9, 3), 6);
    });
    it('Should return negative number', function() {
      assert.equal(calculateNumber('SUBTRACT', -4, 3), -7);
    });
    it('Should return positive number', function() {
      assert.equal(calculateNumber('SUBTRACT', 7.4, 2), 5);
    });
  });
  describe('It should return rounded division', function() {
    it('It should return positive number', function() {
      assert.equal(calculateNumber('DIVIDE', 8, 2), 4);
    });
    it('It should return Error', function() {
      assert.equal(calculateNumber('DIVIDE', 10, 0), 'Error');
    });
    it('It should return positive number', function() {
      assert.equal(calculateNumber('DIVIDE', 10, 2.1), 5);
    });
  });
});
