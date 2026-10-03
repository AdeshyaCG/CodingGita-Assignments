// Q11
console.log(a);
console.log(b);
console.log(c);
var a = 10;
let b = 20;
const c = 30;

// console.log(a); prints undefined
// console.log(b); throws ReferenceError: Cannot access 'b' before initialization
// console.log(c);  Never executes (the script terminates at line 2 due to the unhandled ReferenceError). If line 2 were commented out, line 3 would throw ReferenceError: Cannot access 'c' before initialization.

// Q12
var x = "Hello";
let y = "World";
const z = "!";

console.log(x);
console.log(y);
console.log(z);
console.log(x + " " + y + z);