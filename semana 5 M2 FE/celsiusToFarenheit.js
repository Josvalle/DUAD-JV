const celsiusList = [0,36,77,15,40]

const converter = celsiusList.map((temp) =>{
    return (temp*9/5)+32
})

console.log(converter)