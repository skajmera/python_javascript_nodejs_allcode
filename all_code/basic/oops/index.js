// class students{
//     biodata(){
//         console.log("hi i am a class method");
//     }
// }
// let obj1=new students();
// obj1.biodata();

/////////////////////////////////////////////////////////////////////////////////

// class students{
//     constructor(name,age,city){
//         this.myname=name;
//         this.age=age
//         this.city=city
//     }
//     biodata(){
//         console.log(`hi i am ${this.myname},I am ${this.age} years old from ${this.city}`)
//     }
// }
// let obj1=new students('subhash ajmera',23,'mp');
// let obj2=new students('parmeshwar rathod',20,'mh');

// obj1.biodata();
// obj2.biodata();
///////////////////////////////////////////////////////////////////////////////////


// class students{
//     constructor(name,age,city){
//         this.myname=name;
//         this.age=age
//         this.city=city
//     }
//     biodata(){
//         console.log(`hi i am ${this.myname},I am ${this.age} years old from ${this.city}`)
//     }
// }
// class player extends students{

// }
// let obj1=new player('subhash ajmera',23,'mp');
// let obj2=new player('parmeshwar rathod',20,'mh');
// console.log(obj1);
// // obj1.biodata();
// obj2.biodata();
/////////////////////////////////////////////////////////////////////////////////////////////

// class students{
//     constructor(name,age,city){
//         this.myname=name;
//         this.age=age
//         this.city=city
//     }
//     biodata(){
//         console.log(`hi i am ${this.myname},I am ${this.age} years old from ${this.city}`)
//     }
// }
// class player extends students{
//     constructor(name,age,city,game){
//         super(name,age,city)
//         this.mygame=game;
//     }
//     biodata(){
//         console.log(`hi i am ${this.myname},I am ${this.age} years old from ${this.city}.I am like this game ${this.mygame}`)
//     }
// }
// let obj1=new player('subhash ajmera',23,'mp','free fire');
// obj1.biodata();

////////////////////////////////////////////////////////////////////////////////////////////////


// class students{
//     constructor(name,age,city){
//         this.myname=name;
//         this.age=age
//         this.city=city
//     }
//     biodata(){
//         return `hi i am ${this.myname},I am ${this.age} years old from ${this.city}`
//     }
// }
// class player extends students{
//     constructor(name,age,city,game){
//         super(name,age,city)
//         this.mygame=game;
//     }
//     play_biodata(){
//         return `${super.biodata()}.I am player of ${this.mygame}`;
//     }
// }
// let obj1=new player('subhash ajmera',23,'mp','free fire');
// console.log(obj1.play_biodata());

////////////////////////////////////////////////////////////////////////////////

