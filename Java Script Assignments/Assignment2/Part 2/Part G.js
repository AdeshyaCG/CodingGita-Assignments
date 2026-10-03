// Q8
let a;
let b = null;
let c = 42;
let d = "Hello";
let e = true;
let f = Symbol("key");
let g = 123n;

console.log(typeof a, a);            // Output: undefined
console.log(typeof b, b);            // Output: object
console.log(typeof c, c);            // Output: number
console.log(typeof d, d);            // Output: string
console.log(typeof e, e);            // Output: boolean
console.log(typeof f, f);            // Output: symabol
console.log(typeof g, g);            // Output: BigInt


// Q9
let num = 10;
let text = "Hello";
let flag = true;
let empty;
let nothing = null;
let unique = Symbol("id");
let big = 9007199254740991n;

console.log(num, text, flag, empty, nothing, unique, big);


// Q10
// A] Main difference:

// Primitive: Stores a single, simple value directly.
// Non-Primitive: Stores collections or more complex data and can contain multiple values.

// Example:

let age = 20;              // Primitive
let student1 = {name: "Arnav", age: 18};  // Non-Primitive

// b) Why are they called Primitive?
//    => Number, String, Boolean, Undefined, Null, Symbol, and BigInt are called Primitive because they are the basic, built-in data types in JavaScript. They represent a single value and are not objects.

// c) Non-Primitive example:
//      Object is a Non-Primitive data type because it can store multiple values as key-value pairs.

let student2 = {
    name: "Dhru",
    age: 15
};

// Here, one object contains multiple pieces of data (name and age), so it is Non-Primitive.