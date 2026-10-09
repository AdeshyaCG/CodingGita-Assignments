// Q1
let a = "25";
let b = 25;    
console.log("Result", a===b);      // Result => False because type of a is string and b is a number

// Q2
let first = 0;
let second = false; 
console.log("Result", first === second)    // Result => False because first is a number value and second is bool
console.log(null === undefined)            // Result => False because type of null is object and undifined is undefined

// Q3
console.log(10 === "10");           // Result => False because type of "10" is string and 10 is a number
console.log(true === 1);            // Result => False because type of true is bool and tyoe of 1 is number

// Q4
console.log("" === 0);
console.log([] === false);         // Result => False because type of [] is object and type of false is bool

// Q5
// We prefer === over == in real world because "===" compares value and type and "==" only compares value not type
