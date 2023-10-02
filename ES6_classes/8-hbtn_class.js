class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Define a custom casting behavior for Number
  valueOf() {
    return this._size;
  }

  // Define a custom casting behavior for String
  toString() {
    return this._location;
  }
}

export default HolbertonClass;
