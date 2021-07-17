

////////////////////////////////////////////////////////


// var mysql = require('mysql');

// var con = mysql.createConnection({
//   host: "localhost",
//   user: "root",
//   password: "Subhash@1234",
//   database:"learn"
// });

// con.connect(function(err) {
//   if (err) throw err;
//   console.log("Connected!");
// });


// con.query('select * from student',(err,resp)=>{
//     if (err) throw err
//     console.log(resp)
// })

///////////////////////////////////////////////////////////



// var mysql = require('mysql');
// var con = mysql.createConnection({
//   host: "localhost",
//   user: "root",
//   password: "Subhash@1234",
//   database:"learn"
// });
// con.connect(function(err) {
//   if (err) throw err;
//   console.log("Connected!");
//   var j="select * from student"
//   con.query(j, function (err, result) {
//     if (err) throw err;
//     console.log(result);
//   });
// });
/////////////////////////////////////////////////////
// var mysql = require('mysql');

// var con = mysql.createConnection({
//   host: "localhost",
//   user: "root",
//   password: "Subhash@1234",
//   database: "mydb"
// });

// con.connect(function(err) {
//   if (err) throw err;
//   console.log("Connected!");
//   var sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))";
//   con.query(sql, function (err, result) {
//     if (err) throw err;
//     console.log("Table created");
//   });
// });
////////////////////////////////////////////