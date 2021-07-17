const expreess=require('express');
const router=expreess.Router();


router.get('/',(req,res)=>{
    res.sendFile(__dirname+'/index.html');
});

router.get('/register',(req,res)=>{
    res.sendFile(__dirname+'/register.html');
});

router.get('/login',(req,res)=>{
    res.sendFile(__dirname+'/login.html');
});
module.exports=router;

