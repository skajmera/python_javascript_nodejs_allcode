const knex = require('knex')({
client:"mysql",
connection:{
    host:"localhost",
    user:"root",
    password:"Subhash@1234",
    database:"subhash"
}
})

knex.schema.createTable('siddik',(table)=>{
    table.increments('id').primary();
    table.string('name');
    table.string('email');
    table.string('password')
}).then(()=>{console.log('table created')})
.catch(()=>{console.log('not created')})

module.exports = knex