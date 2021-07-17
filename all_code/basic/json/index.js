const fs=require('fs');
const biodata={
    name:"subhash",
    age:23,
    gender:"m"
};
// ////////////// object ko json me converter
// const jsondata=JSON.stringify(biodata);
// console.log(jsondata);

// ////////////////// json ko object me converter
// const objectdata=JSON.parse(jsondata);
// console.log(objectdata);
// console.log(objectdata.name)
// ////////////////////////////////////////  json file created 

// const jsondata=JSON.stringify(biodata);
// fs.writeFile("json1.json",jsondata,(err)=>{
//     console.log("done");
// })


/////////////////////////////// json file read

fs.readFile("json1.json","utf-8",(err,data)=>{
    // console.log(data);
    const objdata=JSON.parse(data)
    console.log(objdata);    
});

///////////////////////////////////////////


