const http=require("http");
const server=http.createServer((req,res)=>{
    if('/'==req.url){
    // console.log(req.url);
    res.end("hello from the other side")}
    else if('/contact'==req.url){
        res.end("hello from the contact side");
    }else{
        res.end("erro 404 page don't exist")
    }
});

server.listen(8000,"localhost",()=>{
    console.log("connected");
})