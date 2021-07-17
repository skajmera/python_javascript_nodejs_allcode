const expreess=require('express');
const {register}=require('./controllers/auth')
const {login}=require('./controllers/auth')
const router=expreess.Router();


router.post('/register',register);
router.post('/login',login);

module.exports=router;
