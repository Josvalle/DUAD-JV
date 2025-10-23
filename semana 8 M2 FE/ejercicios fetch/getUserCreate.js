const userID = 'ff8081819782e69e0199df40dc10319d'

const getUserID = async (userID) => {
    try{
    const response = await fetch(`https://api.restful-api.dev/objects/${userID}`)
    const data =await response.json()
    console.log(data)} catch(error){
        console.log('There was an error: ', error)
    }
    
}

getUserID(userID)