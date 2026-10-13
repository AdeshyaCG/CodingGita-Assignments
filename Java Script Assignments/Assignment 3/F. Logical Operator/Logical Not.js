// Q1
let isBanned = false;

let result = !isBanned;
console.log(result);

// Q2
let isCompleted = false;

let isPending = !isCompleted;
console.log(isPending);

// Q3
let isOn = true;

let isItOff = !isOn;
console.log(isItOff);

// Q4
let isActive = false;

let cannotAccess = !isActive;
console.log(cannotAccess);

// Q5
let isReadOnly = false;

let canEdited = !isReadOnly;
console.log(canEdited);

// Q6
let a = 0;
let b = 1;
console.log(!a, !b);                                // Output => true false

// Q7
let x = "Hello";
let y = "";
console.log(!x, !y);                                        // Output => false true

// Q8
let val = 5;
let result = !val;
console.log(result);                                // Output => false

// Q9
let a = 10;
let b = 20;
let result = !(a && b);
console.log(result);                                    // Output => false

// Q10
let x = 0;
let y = 1;
let result = !(x || y);
console.log(result);                                // Output => false