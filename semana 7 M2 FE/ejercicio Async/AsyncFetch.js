
console.log('esperando result')



const user =  await fetch(`https://jsonplaceholder.typicode.com/users/2`);
console.log('Response Recevied ')
console.log(await user.json())