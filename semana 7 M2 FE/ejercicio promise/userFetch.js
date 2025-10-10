userID = 2

const user = fetch(`https://jsonplaceholder.typicode.com/users/${userID}`)

user.then((resolve) =>{
    return resolve.json()
}).then(data => {
    console.log('The user is: ',data)
})

