// Q1
let maxWeight = 50;
let currentWeight = 50;

let result = currentWeight < maxWeight;
console.log(result);

// Q2
let presentAge = 16;
let minAge = 18;

let underage = minAge < presentAge;
console.log(underage);

// Q3
console.log(8 < 12);                                    // Output => true
console.log(20 < 10);                                   // Output => false
console.log(7 < 7);                                     // Output => false

// Q4
console.log("8" < 10);                                       // Output => true
console.log("20" < "3");                                     // Output => true
console.log("hello" < 5);                                    // Output => false

// Q5
console.log(null < 0);                                          // Output => false
console.log(undefined < 0);                                     // Output => false

// Q6
let maxCapacity = 500;
let currentCapacity = 375;

let full = currentCapacity > maxCapacity;
console.log(full);

// Q7
console.log(false < true);                                  // Output => true
console.log("5" < "15");                                    // Output => false
console.log(NaN < 10);                                      // Output => false