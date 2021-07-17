const express =require('express');
const app = express();
var jwt=require('jsonwebtoken');
app.use(express.json());
var knex=require("./database/db");
const PORT=process.env.PORT
var signup=express.Router();
app.use=("/",signup);
require("./routes/signup")(signup,jwt,knex);
app.listen(PORT,()=>{
    console.log(`server is running on PORT ${PORT}`);
})


