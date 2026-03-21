const todos = [
    {
        id : 1,
        text : "my id is 1",
        iscompleted : true
    },
    {
        id : 2,
        text : "my id is 2",
        iscompleted : false
    },
    {
        id : 3,
        text : "my id is 3",
        iscompleted : true
    }
]

console.log(todos[1].text);

const todoJSON = JSON.stringify(todos);
console.log(todoJSON);

for(let i = 0 ; i < todos.length; i++)
{
    console.log(todos[i].text)
};

for (let todo of todos){
    console.log(todo.text)
}

//foreach
todos.forEach(function(todo){
    console.log(todo.text);
})

//map
const todotext = todos.map(function(todo) {
    return todo.text;
})

//filter

const todotrue = todos.filter(function(todo){
    return todo.iscompleted === true;
}).map(function(todo){
    return todo.text;
})

console.log(todotrue);