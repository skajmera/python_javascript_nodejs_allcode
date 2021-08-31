//////////////////////////////////////////////auth folder ke andar auth.js file 
// const jwt = require('jsonwebtoken')

// const generatToken = (data) => {
//     const token = jwt.sign(data, 'subhash')
//     return token

// }

// const accessToken = () => {
//     data = { name: "subhash" }
 
//     const decoded = jwt.verify(generatToken(data),'subhash')
//     console.log(decoded);

// }


// accessToken()

//////////////////////////////////////////////////////




const jwt = require('jsonwebtoken')

const generatToken = (data) => {
    const token = jwt.sign(data, 'subhash')
    return token

}

const accessToken = (req,res,next) => {
    ////// const token=req.headers.cookie.split("=")[1];       ('token', token)
    const token=req.headers.cookie.split("=")[0];
    const decoded = jwt.verify(token,'subhash')
  
    req.data=decoded
    next()

}


module.exports ={generatToken,accessToken}
/////////////////////////////////////////////////////                 index .js main file 




const express=require("express")
const {accessToken,generatToken}=require('./Auth/auth') 
const app=express()

app.get('/login',(req,res)=>{
    data={id:343554,name:"subhash"}
    const token=generatToken(data)
    res.cookie(token)
    ///// res.cookie('token',token)         splite[1]  ke liye open kre
    res.send('hello')
    
})

app.get('/secured',accessToken,(req,res)=>{

    res.send('secured page')
    console.log(req.data);
})
app.listen(3000,()=>console.log(`SERVER IS RUNNING...`));


