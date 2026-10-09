// Check whether "18" != 18 returns true or false.
console.log("18"!=18);                        // Output => false

// A password is stored as "1234". User enters 1234 (number). Will != return true?
let password = "1234";
let user_enters = 1234
let result = password != user_enters
console.log(result)                                              // Output => false

// Predict the output:
console.log(5 != "5");                                   // Output => false
console.log(0 != false);                                 // Output => false

// Predict the output:
console.log(null != undefined);                             // Output => false
console.log("" != 0);                                       // Output => false

// What does NaN != NaN return? Explain.
console.log(NaN != NaN);       // NaN is not defined or in another word NaN can be any number or not a definate number.
