// const express = require('express');
// const app = express();
// const port = 3000;

// const { report } = require("process")

// const jwt=require("jsonwebtoken")
// const createToken= async()=>{
//     const token=await jwt.sign({id:"12"},"mynameissubhashajmeraamlatehsilkhategaonmp",{
//         expiresIn:"2 seconds"
//     })
//     console.log(token);
//     const userver=await jwt.verify(token,"mynameissubhashajmeraamlatehsilkhategaonmp")
//     console.log(userver);
// }
// createToken();
// app.listen(port,()=>{
//     console.log(`server is running at port no ${port}`);
// })

//////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////        youtube  ///////////////////////////

///////////////////////////////////////////////////  jsonwebtoken  ////////////////////////////////////


// const express=require('express');
// const jwt=require('jsonwebtoken');
// const app=express();
// app.get('/app',(req,res)=>{
//     res.send({
//         'name':"subhash"
//     })
// })
// ///////////////////////////////////////
// app.post('/app/login',(req,res)=>{
//     const user={id:3}
//     const token=jwt.sign({user},'mysecretkey');
//     res.json({
//         token:token
//     })
// })
// ////////////////////////////////////

// app.get('/app/protected',ensureToken,(req,res)=>{
//     jwt.verify(req.token,'mysecretkey',function(err,data){
//         if(err){
//             res.sendStatus(403)
//         }else{
//             res.json({
//                 text:'this is protected',
//                 data:data
//             })
//         };
//     })
    
// })
// function ensureToken(req,res,next){
//     const bearerHeader=req.headers["authorization"];
//     if(typeof bearerHeader!=='undefined'){
//         const bearer=bearerHeader.split(" ")
//         const bearerToken=bearer[1];
//         req.token=bearerToken;
//         next();
//     }else{
//         res.sendStatus(403)
//     }
// }



// ///////////////////////////////////////////

// app.listen(4000,()=>{
//     console.log("server is running");
// })
// /////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////


//const express=require('express')
//const app=express();
//
//function generateAccessToken(username) {
//    return jwt.sign({id:2}, 'secretkey', { expiresIn: '1800s' });
//  }
//  app.post('/api/createNewUser', (req, res) => {
//    const token = generateAccessToken({ username: req.body.username });
//    res.json(token);
//  });
///////////////////////////
