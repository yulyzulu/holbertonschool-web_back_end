export default class Currency {
  constructor(code, string) {
    this._code = code;
    this._string = string;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    this._code = code;
  }

  get string() {
    return this._string;
  }

  set string(string) {
    this._string = string;
  }

  displayFullCurrency() {
    return (`${this._string} (${this._code})`);
  }
}
