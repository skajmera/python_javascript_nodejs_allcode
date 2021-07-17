const knex = require('./database/db')
const express = require('express')
const app = express()
const routes = require('./routes/route')

app.use('/',require('./routes/route'))




app.listen(8000,()=>{console.log('server is running')})