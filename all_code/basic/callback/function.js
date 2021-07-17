// var x = function (a, b) {return(a * b)};
// var z = x(4, 3);
// console.log(z);

//////////////////////////////////

// var x = function (a, b) {return a * b};
// console.log(x(3,54))

///////////////////////////////

// var myFunction = new Function("a", "b", "return a * b");
// var x = myFunction(4, 3);
// console.log(x);

///////////////////////////////////////////////////

// var myFunction = function (a, b) {return a * b};

// var x = myFunction(4, 3);
// console.log(x);


//////////////////////////////////////////////////////

// myFunction(5);
// function myFunction(y) {
//   return (y * y);
// }
// console.log(myFunction(8));

///////////////////////////////////////////////

// (function () {
//     var x = "Hello!!"; 
//     console.log(x);
//   })();

////////////////////////////
// function myFunction(a, b) {
//     return a * b;
//   }
//   var x = myFunction(4, 3);
//   console.log(x);
/////////////////////////////////////////
// function myFunction(a, b) {
//     return a * b;
//   }
//   var x = myFunction(4, 3) * 2;
//   console.log(x);
//////////////////////////////////////////////

// function myFunction(a, b) {
//     return arguments.length;
//   }
// console.log(myFunction(3,5,6,5));

////////////////////////////////////////////////////


// function myFunction(a, b) {
//     return a * b;
//   }
//   var txt = myFunction.toString();
// console.log(txt);

/////////////////////////////////////////////////////////


///////// ES5
// var k = function(x, y) {
//     return x * y;
//   }
// console.log(k(4,67));



  ////// ES6
// const x = (x, y) => {return x * y};
// console.log(x(3,5));
  

//////////////////////////////////////////////////////

// function myFunction(x, y) {
//     if (y === undefined) {
//       y = 2;
//     }  
//     return x * y;
//   }
//   console.log(myFunction(4));

///////////////////////////////////////////////////////////

// function myFunction(x, y = 2) {
//     return x * y;
//   }
//   console.log(myFunction(4));

//////////////////////////////////////////////////

// function findMax() {
//     var i;
//     var max = -Infinity;
//     for(i = 0; i < arguments.length; i++) {
//       if (arguments[i] > max) {
//         max = arguments[i];
//       }
//     }
//     return max;
//   } 
//   console.log(findMax(4, 5, 6));

///////////////////////////////////////////////


// function sumAll() {
//   var i;
//   var sum = 0;
//   for (i = 0; i < arguments.length; i++) {
//     sum += arguments[i];
//   }
//   return sum;
// }
// x = sumAll(1, 123, 500, 115, 44, 88);
// console.log(x);

//////////////////////////////////////////////////////////////


