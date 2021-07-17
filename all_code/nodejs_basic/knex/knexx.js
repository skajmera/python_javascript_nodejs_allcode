///////////  npm i knex mysql2

// const options = {
//     client: 'mysql2',
//     connection: {
//         host: '127.0.0.1',
//         user: 'root',
//         password: 'Subhash@1234',
//         database: 'mydb'
//     }
// }

// var knex = require('knex')(options);

// knex.raw("SELECT VERSION()").then(
//     (version) => console.log((version[0][0]))
// ).catch((err) => { console.log( err); throw err })
//     .finally(() => {
//         knex.destroy();
//     });
////////////////////////////////////////////////////////////
                                // table created
/////////////////////////////////////

// var knex = require("knex") ({

//     // const options = {
//         client: 'mysql2',
//         connection: {
//             host: '127.0.0.1',
//             user: 'root',
//             password: 'Subhash@1234',
//             database: 'subhash'
//         }
//     // }
// })

// knex.schema.createTable("users", (table) => {
//     table.increments('id').primary();
//     table.string('name');
//     table.string('email');
//     table.string('password');
// }).then(() => {
//     console.log("success created");
// }).catch(() => {
//     console.log("!created err");
// })




// var knex = require('knex')(options);
// knex.schema.createTable('shubhdip5', (table) => {
//     table.increments('id')
//     table.string('name')
//     table.integer('price')
// }).then(() => console.log("table created"))
//     .catch((err) => { console.log(err); throw err })
//     .finally(() => {
//         knex.destroy();
//     });


/////////////////////////////////////////////
                            //  data   insert
//////////////////////////////



// const options = {
//     client: 'mysql2',
//     connection: {
//         host: '127.0.0.1',
//         user: 'root',
//         password: 'Subhash@1234',
//         database: 'mydb'
//     }
// }

// const knex = require('knex')(options);hey

// const cars = [
//     { name: 'Audi', price: 52642 },
//     { name: 'Mercedes', price: 57127 },
//     { name: 'Skoda', price: 9000 },
//     { name: 'Volvo', price: 29000 },
//     { name: 'Bentley', price: 350000 },
//     { name: 'Citroen', price: 21000 },
//     { name: 'Hummer', price: 41400 },
//     { name: 'Volkswagen', price: 21600 },
// ]

// knex('cars').insert(cars).then(() => console.log("data inserted"))
//     .catch((err) => { console.log(err); throw err })
//     .finally(() => {
//         knex.destroy();
//     });

//////////////////////////////////////////////////////////////////
             ///in the following example, we select all rows from the cars table.

//////////////////////////////////////////////

// const options = {
//     client: 'mysql2',
//     connection: {
//         host: '127.0.0.1',
//         user: 'root',
//         password: 'Subhash@',
//         database: 'mydb'
//     }
// }

// const knex = require('knex')(options);

// knex.from('cars').select("*")
//     .then((rows) => {
//         for (row of rows) {
//             console.log(`${row['id']} ${row['name']} ${row['price']}`);
//         }
//     }).catch((err) => { console.log( err); throw err })
//     .finally(() => {
//         knex.destroy();
//     });
///////////////////////////////////////////////////////

////The SQL WHERE clause is used to define the condition to be met-
////// for the rows to be returned.


// const options = {
//     client: 'mysql2',
//     connection: "mysql://root:Subhash@1234@localhost:3306/mydb"
// }

// const knex = require('knex')(options);

// knex.from('cars').select("name", "price").where('price', '>', '50000')
//     .then((rows) => {
//         for (row of rows) {
//             console.log(`${row['name']} ${row['price']}`);
//         }
//     })
//     .catch((err) => { console.log( err); throw err })
//     .finally(() => {
//         knex.destroy();
//     });

//////////////////////////////////////////////////

///////////////////////We can order data withhey orderBy() function.

// const options = {
//     client: 'mysql2',
//     connection: {
//         host: '127.0.0.1',
//         user: 'root',
//         password: 'Subhash@1234',
//         database: 'learn'
//     }
// }

// const knex = require('knex')(options);

// knex.from('cars').select('name', 'price').orderBy('price', 'desc')
//     .then((rows) => {
//         for (row of rows) {
//             console.log(`${row['name']} ${row['price']}`);
//         }
//     }).catch((err) => { console.log( err); throw err })
//     .finally(() => {
//         knex.destroy();
//     });

///////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


//                     //////   knex other website

////

 //                    //////////////////////////////////////////////////

               
// const knex = require('knex')({
//   client: 'mysql',
//   connection: {
//     host : '127.0.0.1',
//     user : 'root',
//     password : 'Subhash@1234',
//     database : 'subhash'
//   }
// });   


//////////////////////////////////////////////
// const pg = require('knex')({
//   client: 'pg',
//   connection: process.env.PG_CONNECTION_STRING,
//   searchPath: ['knex', 'public'],
// });

///////////////////////////////////////
///Note: When you use the SQLite3 adapter, there is a filename required, not a network connection. For example:

// const knex = require('knex')({
//   client: 'sqlite3',
//   connection: {
//     filename: "./subhash.sqlite"
//   }
// });

//////////////////////////////////////////////////////


// const knex = require('knex')({
//   client: 'pg',
//   version: '7.2',
//   connection: {
//     host : '127.0.0.1',
//     user : 'root',
//     password : 'Subhash@1234',
//     database : 'subhash'
//   }
// });
////////////////////////////////////


// const pg = require('knex')({client: 'pg'});
// knex('table').insert({a: 'b'}).returning('*').toString();
// // "insert into "table" ("a") values ('b')"

// pg('table').insert({a: 'b'}).returning('*').toString();
// // "insert into "table" ("a") values ('b') returning *"


///////////////////////////////////////////



// const knex = require('knex')({
//   client: 'mysql',
//   connection: {
//     host : '127.0.0.1',
//     user : 'root',
//     password : 'Subhash@1234',
//     database : 'subhash'
//   },
//   migrations: {
//     tableName: 'migrations'
//   }
// });

///////////////////////////////////////////////////





// const knex = require('knex')({
//   client: 'mysql',
//   // overly simplified snake_case -> camelCase converter
//   postProcessResponse: (result, queryContext) => {
//     // TODO: add special case for raw results (depends on dialect)
//     if (Array.isArray(result)) {
//       return result.map(row => convertToCamel(row));
//     } else {
//       return convertToCamel(result);
//     }
//   }
// });



/////////////////////////////////


//////////////////////////////////////////////////////////////////////////////////





////////////////////////////////////////////////


/////////////////////////////////////


////////////////////////////




// const options = {
//   client: 'mysql2',
//   connection: {
//       host: '127.0.0.1',
//       user: 'root',
//       password: 'Subhash@1234',
//       database: 'learn'
//   }
// }

// const knex = require('knex')(options);

// knex.from('student').select('name', 'country').orderBy('country', 'desc')
//   .then((rows) => {
//       for (row of rows) {
//           console.log(`${row['name']} ${row['country']}`);
//       }
//   }).catch((err) => { console.log( err); throw err })
//   .finally(() => {
//       knex.destroy();
//   });


/////////////////////////////////////////


// const options = {
//     client: 'mysql2',
//     connection: "mysql://root:Subhash@1234@localhost:3306/learn"
// }

// const knex = require('knex')(options);

// knex.from('student').select("name", "id").where('id', '<', '500')
//     .then((rows) => {
//         for (row of rows) {
//             console.log(`${row['name']} ${row['id']}`);
//         }
//     })
//     .catch((err) => { console.log( err); throw err })
//     .finally(() => {
//         knex.destroy();
//     });

//////////////////////////////////////////////////////////////



// const options = {
//     client: 'mysql2',
//     connection: {
//         host: '127.0.0.1',
//         user: 'root',
//         password: 'Subhash@1234',
//         database: 'learn'
//     }
// }

// var knex = require('knex')(options);
// knex.select().table('student')
// knex.select('id', 'name').from('student')
// knex.select().from('student').timeout(1000)
// knex.column('name','id','city').select().from('student')
// knex.select('*').from('student')
// knex.select('id').from('student')///undefined
// knex('student').where('id', 23)
// knex('student').whereNot('id', 1)
// const subquery = knex('student').where('id', '<', 100).andWhere('name', 'sahyog').orWhere('name', 'subhash').select('id')
// knex('student').whereBetween('id', [1, 100])
// knex('student').whereNotBetween('id', [1, 100])
// knex('student').whereRaw('id = ?', [246])
// knex.from('student').select("*")

    // .then((rows) => {
    //     for (row of rows) {
    //         console.log(`${row['id']} ${row['name']} ${row['city']}`);
    //     }
    // }).catch((err) => { console.log( err); throw err })
    // .finally(() => {
    //     knex.destroy();
    // });
