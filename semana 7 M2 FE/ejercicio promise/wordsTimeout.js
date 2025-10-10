const words = ["very", "dogs", "cute", "are"]

const w1 = new Promise (resolve =>{
    setTimeout(() => {
        resolve(words[1])
    }, 2000);
})
const w2 = new Promise (resolve =>{
    setTimeout(() => {
        resolve(words[3])
    }, 3000);
})

const w3 = new Promise (resolve =>{
    setTimeout(() => {
        resolve(words[0])
    }, 4000);
})

const w4 = new Promise (resolve =>{
    setTimeout(() => {
        resolve(words[2])
    }, 4000);
})

Promise.all([w1,w2,w3,w4]).then(
    (values) => {
        console.log('The phrase is: ', values)
    }
).catch((error)=>{
    console.log(error)
})