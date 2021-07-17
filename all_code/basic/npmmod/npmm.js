const chalk =require('chalk');
const validator=require('validator')


// console.log(chalk.red("hello world"));
// console.log(chalk.red.italic("hello world"));
// console.log(chalk.blue.underline.inverse("success"));

////////////////////////////////////////
///////////////////////  validator  //////////////////////

const res=validator.isEmail('thapa@thapa.com')
console.log(res ? chalk.green.inverse(res):chalk.red.inverse(res));

 