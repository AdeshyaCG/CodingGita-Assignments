// Q1
let student = {
    name: "Riya",
    age: 18,
    isEnrolled: true
};

console.log(student);

console.log(student.name);
console.log(student.age);
console.log(student.isEnrolled);


// Q2
let scores = [85, 92, 78, 90];

let mixedData = [25, "Hello", true, null];

console.log(scores);
console.log(mixedData);

console.log(scores[0]); // First element
console.log(scores[3]); // Last element


// Q3
function calculateArea(length, width) {
    return length * width;
}

console.log(calculateArea(10, 5));                             // Output: 50
console.log(calculateArea(8, 4));                              // Output: 32


// Q4
let num = 42;
let text = "Hello";
let flag = true;
let nothing = null;
let obj = { name: "Riya" };
let arr = [1, 2, 3];
let func = function() {
    console.log("Hello");
};

console.log(num, typeof num);                                        // Output: number
console.log(text, typeof text);                                      // Output: string
console.log(flag, typeof flag);                                      // Output: boolean
console.log(nothing, typeof nothing);                                // Output: object
console.log(obj, typeof obj);                                        // Output: object
console.log(arr, typeof arr);                                        // Output: array
console.log(func, typeof func);                                      // Output: function