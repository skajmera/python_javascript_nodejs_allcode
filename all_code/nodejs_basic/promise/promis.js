



// const promise= new Promise((resolve,result)=>{
//     var data=true
//     if(data){
//         resolve("ok")
//     }else{
//         result("not ok")
//     }
// })


// promise.then((data)=>{
// console.log(data);
// }).catch((err)=>{
//     console.log(err);
// })
///////////////////////////////////////////


// const promise= new Promise((resolve,result)=>{
//     var data=false
//     if(data){
//         resolve("ok")
//     }else{
//         result("not ok")
//     }
// })
/////
// console.log(promise);

// promise.then((dat)=>{
// console.log(dat);
// }).catch((err)=>{
//     console.log(err);
// })
/////////or  ////////
////////////////////////////////////////  not promises use 
const handlePromise=async()=>{
    try{
    let data1=await promise
    console.log(data1);
}
catch(err){
    console.log(err);
}}
handlePromise()

/////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// let myPromise = new Promise(function (myResolve, myReject) {
//     let x = setTimeout(function () { myFunction("I love You !!!"); }, 3000);
//     //// x=0;
//     function myFunction(value) {
//         console.log(value);
//     };
//     if (x == 0) {
//         myResolve("OK");
//     } else {
//         myReject("Error");
//     }
// });
// myPromise.then((message) => {
//     console.log("this is in the " + message)

// }).catch((message) => {
//     console.log("this is in the catch" + message)
// })

///////////////////////////////////////



// setTimeout(function() { myFunction("I love You !!!"); }, 3000);

// function myFunction(value) {
//   console.log(value);
// }

////////////////////////////////////////////////////////////////

// let myPromise = new Promise(function(myResolve, myReject) {
//     setTimeout(function() { myResolve("I love You !!"); }, 3000);
//   });

//   myPromise.then(function(value) {
//     console.log(value);
//   });
//////////////////////////////////////////////////////////////





/////////////////////////////////////Async Syntax/////////////////////


// async function myFunction() {
//     console.log("Hello");
//   }
// myFunction();


///////////////////////////////

// async function myFunction() {
//     console.log(Promise.resolve("Hello"));
//   }
// myFunction();

/////////////////////////////////


// async function myDisplay() {
//     let myPromise = new Promise(function(myResolve, myReject) {
//       myResolve("I love You !!");
//     });
//     console.log(await myPromise);
//   }
// myDisplay();

/////////////////////////////////////////////////

// async function myDisplay() {
//     let myPromise = new Promise(function(myResolve, myReject) {
//       setTimeout(function() { myResolve("I love You !!"); }, 3000);
//     });
//     console.log(await myPromise);
//   }

//   myDisplay();


//////////////////////////////////////////////////////

//////////////////  call back function  ///////////////

// function myDisplayer(some) {
//     console.log(some);
//   }
//   function myFirst() {
//     myDisplayer("Hello");
//   }
//   function mySecond() {
//     myDisplayer("Goodbye");
//   }
//   myFirst();
//   mySecond();

/////////////////////////////////////////

// function myDisplayer(some) {
//     console.log(some);
//   }a=async ()=>{
//     let myPromise=new Promise((myResolve,myReject)=>{
//         myResolve("hello i am subhash")
//     });
//     console.log(await myPromise)
// }
// a()

//   function myFirst() {
//     myDisplayer("Hello");
//   }

//   function mySecond() {
//     myDisplayer("Goodbye");
//   }

//   mySecond();
//   myFirst();

/////////////////////////////////////////
// function myDisplayer(some) {
//     console.log(some);
//   }
//   function myCalculator(num1, num2) {
//     let sum = num1 + num2;
//     return sum;
//   }
//   let result = myCalculator(5, 5);
//   myDisplayer(result);

/////////////////////////////////////////
// function myDisplayer(some) {
//     console.log(some);
//   }
//   function myCalculator(num1, num2) {
//     let sum = num1 + num2;
//     myDisplayer(sum);
//   }
//   myCalculator(5, 5);

///////////////////////////////////////

// function myDisplayer(some) {
//     console.log(some);
// }
//   function myCalculator(num1, num2, myCallback) {
//     let sum = num1 + num2;
//     myCallback(sum);
//   }
//   myCalculator(5, 5, myDisplayer);

///////////////////////////////////////////////////////////////////////////////////
//////////////////////Asynchronous JavaScript ////////////////////
//////////////////////////////////////////////////////////////////

// function myDisplayer(some) {
//     console.log(some);
//   }function myDisplayer(some) {
//     console.log(some);
//   }
//   function myCalculator(num1, num2, myCallback) {
//     let sum = num1 + num2;
//     myCallback(sum);
//   }
//   myCalculator(5, 5, myDisplayer);
//   function myCalculator(num1, num2, myCallback) {
//     let sum = num1 + num2;
//     myCallback(sum);
//   }
//   myCalculator(8, 5, myDisplayer);

///////////////////////////////////////////////////////





///////////////////////////////////////////////


/////////////////////////////////////////////////

// a=async ()=>{
//     let myPromise=new Promise((myResolve,myReject)=>{
//         myResolve("hello i am subhash")
//     });
//     console.log(await myPromise)
// }
// a()function myDisplayer(somefunction myDisplayer(some) {
//     console.log(some);
//   }function myDisplayer(some) {
//     console.log(some);
//   }
//   function myCalculator(num1, num2, myCallback) {
//     let sum = num1 + num2;
//     myCallback(sum);
//   }
//   myCalculator(5, 5, myDisplayer);
//   function myCalculator(num1, num2, myCallback) {
//     let sum = num1 + num2;
//     myCallback(sum);
//   }
//   myCalcu) {
//     console.log(some);
//   }function myDisplayer(some) {
//     console.log(some);
//   }
//   function myCalculator(num1, num2, myCallback) {
//     let sum = num1 + num2;
//     myCallback(sum);
//   }
//   myCalculator(5, 5, myDispl
//   database: 'learn'ayer);
//   function myCalculator(num1, num2, myCallback) {
//     let sum = num1 + num2;
//     myCallback(sum);
//   }
//   myCalcu

// async function myDisplay() {
//     let myPromise = new Promise(function(myResolve, myReject) {
//       myResolve("I love You !!");
//     });
//     console.log(await myPromise);
//   }
// myDisplay();


// d=async ()=>{
//     let myPromise=new Promise((myResolve,myReject)=>{
//         myResolve("yes,I'm subhash")
//     });
//     console.log(myPromise);
// }
// d()



// async function myDisplay() {
//     let myPromise = new Promise(function(myResolve, myReject) {
//       setTimeout(function() { myResolve("I love You !!"); }, 3000);
//     });
//     console.log(myPromise);
//   }

//   myDisplay();
///////////////////////////////////
// async function myDisplay() {
//     let myPromise = new Promise(function(myResolve, myReject) {
//       setTimeout(function() { myResolve("I love You !!"); }, 3000);
//     });
//     console.log(myPromise);
//   }
//   myDisplay();
///////////////////////////////////////////////

// async function myDisplay(){
//     let myPromise=new Promise(function(myResolve,myReject){
//         setTimeout(function(){
//             myResolve("i love you");},3000);
//         });
//         console.log(await myPromise);
// }
// myDisplay();

///////////////////////////////////////////////
///////////////////////////////////////////////
