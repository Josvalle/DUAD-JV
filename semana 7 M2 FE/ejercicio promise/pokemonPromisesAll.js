const p1 = fetch('https://pokeapi.co/api/v2/pokemon/2').then((res)=> {return res.json()})
const p2 = fetch('https://pokeapi.co/api/v2/pokemon/3').then((res)=> {return res.json()})
const p3 = fetch('https://pokeapi.co/api/v2/pokemon/5').then((res)=> {return res.json()})



Promise.all([p1,p2,p3]).then(
    (values) => {
        console.log('The pokemons are: ', values)
    }
).catch((error)=>{
    console.log(error)
})