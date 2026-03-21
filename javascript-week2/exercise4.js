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