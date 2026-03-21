//oops
//es5
function person (firstName , lastName , dob) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.dob = new Date(dob);
    this.getBirthYear = function (){
        return this.dob.getFullYear();
    }
    this.getFullName = function(){
        return `${this.firstName} ${this.lastName}`;
    }
    
}


//es6

class people{
    constructor(firstName, lastName , dob){
        this.firstName = firstName;
        this.lastName = lastName;
        this.dob = dob;
    }

    getBirthYear(){
        return this.dob.getFullYear();
    }

    getFullName(){
        return `${this.firstName} ${this.lastName}`
    }
}

//instance
const instance1 = new person("rubi" , "kill" , '10-10-2000');
const instance2 = new person("tybi" , "bill" , '11-11-1988');

console.log(instance1.getFullName());
console.log(instance2);