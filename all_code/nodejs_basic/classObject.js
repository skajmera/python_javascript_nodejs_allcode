////////////////////      constructor ////////////////////////////////////


// function Person(name,age,gender){
//     this.name = name;
//     this.age = age;
//     this.gender = gender;
//   }

//    var person1 = new Person("Vivek", 76, "male");
//   console.log(person1.name);
// console.log(person1);

//   var person2 = new Person("Courtney", 34, "female");
//   console.log(person2);
/////////////////////////////////////////////////////////////////////  prototype  /////////


// function Student(name,rollNumber,grade,section){
//     this.name = name;
//     this.rollNumber = rollNumber;
//     this.grade = grade;
//     this.section = section;
//   }

//   // Way to add methods to a constructor function
//   Student.prototype.getDetails= function(){
//     return `Name: ${this.name}, Roll no: ${this.rollNumber}, Grade: ${this.grade}, Section:${this.section}`;
//   }
//   let student1 = new Student("Vivek", 354, "6th", "A");
//   let aa=student1.getDetails();
//   console.log(aa);
//   console.log(student1.name)
// ////////////////////////////////////////////////////////////////////////// class 

// class Student {
//     constructor(name, rollNumber, grade, section) {
//         this.name = name;
//         this.rollNumber = rollNumber;
//         this.grade = grade;
//         this.section = section;
//     }
// }
// let student2 = new Student("Garry", 673, "7th", "C");
// console.log(student2);
// console.log(student2.rollNumber)
////////////////////////////////////////////////////////


// class Student {
//     constructor(name, rollNumber, grade, section) {
//         this.name = name;
//         this.rollNumber = rollNumber;
//         this.grade = grade;
//         this.section = section;
//     }
//      getDetails(){
//       return `Name: ${this.name}, Roll no: ${this.rollNumber}, Grade:${this.grade}, Section:${this.section}`;
//     }
// }
// let student2 = new Student("Garry", 673, "7th", "C")
//   let aa=student2.getDetails();
// console.log(aa);
/////////////////////////////////////////////

// class subhash{
//     constructor(name,age){
//         this.name=name;
//         this.age;
//     }
// }
// const dat= new subhash("subhash",22);
// console.log(dat.name);
// console.log(dat);
// ///////////////////////////////////////////////

// class subhash{
//     constructor(name,sername){
//         this.name=name;
//         this.sername=sername;
//     }
//     getDetails(){
//         return `Name:${this.name}, sername:${this.sername}`
//     }
// }
// const data=new subhash("subhash","ajmera");
// const output=data.getDetails();
// console.log(output);

///////////////////////////////////////////////////////////////////////////////////////////////////////////


class studentDaata {
    constructor(name, grade, sub, age) {
        this.name = name
        this.age = age
        this.grade = grade
        this.sub = sub
    }
    details(){
        return `my name is ${this.name} and my subject is ${this.sub} and ${this.grade} I'm ${this.age} year old`
    }

    det(){
        return `my name is ${this.name} and my subject is ${this.sub} and ${this.grade} I'm ${this.age} year old`
    }
}

// const  data=new studentDaata("subhash",69,"biology",23)
// console.log(data.details());
// console.log(data.det());
///////////////////////////////////////////////// extends 
class software_engineer extends studentDaata{
constructor(name,age,grade,sub,degree){
    super(name,age,grade,sub)
    this.degree=degree

}

dataa(){
    return `my name is ${this.name} and my subject is ${this.sub} and ${this.grade} I'm ${this.age} year old
    and i have degree of ${this.degree}`
}
}
const  data=new software_engineer("subhash",69,"biology",23,"DCA")
console.log(data.dataa());

/////////////////////////////////////////////////////////////////////////////////////////////////////