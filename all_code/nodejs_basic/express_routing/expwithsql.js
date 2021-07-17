const express=require('express')
const app=express();
const students=require("./fakedata.js")
const port=3006;
var mysql=require('mysql');
app.use(express.json())
var connection=mysql.createConnection({
  host:"localhost",
  user:"root",
  password:"Subhash@1234",
  database:"learn"  
});
connection.connect(function(err){
  if (err)throw err;
  console.log('connected')})

  app.get('/',function(req,res,next){
   var query=`select * from ${req.body.tab}`
   connection.query(query,function(err,data){
     if (err)throw err;
     res.send(data);
   })
   ///////////////////
   app.post('/',function(req,res,next){
    var query=`alter table student add ${req.body.name} varchar(255)`
    connection.query(query,function(err,data){
      if (err)throw err;
      res.send(data);
    })})
})
app.listen(port,(req,res)=>{
  console.log(`connected${port}`)
})


