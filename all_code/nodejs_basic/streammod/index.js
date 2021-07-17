// const fs=require("fs");
// const http=require("http");
// const server=http.createServer();

// server.on("request",(req,res)=>{
//     var fs=require('fs');
//     fs.readFile("input.txt",(err,data)=>{
//         if(err)return console.error(err);
//         res.end(data.toString());
//     })})
/////////////////////////////////////////////////////
// server.on("request",(req,res)=>{
// const rstream=fs.createReadStream("input.txt");
// rstream.on('data',(chunkdata)=>{
//     res.write(chunkdata)
// });
// rstream.on('end',()=>{
//     res.end();
// })
// rstream.on("error",(err)=>{
//     console.log(err);
//     res.end("file not found")
// })
// });

////////////////////////////////////////////////////////////

// server.on("request",(req,res)=>{
// const rstream=fs.createReadStream("input.txt");
// rstream.pipe(res)})


////////////////////////////////////////////////////

// server.listen(8004,"localhost",()=>{
//     console.log("server connected");
// });server.listen(8004,"localhost",()=>{
//     console.log("server connected");
// });



//////////////////////////////////////  wtitestream //////////////

// var fs = require("fs");
// var data = 'Simply Easy Learning';

// // Create a writable stream
// var writerStream = fs.createWriteStream('output.txt');

// // Write the data to stream with encoding to be utf8
// writerStream.write(data,'UTF8');

// // Mark the end of file
// writerStream.end();

// // Handle stream events --> finish, and error
// writerStream.on('finish', function() {
//    console.log("Write completed.");
// });

// writerStream.on('error', function(err) {
//    console.log(err.stack);
// });

// console.log("Program Ended");
/////////////////////////////////////////////////////

// var fs = require("fs");
// var data = '';

// // Create a readable stream
// var readerStream = fs.createReadStream('input.txt');

// // Set the encoding to be utf8. 
// readerStream.setEncoding('UTF8');

// // Handle stream events --> data, end, and error
// readerStream.on('data', function(chunk) {
//    data += chunk;
// });
// readerStream.on('end',function() {
//    console.log(data);
// });

// readerStream.on('error', function(err) {
//    console.log(err.stack);
// });

// console.log("Program Ended");





///////////////////////////////////////////////////////////////////

// var fs = require("fs");

// // Create a readable stream
// var readerStream = fs.createReadStream('input.txt');

// // Create a writable stream
// var writerStream = fs.createWriteStream('output.txt');

// // Pipe the read and write operations
// // read input.txt and write data to output.txt
// readerStream.pipe(writerStream);

// console.log("Program Ended");

/////////////////////////////////////////

// var fs = require("fs");
// var zlib = require('zlib');

// // Compress the file input.txt to input.txt.gz
// fs.createReadStream('input.txt')
//    .pipe(zlib.createGzip())
//    .pipe(fs.createWriteStream('input.txt.gz'));
  
// console.log("File Compressed.");
/////////////////////////////////////

// var fs = require("fs");
// var zlib = require('zlib');

// // Decompress the file input.txt.gz to input.txt
// fs.createReadStream('input.txt.gz')
//    .pipe(zlib.createGunzip())
//    .pipe(fs.createWriteStream('input.txt'));
  
// console.log("File Decompressed.");

///////////////////////////// 
