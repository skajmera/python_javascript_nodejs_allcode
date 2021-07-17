const mysql = require ("mysql");
const jwt=require('jsonwebtoken');
const bcrypt=require('bcryptjs');
const db=mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"Subhash@1234",
    database:"subhash"  
});

exports.login=async(req,res)=>{
    try {
        const {email,password}=req.body;
        if(!email||!password){
          
            res.send({message:"please provide email and password"})
        }
db.query('select * from anand where email = ?',[email],async(error,results)=>{
    console.log(results);
    if(!results|| !(await bcrypt.compare(password,results[0].password))){
       
        res.send({message:"email and password incorrect"})
    }
    else{
        const id=results[0].id;
        const token=jwt.sign({id},"mysupersecretpassword",{
            expiresIn:"90d"
        })
        console.log("the token is:"+token);
        const cookieOptions={
            expires:new Date(
                Date.now()+90*24*60*60*1000
            ),
            httpOnly:true
        }
        res.cookie('jwt',token);
        res.send(
            {message:"successfully login"})

    }
})
    } catch (error) {
        console.log(error);
    }
}

exports.register=(req,res)=>{
    console.log(req.body);
    // const name=req.body.name;
    // const email=req.body.email;
    // const password=req.body.password;
    // const passwordConfirm=req.body.passwordConfirm;

    const{name,email,password,passwordConfirm}=req.body;
    db.query('select email from anand where email=?',[email],async(error,results)=>{
        if(error){
            console.log(error);
        }
        console.log(req.body);
        if (results.length>0){
          
            res.send({"message":"that email is already in use"})
        }else if(password!==passwordConfirm){
            
            res.send({"message":"password do not match"})
            
        }

        let hashedPassword=await bcrypt.hash(password,8);

        console.log(hashedPassword);
        db.query('INSERT INTO anand SET ?',{name:name,email:email,password:hashedPassword},(error,results)=>{
            if(error){
                console.log(error);
            }else{
                console.log(results);
              


                res.send({"message":"user register"})
                
            }
        })

    })
}

console.log();