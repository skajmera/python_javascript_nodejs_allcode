
const rL = require("readline-sync");
var hangman=[ 
`+---+
 |   |
 O   |
(|)  |
| |  |
     |
=========`,     
`+---+
 |   |
 O   |
/|   |
/    |
     |
=========`,
`+---+
 |   |
 O   |
(|)  |
     |
     |
=========`,
 `+---+
 |   |
 O   |
/|   |
     |
     |
=========`,
`+---+
 |   |
 O   |
 |   |
     |
     |
     |
     |
=========`,
`+---+
 |   |
 O   |
     |
     |
     |
=========`,
`+---+
 |   |
     |
     |
     |
     |`]
console.log("wel-come")
const name= rL.question("what is yourname\n")
console.log("hello,"+name,"time to lay hangman")
var word="subhash"
var guesses=" "

while (true){
   var a=0;
   var t=7;
   while (t>0){
       var b=0;
       var i;
       for (i in word){
           if(guesses.includes(word[i])){
               console.log(word[i])
           }else{
                console.log("________")
                b++}
        }if (b==0){
            console.log("you won")
            break;}
        var guess=rL.question("guess the character\n")
        if(guesses.includes(guess)){
            console.log("already use this word")}
        guesses+=guess
        if(!word.includes(guess)){
            t-=1
            a+=1
            console.log("t="+t);
            console.log(hangman[hangman.length-a])
          //   a+=1
            console.log("you have",+t,"more guess")
            console.log("do you help me: yes/no")
            var help=rL.question("yes/no")
            if (help=="yes"){
                var m='q'
                var i;
                for (i=0; i < m.length; i++) {
                    t-=1
                    console.log("(1st chance press : 1), (2nd chance press: 2) and (3rd chance press: 3)")
                    var helpp=rL.question("you have 3 chance")
                    if (helpp==="1"){
                        console.log("*b*")
                    }else if(helpp==="2"){
                        console.log("*h*")
                    }else if (helpp==="3"){
                        console.log("*a*")}
                }}
            else if(help=="no"){
                console.log("ok")
            }
        
            if (t==0){
                console.log("you are lose")}
    }}
    console.log("do you want play: y/n")
    var again=rL.question("y/n")
    if (again=="y"){
        console.log("thank you")
        guesses="0"
        
    }else{
        console.log("good bye")
        break;}
}
// /////////////////////////////////////////////////////////////////

