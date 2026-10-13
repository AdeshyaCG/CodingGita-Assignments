// Q1
let username = "admin";
let password= 1234;

let result = username && password;
console.log(result);

// Q2
let isLoggedIn = true;
let hasPermission = true;

let canAccess = isLoggedIn && hasPermission;
console.log(canAccess);

// Q3
let inStock = true;
let price = 800;

console.log(inStock = true && price < 1000);

// Q4
let marks = 75;
let attendance = 80;

console.log(marks > 65 && attendance > 70);

// Q5
let isWeekend = true;
let isHoliday = false;

console.log(isWeekend == true && isHoliday == true);

// Q6
let a = 0;
let b = 10;
let result = a && b;
console.log(result);                            // Output => 0

// Q7
let x = 5;
let y = 10;
let result = (x > 3 && y) || 0;
console.log(result);                                        // Output => 10

// Q8
let p = "Hello";
let q = "";
let r = "World";
let result = p && q && r;
console.log(result);                            // Output => 

// Q9
let val = 5;
let condition = val && (val = 0);
console.log(condition);                             // Output => 0
console.log(val);                                   // Output => 0

// Q10
let x = 10;
let y = 20;
let result = (x && y) && (x > y);
console.log(result);                                    // Output => false