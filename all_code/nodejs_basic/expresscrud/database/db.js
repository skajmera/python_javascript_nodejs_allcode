const { exists } = require('fs');

const env=require('dotenv').config();
var knex=require('knex')({
    client:"mysql",
    connection:{
        host:process.env.DB_HOST,
        user:process.env.DB_USER,
        password:process.env.DB_PASS,
        database:process.env.DB_NAME
    }
})
knex.schema.createTable('anand',(table)=>{
    table.increments('id').primary();
    table.string('name');       
    table.string('email');
    table.string('password');
})
.then(()=>{
    console.log({"success":"user table created successfully"});
})
.catch((err)=>{
    console.log(err);
})
module.exports=knex;



