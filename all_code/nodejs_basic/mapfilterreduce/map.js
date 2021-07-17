// var new_array = arr.map(function callback(element, index, array) {
//     // Return value for new_array
// }[thisArg])

// const { rejects } = require("assert/strict");
// const { resolve } = require("path/posix");

// const { lookup } = require("dns")
// const { stringify } = require("querystring")

///////////////////////////

// const numbers = [1, 2, 3, 4];
// const evens = numbers.filter(item => item % 2 === 0);
// console.log(evens); 

//////////////////////////

// const students = [
//     { name: 'Quincy', grade: 96 },
//     { name: 'Jason', grade: 84 },
//     { name: 'Alexis', grade: 100 },
//     { name: 'Sam', grade: 65 },
//     { name: 'Katie', grade: 90 }
//   ];
//   const studentGrades = students.filter(student => student.grade >= 90);
//   return studentGrades; // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]
///////////////////////////////////////

// arr.reduce(callback[initialValue])
// const numbers = [1, 2, 3, 4];
// const sum = numbers.reduce(function (result, item) {
//   return result + item;
// }, 0);
// console.log(sum); // 10
/////////////////////////////////////
// var pets = ['dog', 'chicken', 'cat', 'dog', 'chicken', 'chicken', 'rabbit'];

// var petCounts = pets.reduce(function(obj, pet){
//     if (!obj[pet]) {
//         obj[pet] = 1;
//     } else {
//         obj[pet]++;
//     }
//     return obj;
// }, {});
///////////////////////////////////

////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////  forEach loop  ///////////////////

// const arr=[2,4,6,78,8]
// arr.forEach(function(item){
//     console.log(item);
// })

////////////////////////////////////////////////// filter  ////////////

// const arr=[2,4,6,78,8]
// const newarr= arr.filter(function(item){
//     if(item<=5){
//         return item
//     }
// })
// console.log(newarr);


// ///////////////////////////////////////////////////////////  map  /////////////////////


// const arr=[2,4,6,7,8,9];
// const secarr=arr.map(function(item){
//     return item
// })
// console.log(secarr);

///////////////////////////////////////// sorted array  ////////////////
// const arr=[2,44,67,78,6,7,8,9];
// const sortedarr=arr.sort((a,b)=>{
//     // if(a>b){
//     //     return 1
//     // }else{
//     //     return -1
//     // }
// })
// console.log(sortedarr)
//////////////////////////////////////

// const arr=[2,44,67,78,6,7,8,9];
// const sortedarr=arr.sort((a,b)=>{
//     return b-a;
// })
// console.log(sortedarr)

///////////////////////////////////////  reduce  ///////////

// const arr=[2,44,67,78,6,7,8,9];
// const total = arr.reduce((total,item)=>{
//     return total+item;
// },0)
// console.log(total);
//////////////////////////////////////////

// const arr=[2,44,67,78,6,7,8,9];
// const d=arr.map(x=>x+2);
// console.log(d);

/////////////////////////////////////////////////

// const arr=[2,44,67,78,6,7,8,9];
// const d=arr.filter(x=>x<20);
// console.log(d);


///////////////////////////////////////////

// const arr=[2,44,67,78,6,7,8,9];
// const d=arr.reduce((total,item)=>{
//     return total+item
// });
// console.log(d);
///////////////////////////////////////
// const arr=[1,2,3,4,5,6,7,8,9];
// const d=arr.reduce((total,item)=>{
//     return total+item;
// },10);
// console.log(d);
//////////////////////////////////////////////////
// const arr=[2,44,67,78,6,7,8,9];
// arr.forEach(element => {
//     console.log(element+5);
// });
/////////////////////////////////////////////////

// const arr=[2,44,67,78,6,7,8,9];
// var b=arr.map(test);
// console.log(b);

// function test(x){
//     return x*10
// }
//////////////////////////////////////

// const arr=[2,4,6,8];
// const secarr=arr.map(function(item){
//     return item*2
// })
// console.log(secarr);

//////////////////////////
// function hide(a,callback) {
//     var b="hello"+callback
//   console.log(b);
// }
//   function show(callback) {

//       console.log(callback);
//   }


// hide()
// show("navgurukul");

// function hide(a,callback) {
//     var b="hello"+callback
//   console.log(b);
// }
//   function show(callback) {

//       console.log(callback);
//   }


// hide()
// show("navgurukul");



// var newPromise=newPromise(resolve,reject)=>{
//     if(reject){
//         console.log("room is not clean");
//     }else{
//         console.log("room is clean");
//     }
// }




// const arr=["a","b","c","d","a","d","a"];
// const asd=arr.filter(x=>x=="a");
// console.log(asd);

////////////////////////////////////////////////////

// const arr=['a','b','c','a']
// const newarr= arr.filter(function(item){
//     if(item==="a"){
//         return item
//     }
// })
// console.log(newarr);
///////////////////////////////////////////////

// function hide() {

//     return ("hello");
// }
// function show() {
//     var b=hide()
//     return (b+" "+"navgurukul");
// }
// // console.log(hide() + " " + show())
// console.log(show());
//////////////////////////////////////////////


// function hide() {
//     var b=show()
//     return ("hello"+" "+b);
// }
// function show() {
//     return ("navgurukul");
// }
// console.log(hide());

//////////////////////////////////////////////
 