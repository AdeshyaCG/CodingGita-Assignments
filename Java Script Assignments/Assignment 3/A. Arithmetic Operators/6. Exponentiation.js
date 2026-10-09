
// Q1
let side = 6;
let volume = side ** 3;
console.log(volume);  

// Q2
let cellsPerSide = 9;
let totalCells = cellsPerSide ** 2;
console.log(totalCells);  

// Q3
let base1 = 5;
let power1 = 4;
console.log(base1 ** power1);  

// Q4
let pixels = 1024;
let totalPixels = pixels ** 2;
console.log(totalPixels);  // result => 1048576

// Q5
let base = 2;
let power = -1;
let result = base ** power;
console.log(result);  // result => 0.5

// Q6
console.log(3 ** 4);  // result => 81

// Q7
let sideLength = 9;
let area = sideLength ** 2;
console.log(area);  // result => 81

// Q8
console.log(2 ** 5);  // result => 32
console.log(5 ** 2);  // result => 25
// They are not the same.

// Q9
console.log(2 ** 3 ** 2);       // result => 512
console.log((2 ** 3) ** 2);     // result => 64
console.log(2 ** -3);           // result => 0.125
// console.log(-2 ** 2);        // SyntaxError
console.log((-2) ** 2);         // result => 4
console.log(4 ** 0.5);          // result => 2

// Q10
let a = 10;
let b = 0;
let result2 = a ** b;
console.log(result2);  // result => 1