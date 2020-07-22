const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('checks the output', () => {
    assert.strictEqual(calculateNumber(1.1, 2.5), 4);
    assert.strictEqual(calculateNumber(0.0, 0), 0);
  });
  it('negative numbers', () => {
    assert.strictEqual(calculateNumber(-1, 1), 0);
    assert.strictEqual(calculateNumber(-1.5, 0), -1);
  });
  it('checks arguments', () => {
    assert.strictEqual(isNaN(calculateNumber(2.2)), true);
    assert.strictEqual(isNaN(calculateNumber()), true);
  });
});
