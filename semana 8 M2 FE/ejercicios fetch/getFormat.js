const response = await fetch('https://api.restful-api.dev/objects');
const data = await response.json();


let objectsNull = [];
data.forEach(data => {
    if (data.data === null){
        console.log('nel pastel');
    }else{
        const name = data.name;
        const info = data.data;
        console.log(name, '(', info, ')' );
    }
    
});

console.log('termino');