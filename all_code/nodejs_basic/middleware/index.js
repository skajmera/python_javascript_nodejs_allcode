// var express = require('express');
// var app = express();

// function loginfo(req,res,next){
//     console.log('hello from loginfo() middleware.....');
//     next();
// }
// function addData(req,res,next){
//     var person={
//         'name':"subhash",
//         "age":23
//     };
//     req.person=person
//     next();
// }
// app.use(loginfo)
// app.use(addData)

// app.use('/profile/:id([0-3]{1})', function(req, res,next){
//     var names=['subhash','ajmera','parmeshwar','rathod']
//     req.name=names[req.params.id];
//     next()
//  });


// app.get('/', function(req, res){
//    res.send('welcome to my index page');
// });

// app.get('/person', function(req, res){
//     res.send('name :'+req.person.name+',age :'+req.person.age);
//  });

//  app.get('/profile/:id([0-3]{1})', function(req, res){
//     res.send('name :'+req.name);
//  });



// app.listen(8000,()=>{
//     console.log("server connected middleware");
// })

////////////////////////////////////////////////////////////////

// var express = require('express');
// var app = express();

// //First middleware before response is sent
// app.use(function(req, res, next){
//    console.log("Start");
//    next();
// });

// //Route handler
// app.get('/', function(req, res, next){
//    res.send("Middle");
//    next();
// });


// app.use('/', function(req, res){
//    console.log('End');
// });

// app.listen(8000,()=>{
//     console.log("server connected middleware");
// })

////////////////////////////////////////////////

// var express = require('express');
// var app = express();
// var bodyParser = require('body-parser');

// //To parse URL encoded data
// app.use(bodyParser.urlencoded({ extended: false }))

// //To parse json data
// app.use(bodyParser.json())
