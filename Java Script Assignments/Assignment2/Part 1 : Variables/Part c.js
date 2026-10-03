// Q9
// 20
//ReferenceError: y is not defined
//ReferenceError: z is not defined


//var x = 10; declares x in the surrounding function/global scope.
//Inside the if block, var x = 20; does not create a new block-scoped variable. var is function-scoped, so it reassigns the existing x from 10 to 20.

// Q10
const name = "John";

let age = 20;
age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";

    console.log(country);
}

console.log(city);

const score = 50;
console.log(score);
