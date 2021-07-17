module.exports=(singup,jwt,knex)=>{
    singup.post('/singup',(req,res)=>{
        knex.select('*'),from('anand')
        .where({"name":req.body.name,"email":req.body.email,"password":req.body.password})
        .then((data)=>{
            console.log(data,"data");
            
            // if(data.length>1){
            knex('anand').insert(req.body)
            .then((result)=>{
                console.log(result,"result");
                knex('*').from('anand')
                .where('email',req.body.email)
                .then((data)=>{
                    res.send({"success":"signup successfully"});
                }).catch((err)=>{console.log({"sorry":"something went wrong"});})
            }).catch((error)=>{console.log(error);})
        // }else{
        //     console.log("are yrr");
        // }
        }).catch((error)=>{console.log(error);})
    })
}




