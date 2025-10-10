const p1 = fetch('https://pokeapi.co/api/v2/pokemon/2').then((res)=> {return res.json()})
const p2 = fetch('https://pokeapi.co/api/v2/pokemon/3').then((res)=> {return res.json()})
const p3 = fetch('https://pokeapi.co/api/v2/pokemon/5').then((res)=> {return res.json()})



Promise.any([p1,p2,p3]).then(
    (result) => {
        console.log('The pokemon is: ', result)
    }
).catch((error)=>{
    console.log(error)
})