// Q1
let passwordCorrect = true;
let otpValid = false;

let loginPossible = passwordCorrect || otpValid;
console.log(loginPossible);

// Q2
let isMember = false;
let hasCoupon = true;

let result = isMember || hasCoupon;
console.log(result);

// Q3
let age = 16;
let height = 155;

let allowed = (age > 18) || (age > 150);
console.log(allowed);

// Q4
let emailGiven = true;
let phoneGiven = false;

let valid = emailGiven || phoneGiven;
console.log(valid);

// Q5
let score = 900;
let timeBonus = true;

let result = (score > 1000) || (timeBonus == true);
console.log(result);

// Q6
let a = 0;
let b = false;
let c = "";
let d = null;
let e = 42;
let result = a || b || c || d || e;
console.log(result);                                        // Output => 42

// Q7
let x = "Hello" || 0;
let y = 0 || "Hi";
console.log(x, y);                                            // Output => Hello Hi

// Q8
let a = 10;
let b = 20;
let result = (a < 5) || (b > 15);
console.log(result);                                    // Output => true

// Q9
let val = 5;
let condition = val || (val = 0);
console.log(condition);                                          // Output => 5
console.log(val);                                                // Output => 5

// Q10
let x = "" || 0 || false || null || undefined || "OK";
console.log(x);                                                 // Output => OK