const EventEmitter=require('events');
const event=new EventEmitter();
// event.on("sayMyname",()=>{
//     console.log("your name is subhash");
// })   

// event.on("sayMyname",()=>{
//     console.log("your name is ajmera");
// })   
// event.on("sayMyname",()=>{
//     console.log("your name is skajmera");
// })   
// event.emit("sayMyname");

///////////////////////////////////////

event.on("checkpage",(sc,msg)=>{
    console.log(`status code is ${sc} and the page is ${msg}`)});

    event.emit("checkpage",200,"ok");