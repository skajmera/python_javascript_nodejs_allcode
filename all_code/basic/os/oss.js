const os=require('os')
const space=os.freemem();
console.log(`${space/1024/1024/1024}`);


const total=os.totalmem();
console.log(`${total/1024/1024/1024}`);


console.log(os.hostname());


console.log(os.arch());

console.log(os.platform());

console.log(os.release());