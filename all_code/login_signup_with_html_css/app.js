
const express =require ("express");
const mysql = require ("mysql");
const path=require("path");
var hbs = require('hbs');
const cookieParser =require('cookie-parser');
const app =express();
const db=mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"Subhash@1234",
    database:"subhash"  
});
const publicDirectory=path.join(__dirname,'../expressbythapa')
// console.log(publicDirectory)
app.use(express.static(publicDirectory))
/////parse url-encoded bodies(as sent by html form)
app.use(express.urlencoded({extended:false}));
////parse json bodies (as sent by api clients)
app.use(express.json())
app.use(cookieParser());
app.set('view engine','hbs');
app.set('views','');

db.connect((error)=>{
    if(error){
        console.log(error);
    }else{
        console.log("mysql connected...");
    }
});


app.use('/',require(__dirname+'/pages.js'))
app.use('/auth',require(__dirname+'/auth.js'))


app.listen(3006,()=>{
    console.log("server started on port 5001");
})
