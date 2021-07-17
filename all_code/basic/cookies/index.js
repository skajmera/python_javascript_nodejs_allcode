const express=require('express');
const app= express()
var cookieParser = require('cookie-parser');
app.use(cookieParser());
app.get("/",(req,res)=>{
    // res.cookie("cookie1","subhash ajmera").send('cookie has been set');
    // res.cookie("cookie1","parmeshwar",{expire:Date.now()+36000}).send("cookie has been set1")
    res.cookie("mycookie3","parmeshwar",{maxAge:36000}).send("cookie has been set3")
})

app.get("/show",(req,res)=>{
    res.send(req.cookies);
})
app.get("/delete",(req,res)=>{
    res.clearCookie('cookie1').send("cookie1 has been deleted")
})
app.listen(3009,()=>{
    console.log("server start")
})


//////////////////////////////////////////////////////////////////////


// var express = require('express');
// var app = express();

// app.get('/', function(req, res,next){
// //    res.cookie('name', 'express').send('cookie set'); //Sets name = express
// res.cookie('name', 'value', {expire: 360000 + Date.now()}).send('yes bro'); 

// // res.cookie('name', 'value', {maxAge: 360000}).send('ok');
// next()
// });


//////////////////////////////////////////////////////

// app.get('/clear_cookie_foo', function(req, res){
//    res.clearCookie('foo');
//    res.send('cookie foo cleared');
// });

// app.listen(3000,()=>{
//     console.log("connected");
// });
