const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('Returns the expected operation', function() {
  describe('Should return correct sum', function() {
    it('Should return positive number', function() {
      expect(calculateNumber('SUM', 3, 4)).to.equal(7);
    });
    it('Should return positive number', function() {
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    });
    it('Should return a negative number', function() {
      expect(calculateNumber('SUM', -1.2, -3.8)).to.equal(-5);
    });
  });
  describe('Should return rounded substraction', function() {
    it('Should return positive number', function() {
      expect(calculateNumber('SUBTRACT', 9, 3)).to.equal(6);
    });
    it('Should return negative number', function() {
      expect(calculateNumber('SUBTRACT', -4, 3)).to.equal(-7);
    });
    it('Should return positive number', function() {
      expect(calculateNumber('SUBTRACT', 7.4, 2)).to.equal(5);
    });
  });
  describe('It should return rounded division', function() {
    it('It should return positive number', function() {
      expect(calculateNumber('DIVIDE', 8, 2)).to.equal(4);
    });
    it('It should return Error', function() {
      expect(calculateNumber('DIVIDE', 10, 0)).to.equal('Error');
    });
    it('It should return positive number', function() {
      expect(calculateNumber('DIVIDE', 10, 2.1)).to.equal(5);
    });
  });
});
