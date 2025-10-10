const user = fetch(`https://reqres.in/api/users/23`)

user.then((resolve) =>{
    return resolve.json()
}).then(data => {
    console.log('The user is: ',data)
}).catch(error => console.log('The was an error: ', error))

