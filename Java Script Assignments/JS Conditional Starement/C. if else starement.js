// Q1
let monthNumber = 4;
if (monthNumber==12 || monthNumber == 1 || monthNumber == 2){
    console.log("Winter");
}else if (monthNumber==3 || monthNumber == 4 || monthNumber==5){
    console.log("Summer");
}else if(monthNumber==6 || monthNumber == 7 || monthNumber==8){
    console.log("Monsoon");
}else if(monthNumber==9 || monthNumber==10 || monthNumber==11){
    console.log("Autumn");
}else{
    console.log("Invalid month number");
}

// Q2
let income = 500000;
if(income<300000){
    console.log("No tax");
}else if(income>300000 && income<700000){
    console.log("5% tax");
}else if(income>700000 && income<1000000){
    console.log("10% tax");
}
else if(income>1000000){
    console.log("15% tax");
}else{
    console.log("Invalid Income")
}

// Q3
let marks = 85;
if (marks>=90){
    console.log("Outstanding");
}else if(marks>=70 && marks<=89){
    console.logaa("Good");
}else if(marks>=40 && marks<=69){
    console.log("Average")
}else if(marks<40){
    console.log("Needs Improvement")
}else{
    console.log("Invalid Marks")
}

// Q4
let speed = 60;
if (speed>40){
    console.log("Slow")
}else if(speed>=40 && speed<=80){
    console.log("Normal")
}else if(speed>80){
    console.log("Fast")
}else{
    console.log("Invalid speed")
}

// Q5
let height = 160;
if (height<150){
    console.log("Short")
}else if(height>=150 && height<=170){
    console.log("Average")
}else if (height>170){
    console.log("Tall")
}else{
    console.log("Invalid Height")
}