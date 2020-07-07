const Car = require('./10-car.js');

class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }
  
  static get [Symbol.species]() {
    return Car;
  }
  
  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species(this._brand, this._motor, this._color, this._range);
  }
}

const ec1 = new EVCar("Tesla", "Turbo", "Red", "250");

const ec2 = ec1.cloneCar();

console.log(ec1);
console.log(ec2);