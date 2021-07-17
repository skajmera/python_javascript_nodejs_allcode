const express = require('express')
const routes = express.Router()
const {home}=require('../controller/user')
console.log(home)

routes.get('/home',home)

module.exports = routes
