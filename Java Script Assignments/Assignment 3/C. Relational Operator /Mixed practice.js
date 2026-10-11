// Q1 Write expressions to check:

// Whether age 18 is greater than or equal to voting age 18.
let ageLimit = 18;
let currentage = 18;

let result = ageLimit >= currentage;
console.log(result);

// Whether temperature 32 is less than 35.
let maxTemp = 35;
let temp = 32;

let result1 = maxTemp < temp;
console.log(result1);

// Whether score 90 is greater than 85.
let score1 = 90;
let score2 = 85;

let result2 = score1 >= score2;
console.log(result2);

// Q2
console.log(10 > 5 && 5 < 10);                          // Output => true
console.log("10" >= 10);                                // Output => true
console.log(null <= undefined);                         // Output => false
console.log("5" < "10" && 5 > 2);                       // Output => false

// Q3
let cost = 499;
let customerHas = 500;

let result4 = customerHas >= cost;
let changeWillLeft = cost < customerHas;

console.log(result4);
console.log(changeWillLeft);

