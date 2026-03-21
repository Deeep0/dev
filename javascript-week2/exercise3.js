const person = {
    first_name : "john",
    last_name : "hing",
    age : 20,
    hobbies : ["movies" , "sports" , "guitar"],
    address : {
        street : "123",
        city : "la",
        state : "ma" 
    }

}

person.email = "john1234@gmail.com"

console.log(person.first_name)
console.log(person.hobbies[1])
console.log(person.address.city)

//pulling out 

const {first_name , last_name, address : {city}} = person;
console.log(first_name);
console.log(city);