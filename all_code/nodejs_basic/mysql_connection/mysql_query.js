const express = require("express");
const Router=express.Router();
const mysqlconnection=require("./connection")

Router.get("/",(req,res)=>{
    mysqlconnection.query("select * from student",(err,rows)=>{
        if(!err){
            res.send(rows);
        }else{
            console.log(err);
        }
    })
})
module.exports=Router;





