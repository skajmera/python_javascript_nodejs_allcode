///////////////////////  second max 
// var a=[100,10,2,90,495,6]
// var max_=a[0]
// for (i of a){
//     if(max_<i){
//         // var sec=max_
//         max_=i
//     } 
// }
// console.log(max_);
// console.log(sec);
////////////////////////////     reverse  wrong
// var rev=["subhash","ajmera","amla"]
// var a=rev.length-1
// var reverce=[]

// for(i of rev){
//     reverce.push(rev[a])
//     a--
// }
// console.log(reverce);
/////////////////////
// var rev=["subhash","ajmera","amla"]
// var a=1
// var reverce=[]

// for(i of rev){
//     reverce.push(rev[rev.length-a])
//     a++
// }
// console.log(reverce);
////////////////////


// var rev=["subhash","ajmera","amla"]
// var a=""
// var reverce=[]
// for(i of rev){
//     a=i+" "+a
// }
// console.log(a);
////////////////////////////////////  palindrom  
// function checkPalindrom (str) {
//     return str == str.split('').reverse().join('');
//   }
//   console.log(checkPalindrom("nitin"))
//////////////////////////////////////////////

// function checkPalindrom(palindrom)
// {
//    var flag = true;
//    var j = 0;
//     for( var i = palindrom.length-1; i > palindrom.length / 2; i-- )
//     {
//         if( palindrom[i] != palindrom[j] )
//         {
//            flag = false;
//            break; 
//         }
//         j++;
//     }
//   if( flag ) {
//   console.log('the word is palindrome.');
//   }
//   else {
//     console.log('the word is not palindrome.');
//   }
// }
// checkPalindrom('nitin');
///////////////////////
// let flag=true
// let a='nitin'
// let b=1
// for(i of a){
//     if(i!=a[a.length-b]){
//         flag=false
//     break;
//     }b++
// }
// if(flag){
//     console.log("this is palindrom");
// }else{
//     console.log("this is not palindrom");
// }
///////////////////////////////////////////////////  buble sort 

// var a = [3, 6, 13, 7, 9, 6, 5]
// for (let i = 0; i < a.length; i++) {
//     for (let j = 0; j < a.length; j++) {
//         if (a[j] > a[j + 1]) {
//             b = a[j]
//             a[j] = a[j + 1]
//             a[j + 1] = b
//         }
//     }
// }
// console.log(a);
//////////////////////////// decending 
// var a = [3, 6, 13, 7, 9, 6, 5]
// for (let i = 0; i < a.length; i++) {
//     for (let j = 0; j < a.length; j++) {
//         if (a[j] < a[j + 1]) {
//             b = a[j]
//             a[j] = a[j + 1]
//             a[j + 1] = b
//         }
//     }
// }
// console.log(a);



////////////////////////////////////////////////////////////////////////// filter
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
//   console.log(studentGrades); // [ { name: 'Quincy', grade: 96 }, { name: 'Alexis', grade: 100 }, { name: 'Katie', grade: 90 } ]

///////////////////////////////////////   reduce
////// arr.reduce(callback[initialValue])

// const numbers = [1, 2, 3, 4];
// const sum = numbers.reduce(function (result, item) {
//   return result + item;     
// }, 0);
// console.log(sum); // 10
///////////////////////////////////

// var pets = ['dog', 'chicken', 'cat', 'dog', 'chicken', 'chicken', 'rabbit'];
// var petCounts = pets.reduce(function (obj, pet) {
//    if (!obj[pet]) {
//       obj[pet] = 1;
//    } else {
//       obj[pet]++;
//    }
//    return obj;
// }, {});
// console.log(petCounts);
////////////////////////////////////////////////// map
// const numbers = [65, 44, 12, 4];
// const newArr = numbers.map(myFunction)
// console.log(newArr);
// function myFunction(num) {
//   return num * 10;
// }
// ///////////////////////////////
// var express = require('express');
// var app = express();

// app.get('/', function(req, res){
//    res.cookie('name', 'express').send('cookie set'); //Sets name = express
// });
// app.listen(4000);
///////////////////////////////////////////////

// function Person(name,age,gender){
//     this.name = name;
//     this.age = age;
//     this.gender = gender;

//   }

//   var person1 = new Person("Vivek", 76, "male");
//   console.log(person1);

//   var person2 = new Person("Courtney", 34, "female");
//   console.log(person2);
// //   var person3 = new Person("Lilly", 17, "female");
///////////////////////////////////////////carrying


// function add (a) {
//     return function(b){
//       return a + b;
//     }
//   }

//   console.log(add(3)(4))
///////////////////////

// function addFourNumbers(num1,num2,num3,num4){
//     return num1 + num2 + num3 + num4;
//   }

//   let fourNumbers = [5, 6, 7, 8];


// //   console.log(addFourNumbers(...fourNumbers));
//   // Spreads [5,6,7,8] as 5,6,7,8

//   let array1 = [3, 4, 5, 6];
//   let clonedArray1 = [...array1]
//   console.log(addFourNumbers(...clonedArray1));
////////////////////////////////////////////////


// function func1(){
//     setTimeout(()=>{
//       console.log(x);
//       console.log(y);
//     },3000);

//     var x = 2;
//     let y = 12;
//   }

//   func1();
////////////////////////////

// function func2(){

//     for(var i = 0; i < 3; i++){
//         // console.log(i);
//       setTimeout(()=> console.log(i),2000);
//   }


//   }

//   func2();
//////////////////////////

//// Code 3:


//   (function(){
//     setTimeout(()=> console.log(1),2000);
//     console.log(2);
//     setTimeout(()=> console.log(3),0);
//     console.log(4);
//   })();
///////////////////////////
// let x= {}, y = {name:"Ronny"},z = {name:"John"};

// x[y] = {name:"Vivek"};
// x[z] = {name:"Akki"};
// console.log(x);
// console.log(x[y]);
//////////////


// function runFunc(){
//     console.log("1" + 1);
//     console.log("A" - 1);
//     console.log(2 + "-2" + "2");
//     console.log("Hello" - "World" + 78);
//     console.log("Hello"+ "78");
//     console.log("22"+2);
//   }

//   runFunc();

///////////////////////


// let a = 0;
// let b = false;
// console.log((a == b));
// console.log((a === b));
//////////////////////

// var x = 23;

// (function(){
//   var x = 43;
//   (function random(){
//     x++;
//     console.log(x);
//     var x = 21;
//   })()
// })()
///////////
// var x = 23;

// (function () {
//     var x = 43;
//     x++;
//     console.log(x);
//     var x = 21;
// })()
/////////////////////////////

// function random(){
//     var x; // x is hoisted
//     x++; // x is not a number since it is not initialized yet
//     console.log(x); // Outputs NaN
//     x = 21; // Initialization of x
//   }

//   random()

/////////////////////////


// var x; // x is hoisted
// x++; // x is not a number since it is not initialized yet
// console.log(x); // Outputs NaN
// var x = 21; // I 

////////////////////////////////////////////

// let hero = {
//     powerLevel: 99,
//     getPower(){
//       return this.powerLevel;
//     }
//   }

//   let getPower = hero.getPower;

//   let hero2 = {powerLevel:42};
//   console.log(getPower());
//   console.log(getPower.apply(hero2));

//////////////////////////

// const dic={"a":2,"d":{"a":4},
// 'h':9}
// // dic["a"]=0
// // dic["d"]['a']=0
// // console.log(dic)
// ////////////////////
// for(i in dic){
//     if(i==="a"){
//         dic[i]=0
//     }else if(i==="d"){
//        dic[i]["a"]=0
//     }
// }
// console.log(dic);
////////////////////////       array method      ///////////////////////////////


// let arr = ["I", "go", "home"];

// delete arr[1];
// console.log(arr.length);
// console.log(arr[2]);
/////////////////////////////////////////////////////

/////////////////// arr.splice(start[deleteCount, elem1,elemN])

// let arr = ["I", "study", "JavaScript"];
// arr.splice(1, 1); // from index 1 remove 1 element
// console.log( arr ); // ["I", "JavaScript"]
// arr.splice(1,2)
// console.log(arr);

///////////////////////////////////////
// let arr = ["I", "study", "JavaScript"];

// var h=arr.slice(1,3)
// console.log(h);
// console.log(arr);
///////////////////////////////
// let arr = ["I", "study", "JavaScript"];

// // from index 2
// // delete 0
// // then insert "complex" and "language"
// arr.splice(1, 0, "complex", "language");

// console.log( arr ); // "I", "study", "complex", "language", "JavaScript"

//////////////////////////////////

// let arr = [1, 2, 5];

// // from index -1 (one step from the end)
// // delete 0 elements,
// // then insert 3 and 4
// arr.splice(-1, 0, [3, 4]);

// console.log( arr ); // 1,2,3,4,5
//////////////////////////////////////

// let arr = ["t", "e", "s", "t"];
// console.log( arr.slice(-3) ); // e,s (copy from 1 to 3)

// console.log( arr.slice(-2) ); // s,t (copy from -2 till the end)
///////////////////////////

// let arr = [1, 2];

// // create an array from: arr and [3,4]
// console.log( arr.concat([3, 4]) ); // 1,2,3,4

// // create an array from: arr and [3,4] and [5,6]
// console.log( arr.concat([3, 4], [5, 6]) ); // 1,2,3,4,5,6

// // create an array from: arr and [3,4], then add values 5 and 6
// console.log( arr.concat([3, 4], 5, 6) ); // 1,2,3,4,5,6
//////////////////////////////////

// let arr = [1, 2];

// let arrayLike = {
//   0: "something",
//   length: 1
// };

// console.log( arr.concat(arrayLike) ); // 1,2,[object Object]
//////////////////////////////////////

// let arr = [1, 2];

// let arrayLike = {
//   0: "something",
//   1: "else",
//   [Symbol.isConcatSpreadable]: false,////true
//   length: 2
// };

// console.log( arr.concat(arrayLike) ); // 1,2,something,else
////////////////////////////


// let arr = [1, 0, false];

// console.log( arr.indexOf(0) ); // 1
// console.log( arr.indexOf() ); // 2
// console.log( arr.indexOf(null) ); // -1

// console.log( arr.includes(1) ); // true

///////////////////////////////


// const arr = [3,3,NaN,4];
// console.log( arr.indexOf(NaN) );   // -1 (should be 0, but === equality doesn't work for NaN)
// console.log( arr.includes(NaN) );  // true (correct)

//////////////////////////////////


// let users = [
//     {id: 1, name: "John"},
//     {id: 2, name: "Pete"},
//     {id: 3, name: "Mary"}
//   ];

//   let user = users.find(item => item.id ==3);

//   console.log(user.name); // John
// /////////////////////////////

// let users = [
//     {id: 1, name: "John"},
//     {id: 2, name: "Pete"},
//     {id: 3, name: "Mary"}
//   ];

//   // returns array of the first two users
//   let someUsers = users.filter(item => item.id < 3);

//   console.log(someUsers.length); // 2
//   console.log(someUsers);
///////////////////
// let lengths = ["Bilbo", "Gandalf", "Nazgul"]
// let dd=lengths.map(item => item.length);
// console.log(dd); // 5,7,6  

//////////////////////////////////////////

// let arr = [ 1, 2, 15 ];

// // the method reorders the content of arr
// arr.sort();

// console.log( arr );  // 1, 15, 2
////////////////////////////////////

// function compare(a, b) {
//     if (a > b) return 1; // if the first value is greater than the second
//     if (a == b) return 0; // if values are equal
//     if (a < b) return -1; // if the first value is less than the second
//   }

// console.log(compare(2,4))
////////////////////////////////////////      sort list      /////////////////////////

// function compareNumeric(a, b) {
//     console.log(arr);
//     console.log(a,b);
//     if (a > b) return 1;
//     if (a == b) return 0;
//     if (a < b) return -1;
// }
// let arr = [1, 2, 15, 5, 7];
// arr.sort(compareNumeric);

// console.log(arr);  // 1, 2, 

// /////////////////////////

// let arr = [ 1,4,5,62, 15 ];

// arr.sort(function(a, b) { return a - b; });

// console.log(arr);  // 1, 2, 15
//////////////////////////////

// let countries = ['Österreich', 'Andorra', 'Vietnam'];

// console.log( countries.sort( (a, b) => a > b ? 1 : -1) ); // Andorra, Vietnam, Österreich (wrong)
// console.log();( countries.sort( (a, b) => a.localeCompare(b) ) )
/////////////////////////////////////////////////
// var a=477
// var b=44
// a < b ? console.log(1) :console.log(-1);

///////////////////////////
// let names = 'Bilbo, Gandalf, Nazgul';

// let arr = names.split(', ');
// console.log(arr);
// for (let name of arr) {
//   console.log( `A message to ${name}.` )}

////////////////////////


// let str = "test";

// console.log( str.split('') ); // t,e,s,t

////////////////////


// let arr = ['Bilbo', 'Gandalf', 'Nazgul'];

// let str = arr.join(' = '); // glue the array into a string using ;

// console.log( str ); // Bilbo;Gandalf;Nazgul
///////////////

// let arr = [1, 2, 3, 4, 5];
// let h = arr.reduce((sum, current) => {
//     return sum + current
// })
// console.log(h);
///////////////////////////////////////////

// let arr = [1, 2, 3, 4, 5];
// let result = arr.reduce((sum, current) => sum + current, 0);
// console.log(result); // 15
////////////////////////////

// const person = {
//     firstName: "John",
//     lastName : "Doe",
//     id       : 5566,
//     fullName : function() {
//       return this.firstName + " " + this.lastName;
//     }
//   };
// console.log(person.fullName())
///////////////////////////////


// let a=((a)=>{
//     console.log("4",a);
// },1)
// // console.log(a);

///////////////////////


// let a=[1,2,3]

// let b=[1,2,3]
// a=b

// console.log(a===b);

// (function (){
//     console.log("subhash");
// })()
//////////////////////////

// var x = 23;

// (function(){
//   var x = 43;

//   (function (){

//     x++;
//     console.log(x);
//     var x = 21;
//   })()
// })()


////////////////////

// console.log(1 + "2" + "2");
// console.log(1 + + "2" + "2");
// console.log(1 + -"1" + "2");
// console.log(+"1" + "1" + "2");
// console.log("A" - "B" + "2");
// console.log("A" - "B" + 2);

/////////////////////////////////////

// console.log(0 || 1 && 4);
// console.log(1 || 2);
// console.log(0 && 1);
// console.log(1 && 2);
///////////////////////////////

// console.log(0==false);

/////////////////////////////



// var x = 23;

// function dd(){
//   var x = 43;

//   function f (){
//       console.log(x);
//     x++;
//     console.log(x);
//     var x = 21;
//   }f()
// }
// dd()
//////////////////



// var x = 21;
// (function() {
//     console.log(x);
// })()

///////////////////////////

// function ran() {
//     console.log(x);
//     // var x = 20;
// }

// ran()
// var  x = 21;
///////////////////////////

// var rl=require('readline-sync')

// var guess=rl.question("guess the character\n")

// console.log(guess);
//////////////////////////////////////


// a()

// function a(){
//     console.log("ajmera");
// }
////////////////////      constructor ////////////////////////////////////


// function Person(name,age,gender){
//     this.name = name;
//     this.age = age;
//     this.gender = gender;
//   }


//    var person1 = new Person("Vivek", 76, "male");
// //   console.log(person1.name);
// console.log(person1);


// //   var person2 = new Person("Courtney", 34, "female");
// //   console.log(person2);
///////////////////////////////////////////////////////////////////////  prototype  /////////


// function Student(name,rollNumber,grade,section){
//     this.name = name;
//     this.rollNumber = rollNumber;
//     this.grade = grade;
//     this.section = section;
//   }

//   // Way to add methods to a constructor function
//   Student.prototype.getDetails= function(){
//     return `Name: ${this.name}, Roll no: ${this.rollNumber}, Grade: ${this.grade}, Section:${this.section}`;
//   }


//   let student1 = new Student("Vivek", 354, "6th", "A");
//   let aa=student1.getDetails();
//   console.log(aa);
//   console.log(student1.name)
// ////////////////////////////////////////////////////////////////////////// class 

// class Student {
//     constructor(name, rollNumber, grade, section) {
//         this.name = name;
//         this.rollNumber = rollNumber;
//         this.grade = grade;
//         this.section = section;
//     }
// }

// let student2 = new Student("Garry", 673, "7th", "C");
// console.log(student2);
// console.log(student2.rollNumber)
//////////////////////////////////////////////////////////


// class Student {
//     constructor(name, rollNumber, grade, section) {
//         this.name = name;
//         this.rollNumber = rollNumber;
//         this.grade = grade;
//         this.section = section;
//     }
//     getDetails(){
//       return `Name: ${this.name}, Roll no: ${this.rollNumber}, Grade:${this.grade}, Section:${this.section}`;
//     }
// }

// let student2 = new Student("Garry", 673, "7th", "C");
//   let aa=student2.getDetails();
// console.log(aa);




/////////////////////////////////////    null   ////////////////////////////////////  

// function getVowels(str) {
//     const m = str.match(/[aeiou]/gi);
//     if (m === null) {
//       return 0;
//     }
//     return m.length;
//   }

//   console.log(getVowels('sky'));
// //////////////////////////////////////   fetch///////////////////////////////////

// const fetch = require('cross-fetch');	//npm install node-fetch
// fetch("https://pokeapi.co/api/v2/pokemon/ditto")
//   .then(res => res.json())
//   .then(json => {
//       console.log(json);
//   })
//   .catch(err => console.log(err));
// // ////////////////////////////////////

///////////////////////////////////
// const axios=require('axios')
// axios.get("https://pokeapi.co/api/v2/pokemon/ditto")
//   .then((response) => {
//       console.log(response.data);
//   })
//   .catch((error) => {
//       console.log(error);
//   })

////////////////////////////////////////// promise  //////////////////////////////



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

// console.log(promise);

// promise.then((dat)=>{
// console.log(dat);
// }).catch((err)=>{
//     console.log(err);
// })
/////////or  or  //////////////

////////////////////////////////////////  not promises use 
// const handlePromise=async()=>{
//     try{
//     let data1=await promise
//     console.log(data1);
// }
// catch(err){
//     console.log(err);
// }}
// handlePromise()

/////////////////////////////////////////////////////////////

// function a(){
// setTimeout(()=>{
//     console.log("ajmera");

// },1000)
// }
// console.log('subhash');
// a()
//////////////////////////////////////////

// "use strict"
// function a(){
// console.log(this);
// }

// a()
////////////////////////////////////////////////
// var  a={name:"sfj",age:22,fun:function aa(){
//     return this.name
// }}
// console.log(a.fun())
/////////////////////////////////////
// "use strict"

// let a=3
// console.log(a);
/////////////////////////////////
// function say(){
//     return this;
// }
// let obj={name:'subhash'}
// let a=say(obj)
// console.log(a);
// var  a=say.call(obj)
// console.log(a);
///////////////////////////////////////

// function a(){

// return this
// }
// let ss={name:"e"}
// let aa=a.call(ss)
// console.log(aa);
//////////////////////////////////////

// function name(a,b,...c) {
//     console.log(a);
//     console.log((`${a} ${b}`));
//     console.log((c));
//     console.log(c[0]);
//     console.log(c.length);
//     console.log(c.indexOf('people'));
// }
// name("subhash","parmeshwar","people","nikhil","holiday")
////////////////////////////////////////////

// const fs=require('fs')
// fs.promises.readFile('testt.txt')
// .then((result) => {
//     console.log(result.toString());
// }).catch((err) => {
//     console.log(err);

// });

//////////////////

// const fs=require('fs')
// fs.promises.readFile('testt.txt','utf-8')
// .then((result) => {
//     console.log(result);
// }).catch((err) => {
//     console.log(err);

// });
////////////////////////  synchronous ///////////////

// const fs = require('fs')
// const a = fs.readFileSync('testt.txt', 'utf-8')

// console.log(a);
// console.log("subhash");

////////////////////////////   asynchronous  //////////////////

// const fs=require('fs')
// fs.readFile('testt.txt','utf-8',(err,result)=>{
//     if(result){
//     console.log(result);
//     }
//     else{
//         console.log(err);
//     }
// })
// console.log("subhash");
/////////////////////////////////////////////////////////////////

// let isBalanced = (input) => {
//     let brackets = "[]{}()<>"
//     let stack = []
//     for(let bracket of input) {
//       let bracketsIndex = brackets.indexOf(bracket)
//       if(bracketsIndex % 2 === 0) {
//         stack.push(bracketsIndex + 1)
//       } else {
//         if(stack.pop() !== bracketsIndex) {
//           return false;
//         }
//       }
//     }
//     return stack.length === 0
//   }
//   console.log(isBalanced('[{]]}'))
//////////////////////////////////////////////////////////////

// const error=new Error("error page")
// console.log(error); 

///////////////////////////////////////////////////////////////////////////////









// var finalhandler = require('finalhandler')
// var http = require('http')
// var morgan = require('morgan')
 
// // create "middleware"
// var logger = morgan('combined')
 
// http.createServer(function (req, res) {
//   var done = finalhandler(req, res)
//   logger(req, res, function (err) {
//     if (err) return done(err)
 
//     // respond to request
//     res.setHeader('content-type', 'text/plain')
//     res.end('hello, world!')
//   })
// })

///////////////////////////////////////////////////// carrying function///

// function Myfunction(a) {
//   return (b) => {
//      return (c) => {
//        return a * b *c
//        }
//       }
//    }

//   let s=Myfunction(4)(3)(4)
//   console.log(s)
/////////////////////////////////////////////

// var express = require('express')
// var morgan = require('morgan')
// var app = express()
// app.use(morgan('dev'))
// app.get('/page', function (req, res) {
//   // res.status(404).send('page not found')
//   res.status(200).send('this is home page')
//   console.log(req.method,req.originalUrl,req.status)
//   console.log(req.statusCode);
// })
// app.listen(3003,()=>{
//   console.log("listening port");
// })



//////////////////

// let arr=[200,4,64,7,54,6,7]
// var a=(arr.slice(0,1));
// var b=(arr.slice(1,2));
// let total=(arr.slice(2));
// if(a>b){
//   var s1=a
//   var s=b
// }else{
//   var s1=b
//   var s=a
// }
// for(let i of total){
//   if(i>s1){
//     if(i>s){
//       s1=s
//       s=i
//     }else{
//       s1=i
//     }
//   }
// }
// console.log(s1);
// console.log(...s);
///////////////////////////////////////
const exp