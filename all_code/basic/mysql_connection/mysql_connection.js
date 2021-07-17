
var mysqlconnection=mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"Subhash@1234",
    database:"learn",
    // multipleStatements:true
});

mysqlconnection.connect((err)=>{
    if(!err){
        console.log("connected");
    }else{
        console.log("connection failed");
    }
})


module.exports=mysqlconnection;