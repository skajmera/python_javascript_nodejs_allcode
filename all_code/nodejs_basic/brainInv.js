///////////////////////////////////////////////////// carrying function///

// function Myfunction(a) {
//     return (b) => {
//        return (c) => {
//          return a * b *c
//          }
//         }
//      }

//     let s=Myfunction(4)(3)(4)
//     console.log(s)
/////////////////////////////////////////////////////////  morgan  ///////

// var express = require('express')
// var morgan = require('morgan')

// var app = express()

// app.use(morgan('combined'))

// app.get('/', function (req, res) {
//   res.send('hello-world!')
// })

// app.listen(3000,()=>{
//   console.log("listening");
// })
/////////////////////////////////////////////  error  handling
// const error=new Error("error page")
// console.log(error); 
///////////////////////////////////////////////  bracket question////

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
/////////////////////////////////////////////////   file system  ///

// const fs=require('fs')
// fs.promises.readFile('testt.txt')
// .then((result) => {
//     console.log(result.toString());
// }).catch((err) => {
//     console.log(err);
// });
// console.log("subhash");

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
///////////////////////////////////////  rest perameter

// function name(a,b,...c) {
//     console.log(a);
//     console.log((`${a} ${b}`));
//     console.log((c));
//     console.log(c[0]);
//     console.log(c.length);
//     console.log(c.indexOf('people'));
// }
// name("subhash","parmeshwar","people","nikhil","holiday")
/////////////////////////////////////// spread operator


// function name(a,b,c,d,...e) {
//     console.log(e);
//     console.log(a[1]);
//     console.log((c));
//     console.log(c[0]);
//     console.log(c.length);
//     console.log(c.indexOf('people'));
// }
// const ss=["subhash","parmeshwar","people","nikhil","holiday","dd","df"]
// name(...ss)
////////////////////////////////////////// call methods //////

// function a(){
// return this
// }
// let ss={name:"e"}
// let aa=a.call(ss)
// console.log(aa);

//////////////////////////////
// function say(){
//     return this;
// }
// let obj={name:'subhash'}

// var a=say.call(obj)
// console.log(a);
////////////
// let a=say(obj)
// console.log(a);
////////////////     class /////////////////////

// class ajmera {
//     constructor(name, age,) {
//         this.name = name
//         this.age = age

//     } details() {
//         return `my name is ${this.name} i am ${this.age} year old`
//     }
// }
// let data = new ajmera("subhash", 23).details()
// console.log(data);

/////////////////////////////////////////// prototype

// function name(name,age) {
//     this.age=age
//     this.name=name
// }name.prototype.getdetails=()=>{
//     return ` my name is ${this.name} and i am ${this.age} year old`
// }

// let data=new name("subhash",22).getdetails()
// console.log(data);
/////////////////////////////////////////////////////////////////////////////////


// class studentDaata {
//     constructor(name, grade, sub, age) {
//         this.name = name
//         this.age = age
//         this.grade = grade
//         this.sub = sub
//     }
//     details(){
//         return `my name is ${this.name} and my subject is ${this.sub} and ${this.grade} I'm ${this.age} year old`
//     }

//     det(){
//         return `my name is ${this.name} and my subject is ${this.sub} and ${this.grade} I'm ${this.age} year old`
//     }
// }

// // const  data=new studentDaata("subhash",69,"biology",23)
// // console.log(data.details());
// // console.log(data.det());

// class software_engineer extends studentDaata{
// constructor(name,age,grade,sub,degree){
//     super(name,age,grade,sub)
//     this.degree=degree

// }

// data(){
//     return `my name is ${this.name} and my subject is ${this.sub} and ${this.grade} I'm ${this.age} year old
//     and i have degree of ${this.degree}`
// }
// }
// const  data=new software_engineer("subhash",69,"biology",23,"DCA")
// // console.log(data.details());
// console.log(data.data());
///////////////////////////////////////////////////

// let a={"s":4,"dd":function() {
//     console.log("subhash");
// },
// nex:4}
// var f=(a.dd);
// console.log(a.nex);
// f();
/////////////////////////////////////////////

