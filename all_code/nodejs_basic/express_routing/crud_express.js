const express=require('express')
const app=express();
const students=require("./fakedata.js")
const port=3004;

////////////////////get  /////////////////////////////////
app.use(express.json())
app.get('/',(req,res)=>{
    res.send(req.body);
});

app.get('/students',(req,res)=>{
    res.json(students)
})
// /////////////////post   ////////////////////////////////////

app.post('/astudents',(req,res)=>{
    let user=({id:students.length+1,
        first_name:req.body.name,
        last_name:req.body.password,
        email:req.body.email})
    console.log(user);     
    students.push(user)
    res.send(students)
})
// //////////////////////// put   /////////////////////////////////////////////

app.put('/astudents/:id',(req,res)=>{
    let id=req.params.id
    //// console.log(id)
    //// res.json(id)
    let first_name=req.body.name
    let last_name=req.body.password
    let email=req.body.email
    let index=students.findIndex((student)=>{
        return (student.id==Number.parseInt(id))
    })
    if (index>=0){
        let std=students[index]
        std.first_name=first_name
        std.last_name=last_name
        std.email=email
        res.json(std)
    }else{
        res.status(404)
        res.end()
    }
})
// ///////////////////////////delete   /////////////////////////////////////////
// app.delete('/astudents/:id',(req,res)=>{
//     let id=req.params.id;
//     let index=students.findIndex((student)=>{
//         return student.id==Number.parseInt(id);
//     })
//     //// console.log(id,req.body,index);
//     if (index>=0){
//         let std=students[index]
//         students.splice(index,1)
//         res.json(std)
//     }else{
//         res.status(404)
//     }
// })

app.listen(port,()=>{
    console.log(`listening ${port}`);
})

// ///////////////////////////////////////////////////////////////////////////////////////
// // 